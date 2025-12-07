from flask import Blueprint, render_template_string, request, redirect, url_for,session
from database import Database  

donhangAd_bp = Blueprint('donhangAd', __name__, url_prefix='/donhangAd')

# Cập nhật trạng thái đơn hàng
@donhangAd_bp.route('/update_status/<int:order_id>/<status>')
def update_status(order_id, status):
    admin_id = session.get('admin_id')

    db = Database()
    if admin_id and status == 'shipped':
        query = "UPDATE donhang SET status = %s, admin_id = %s WHERE id = %s"
        db.execute_query(query, (status, admin_id, order_id))
    else:
        query = "UPDATE donhang SET status = %s WHERE id = %s"
        db.execute_query(query, (status, order_id))
    db.close()
    return redirect(url_for('donhangAd.index', status=request.args.get('status', 'pending')))
# Xóa đơn hàng
@donhangAd_bp.route('/delete/<int:order_id>')
def delete_order(order_id):
    db = Database()
    query = "DELETE FROM donhang WHERE id = %s"
    db.execute_query(query, (order_id,))
    db.close()
    return redirect(url_for('donhangAd.index', status=request.args.get('status', 'pending')))

@donhangAd_bp.route('/')
def index():
    status_filter = request.args.get('status', 'pending')  
    db = Database()  
    if status_filter == 'all':
        query = "SELECT * FROM donhang"
        donhangs = db.fetch_data(query)
    elif status_filter == 'completed':
        query = "SELECT * FROM donhang WHERE status = %s ORDER BY user_id DESC"
        donhangs = db.fetch_data(query, (status_filter,))
    else:
        query = "SELECT * FROM donhang WHERE status = %s"
        donhangs = db.fetch_data(query, (status_filter,))
    db.close()  

    PAGE_TEMPLATE = """
    <!DOCTYPE html>
    <html lang=\"vi\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>Quản lý Đơn Hàng</title>
        <style>
            body { font-family: Arial, sans-serif; background: linear-gradient(to right, #f7b42c, #fc575e); padding: 20px; }
            .filter-buttons { margin-bottom: 15px; text-align: center; }
            .back-btn-container { display: flex; justify-content: space-between; align-items: center; }
.back-btn { text-decoration: none; padding: 6px 15px; background-color: #f5db3b; color: white; border-radius: 5px; }
.back-btn:hover { background-color: #f1d15f; }
.filter-btn { padding: 10px 15px; margin: 5px; border-radius: 5px; border: none; cursor: pointer; color: white; font-weight: bold; text-decoration: none; display: inline-block; background-color: #007baa; }
.filter-btn.active { background-color: #0056b3; }
.pending-btn { background-color: orange; }
.shipped-btn { background-color: blue; }
.completed-btn { background-color: green; }
.all-btn { background-color: gray; }
table { width: 100%; border-collapse: collapse; background-color: rgba(255, 255, 255, 0.6); border-radius: 8px; overflow: hidden; }
th, td { padding: 12px; text-align: center; border: 1px solid #ddd; }
.action-btn { padding: 5px 10px; color: white; border-radius: 4px; text-decoration: none; margin: 0 5px; display: inline-block; }
.ship-btn { background-color: blue; }
.complete-btn { background-color: green; }
.delete-btn { background-color: red; }
.h1-box { display: inline-block; padding: 10px 20px; border: 3px solid #ff5e62; border-radius: 8px;
 background: rgba(255, 255, 255, 0.8); box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2); color: #333; font-size: 28px; font-weight: bold; text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.3); }

        </style>
    </head>
    <body>
    <div class="back-btn-container">
        <h1 class="h1-box">📦 Danh Sách Đơn Hàng</h1>
        <a href="/muaAd" class="back-btn"><b>⬅ Quay lại</b></a> 
    </div>      
<div class="filter-buttons">   
    <a href="?status=pending" class="filter-btn {% if status == 'pending' %}active pending-btn{% endif %}">Chờ xử lý</a>
    <a href="?status=shipped" class="filter-btn {% if status == 'shipped' %}active shipped-btn{% endif %}">Đang giao</a> 
    <a href="?status=completed" class="filter-btn {% if status == 'completed' %}active completed-btn{% endif %}">Hoàn thành</a>
    <!-- <a href="?status=all" class="filter-btn {% if status == 'all' %}active all-btn{% endif %}">Tất cả</a> -->
</div>

        <table>
            <thead>
                <tr>
                    <th>Mã</th>
                    <th>ID Người Dùng</th>
                    <th>Tổng Tiền</th>
                    <th>Trạng Thái</th>
                    <th>Địa Chỉ</th>
                    <th>Ngày Tạo</th>
                    <th>Ngày Cập Nhật</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {% for donhang in donhangs %}
                    <tr>
                        <td>{{ donhang.id }}</td>
                        <td>{{ donhang.user_id }}</td>
                        <td>{{ "{:,.0f}".format(donhang.total_price) }} VNĐ</td>
                        <td>
                            {% if donhang.status == 'pending' %}
                                <span style=\"color: orange;\">Chờ xử lý</span>
                                {% elif donhang.status == 'shipped' %}
                                    <span style=\"color: blue;\">Giao hàng</span>                            
                            {% elif donhang.status == 'completed' %}
                                <span style=\"color: green;\">Hoàn thành</span>
                            {% endif %}
                        </td>
                        <td>{{ donhang.address }}</td>
                        <td>{{ donhang.created_at }}</td>
                        <td>{{ donhang.updated_at }}</td>
                        <td>
                            {% if donhang.status == 'pending' %}
                                <a href="/donhangAd/update_status/{{ donhang.id }}/shipped" class="action-btn ship-btn" style="font-size:12px;background-color: green;">Xác nhận đơn hàng</a>
                            {% elif donhang.status == 'shipped' %}
                                <span style="color: green; font-weight: bold;"><i>Đang giao</i></span>
                            {% elif donhang.status == 'completed' %}
                                <a href="/donhangAd/delete/{{ donhang.id }}" class="action-btn delete-btn" onclick="return confirm('Bạn có chắc chắn muốn xóa đơn hàng này không?');">Xóa</a>
                            {% endif %}
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    """
    return render_template_string(PAGE_TEMPLATE, donhangs=donhangs)
