from flask import render_template_string, request, Blueprint
from database import Database
from datetime import datetime
import pytz

thongkeAd_bp = Blueprint('thongkeAd', __name__, url_prefix='/thongkeAd')
tz = pytz.timezone("Asia/Ho_Chi_Minh")
now = datetime.now(tz)
current_year = now.year  

@thongkeAd_bp.route('/', methods=['GET', 'POST'])
def index():
    month = request.form.get('month')
    year = request.form.get('year')
    admin_id = request.form.get('admin_id')

    month = int(month) if month and month.isdigit() else now.month
    year = int(year) if year and year.isdigit() else current_year
    admin_id = int(admin_id) if admin_id and admin_id.isdigit() else 0

    db = Database()

    admins = db.fetch_data("SELECT id, username FROM admin")
    admin_name = "Tất cả"
    if admin_id > 0:
        admin_result = db.fetch_one(f"SELECT username FROM admin WHERE id = {admin_id}")
        if admin_result:
            admin_name = admin_result['username']

    query_orders = """
    SELECT COUNT(*) AS total_orders, SUM(total_price) AS total_revenue
    FROM donhang WHERE status = 'completed'
    """
    if month > 0:
        query_orders += f" AND MONTH(created_at) = {month}"
    if year > 0:
        query_orders += f" AND YEAR(created_at) = {year}"
    if admin_id > 0:
        query_orders += f" AND admin_id = {admin_id}"
    result = db.fetch_one(query_orders)

    total_orders = result['total_orders'] if result else 0
    total_revenue = result['total_revenue'] if result and result['total_revenue'] else 0.0
    total_revenue_formatted = "{:,.0f}".format(total_revenue)

    # Thống kê khách hàng (KHÔNG lọc theo admin)
    query_customers = "SELECT COUNT(*) AS total_customers FROM users WHERE 1=1"
    customers_result = db.fetch_one(query_customers)
    total_customers = customers_result['total_customers'] if customers_result else 0

    # Query doanh thu & số đơn hàng theo tháng trong năm
    query_monthly_stats = """
    SELECT MONTH(created_at) AS month, SUM(total_price) AS total_revenue_month, COUNT(*) AS total_orders_month
    FROM donhang 
    WHERE status = 'completed' AND YEAR(created_at) = %s
    GROUP BY MONTH(created_at)
    """
    monthly_stats_all = db.fetch_data(query_monthly_stats, (year,))

    # Lọc ra chỉ tháng hiện tại
    monthly_stats = [m for m in monthly_stats_all if m['month'] == month]

    # Nếu tháng hiện tại chưa có dữ liệu, tạo mặc định
    if not monthly_stats:
        monthly_stats = [{
            'month': month,
            'total_revenue_month': 0,
            'total_orders_month': 0
        }]

    # Query chi tiêu của tháng hiện tại
    query_monthly_expense = """
    SELECT SUM( unit_import_price) AS total_expense
    FROM nhaphang
    WHERE MONTH(created_at) = %s AND YEAR(created_at) = %s
    """
    expense_result = db.fetch_one(query_monthly_expense, (month, year))
    total_expense_month = float(expense_result['total_expense']) if expense_result and expense_result['total_expense'] else 0
    expense_by_month = {month: total_expense_month}

    # Thống kê theo năm (KHÔNG lọc theo admin)
    query_yearly_stats = """
    SELECT YEAR(created_at) AS year, SUM(total_price) AS total_revenue_year, COUNT(*) AS total_orders_year
    FROM donhang WHERE status = 'completed'
    GROUP BY YEAR(created_at)
    """
    yearly_stats = db.fetch_data(query_yearly_stats)
    query_yearly_expense = """
    SELECT YEAR(created_at) AS year, SUM(unit_import_price) AS total_expense
    FROM nhaphang
    GROUP BY YEAR(created_at)
    """
    yearly_expenses = db.fetch_data(query_yearly_expense)
    expense_by_year = {e['year']: e['total_expense'] for e in yearly_expenses}
    # Tính lợi nhuận và tỷ lệ theo tháng
    for m in monthly_stats:
        month_num = m['month']
        revenue = float(m['total_revenue_month'] or 0)
        expense = float(expense_by_month.get(month_num, 0) or 0)
        profit = revenue - expense
        percent = (profit / expense * 100) if expense > 0 else 0
        m['total_expense'] = expense
        m['profit'] = profit
        m['profit_percent'] = percent

    # Tính lợi nhuận và tỷ lệ theo năm
    for y in yearly_stats:
        year_num = y['year']
        revenue = float(y['total_revenue_year'] or 0)
        expense = float(expense_by_year.get(year_num, 0) or 0)
        profit = revenue - expense
        percent = (profit / expense * 100) if expense > 0 else 0
        y['total_expense'] = expense
        y['profit'] = profit
        y['profit_percent'] = percent

    # Tổng hợp lãi theo tháng
    total_monthly_profit = sum(float(m['profit']) for m in monthly_stats)
    total_monthly_expense = sum(float(m['total_expense']) for m in monthly_stats)
    avg_monthly_percent = (total_monthly_profit / total_monthly_expense * 100) if total_monthly_expense > 0 else 0

    # Tổng hợp lãi theo năm
    total_yearly_profit = sum(float(y['profit']) for y in yearly_stats)
    total_yearly_expense = sum(float(y['total_expense']) for y in yearly_stats)
    avg_yearly_percent = (total_yearly_profit / total_yearly_expense * 100) if total_yearly_expense > 0 else 0

    db.close()
    PAGE_TEMPLATE = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>📊 Báo cáo thống kê</title>
        <style>
            body { background: linear-gradient(to bottom right, #4CAF50, #f5f5f5); }
            .container { max-width: 1000px; margin: auto; background: rgba(255, 255, 255, 0.85); padding: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);border-radius: 5px; }
            h1 { text-align: center; color: #333; }
            .report-item { margin: 20px 0; font-size: 18px; }
            .report-item span { font-weight: bold; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            table, th, td { border: 1px solid #ddd; }
            th, td { padding: 8px; text-align: center; }
            th { background-color: #f4f4f4; }
            select { padding: 5px; margin-right: 10px; }
            .filter-box { border: 2px solid #ccc; padding: 10px; margin-top: 20px; background-color: #fee; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .back-btn-container { text-align: right; width: 100%; }
            .back-btn { margin-top: 5px; display: inline-block; padding: 8px 12px; background: #ffeb3b; border-radius: 5px; text-decoration: none; color: #333; font-weight: bold; }  
            .back-btn:hover { background: #f1d15f; }
            .h1-box { display: inline-block; padding: 10px 20px; border: 3px solid #ff5e62; border-radius: 8px;
            background: #FFDAB9; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2); color: #333; font-size: 28px; font-weight: bold; text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.3); }
            .report-profit {display: inline-block;text-align: left;font-size: 14px;color: #006400;font-weight: bold;background: #e7ffe7;padding: 8px 16px;
            border-radius: 8px;border: 2px solid #9acd32;margin-top: 15px;box-shadow: 0 2px 5px rgba(0, 100, 0, 0.1);max-width: 500px;}

        </style>
    </head>
    <body>
        <div class="container">
            <div style="text-align: center;">
            <h1 class="h1-box">📊 Báo cáo thống kê</h1>
            </div>  
            <div class="back-btn-container">
                <a href="/muaAd" class="back-btn">⬅ Quay lại</a>
            </div>  
            <div class="report-item"><span>Số lượng khách hàng:</span> {{ total_customers }}</div>
                <h2>📅 Thống kê tháng :</h2>

            <table>
                <thead><tr><th>Tháng</th><th>Nhập hàng</th><th>Số đơn hàng đã hoàn thành</th><th>Doanh thu</th></tr></thead>
                <tbody>
    {% for m in monthly_stats %}
        <tr>
            <td>{{ m['month'] }}</td>
            <td>{{ "{:,.2f}".format(expense_by_month.get(m['month'], 0)) }}</td>            
            <td>{{ m['total_orders_month'] }}</td>
            <td>{{ "{:,.2f}".format(m['total_revenue_month']) }}</td>
            
        </tr>
    {% endfor %}
</tbody>

            </table>
<div class="report-profit">
    <span>Lợi nhuận tháng:</span> {{ "{:,.0f}".format(total_monthly_profit) }} VNĐ &nbsp; | &nbsp;
    <span>Lãi suất trung bình:</span> {{ "{:.2f}".format(avg_monthly_percent) }}%
</div>

            <h2>📅 Thống kê theo năm:</h2>
            <table>
                <thead><tr><th>Năm</th><th>Nhập hàng</th><th>Số đơn hàng đã hoàn thành</th><th>Doanh thu</th></tr></thead>
                <tbody>
                    {% for y in yearly_stats %}
                        <td>{{ y['year'] }}</td>
                        <td>{{ "{:,.2f}".format(expense_by_year.get(y['year'], 0)) }}</td> 
                        <td>{{ y['total_orders_year'] }}</td>
                        <td>{{ "{:,.2f}".format(y['total_revenue_year']) }}</td>                                                                 
                    {% endfor %}
                </tbody>
            </table>
            <div class="report-profit" >
                <span>Lợi nhuận năm:</span> {{ "{:,.0f}".format(total_yearly_profit) }} VNĐ &nbsp; | &nbsp;
                <span>Lãi suất trung bình:</span> {{ "{:.2f}".format(avg_yearly_percent) }}%
            </div>

        <div class="filter-box">
            <form id="filterForm" method="post" action="#stat-options">
                <h2 id="stat-options" style="text-align: center;color: #1e90ff;">Xem chi tiết</h2>
            <label for="month">Tháng:</label>
            <select name="month" id="month">
                <option value="0">Tất cả</option>
                {% for m in range(1, 13) %}
                    <option value="{{ m }}" {% if m == month %}selected{% endif %}>Tháng {{ m }}</option>
                {% endfor %}
            </select>
                <label for="year">Năm:</label>
                <select name="year" id="year">
                    {% for y in range(2020, 2026) %}
                        <option value="{{ y }}" {% if y == year %}selected{% endif %}>{{ y }}</option>
                    {% endfor %}
                </select>

                <label for="admin_id">Nhân viên:</label>
                <select name="admin_id" id="admin_id">
                    <option value="0">Tất cả</option>
                    {% for a in admins %}
                        <option value="{{ a['id'] }}" {% if a['id'] == admin_id %}selected{% endif %}>{{ a['username'] }}</option>
                    {% endfor %}
                </select>
                <button type="submit">Xem thống kê</button>
            </form>
            <div class="report-item"><span>Nhân viên:</span> {{ admin_name }}</div>
            <div class="report-item"><span>Tổng số đơn hàng đã hoàn thành:</span> {{ total_orders }}</div>
            <div class="report-item"><span>Tổng doanh thu:</span> {{ total_revenue }} VNĐ</div>
        </div>
    </div>
<script>
    document.getElementById("filterForm").addEventListener("submit", function () {
        setTimeout(function () {
            const section = document.getElementById("stat-options");
            if (section) {
                section.scrollIntoView({ behavior: "smooth" });
            }
        }, 300); // Delay chút để chờ dữ liệu render xong
    });
</script>
    </body>
    </html>
    """

    return render_template_string(PAGE_TEMPLATE,
        total_orders=total_orders,
        total_revenue=total_revenue_formatted,
        total_customers=total_customers,
        monthly_stats=monthly_stats,
        yearly_stats=yearly_stats,
        month=month,
        year=year,
        admin_id=admin_id,
        admins=admins,
        admin_name=admin_name,
        expense_by_month=expense_by_month,
        expense_by_year=expense_by_year,
        total_monthly_profit=total_monthly_profit,
        avg_monthly_percent=avg_monthly_percent,
        total_yearly_profit=total_yearly_profit,
        avg_yearly_percent=avg_yearly_percent,
    )
