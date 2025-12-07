from flask import Blueprint, render_template_string, request, session,redirect,url_for
from datetime import datetime
import calendar
from database import Database

nhaphangAd_bp = Blueprint('nhaphangAd', __name__, url_prefix='/nhaphangAd')

@nhaphangAd_bp.route('/', methods=['GET', 'POST'])
def nhaphangAd():
    db = Database()
    sanphams = db.fetch_data("SELECT id, name, import_price FROM sanpham")

    if 'phieu_nhap' not in session:
        session['phieu_nhap'] = []

    history_list = []
    today = datetime.today()
    current_month = today.strftime('%Y-%m')
    start_date = today.replace(day=1).strftime('%Y-%m-%d')
    last_day = calendar.monthrange(today.year, today.month)[1]
    end_date = today.replace(day=last_day).strftime('%Y-%m-%d')

    history_list = db.fetch_data(f"""
        SELECT nh.id, sp.name AS product_name, nh.quantity, nh.unit_import_price AS import_price, nh.created_at
        FROM nhaphang nh
        JOIN sanpham sp ON nh.product_id = sp.id
        WHERE nh.created_at BETWEEN '{start_date}' AND '{end_date}'
    """)

    if request.method == 'POST':
        if 'add_item' in request.form:
            product_id = request.form['product_id']
            quantity = int(request.form['quantity'])
            unit_import_price = float(request.form['unit_import_price'])
            product = db.fetch_data(f"SELECT name FROM sanpham WHERE id = {product_id}")[0]
            session['phieu_nhap'].append({
                'product_id': product_id,
                'product_name': product['name'],
                'quantity': quantity,
                'unit_price': unit_import_price
            })
            session.modified = True
        elif 'submit_all' in request.form:
            for item in session['phieu_nhap']:
                db.execute_query("""
                    INSERT INTO nhaphang (product_id, name, quantity, unit_import_price, admin_id)
                    VALUES (%s, %s, %s, %s, %s)
                """, (item['product_id'], item['product_name'], item['quantity'], item['unit_price'], 1))

                db.execute_query("UPDATE sanpham SET stock = stock + %s WHERE id = %s", (item['quantity'], item['product_id']))
            
            session['phieu_nhap'] = []
            session.modified = True  
            history_list = db.fetch_data(f"""
                SELECT nh.id, sp.name AS product_name, nh.quantity, nh.unit_import_price AS import_price, nh.created_at
                FROM nhaphang nh
                JOIN sanpham sp ON nh.product_id = sp.id
                WHERE nh.created_at BETWEEN '{start_date}' AND '{end_date}'
            """)

        elif 'filter_month' in request.form:
            month = request.form['month']
            try:
                datetime.strptime(month, '%Y-%m')
            except ValueError:
                return "Tháng không hợp lệ", 400
            start_date = f"{month}-01"
            last_day = calendar.monthrange(int(month[:4]), int(month[5:7]))[1]
            end_date = f"{month}-{last_day}"
            history_list = db.fetch_data(f"""
                SELECT nh.id, sp.name AS product_name, nh.quantity, nh.unit_import_price AS import_price, nh.created_at
                FROM nhaphang nh
                JOIN sanpham sp ON nh.product_id = sp.id
                WHERE nh.created_at BETWEEN '{start_date}' AND '{end_date}'
            """)

    html = """
<!DOCTYPE html>
<html lang=\"vi\">
<head>
    <meta charset=\"UTF-8\">
    <title>Phiếu Nhập Hàng</title>
<style>
    body { font-family: 'Arial', sans-serif; margin: 0; padding: 0; background-color: #98FB98; color: #333; }
    h1 { text-align: center; margin-top: 30px; font-size: 36px; color: #4CAF50; }
    h2, h3 { font-size: 24px; color: #333; margin-bottom: 20px; }
    .container { display: flex; justify-content: space-between; margin: 20px; padding: 20px; border-radius: 8px; background-color: #f5f5dc; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); }
    .left-column, .right-column { width: 48%; padding: 20px; background-color: #fafafa; border-radius: 8px; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1); }
    .right-column { padding-left: 40px; }
    label { font-size: 16px; font-weight: bold; margin-bottom: 8px; display: block; }
    input[type="text"], input[type="number"], select { width: 100%; padding: 10px; margin-bottom: 15px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; transition: border-color 0.3s; }
    input[type="text"]:focus, input[type="number"]:focus, select:focus { border-color: #4CAF50; }
    button { background-color: #4CAF50; color: white; padding: 12px 20px; font-size: 16px; border: none; border-radius: 8px; cursor: pointer; transition: background-color 0.3s ease; }
    button:hover { background-color: #45a049; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    table th, table td { padding: 12px; text-align: left; border: 1px solid #ddd; font-size: 16px; }
    table th { background-color: #f2f2f2; color: #333; }
    table tr:nth-child(even) { background-color: #f9f9f9; }
    table tr:hover { background-color: #f1f1f1; }
    .history-section {margin: 30px auto 0 auto; margin-top: 20px; padding: 20px; background-color: #e6f0fa; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1); border-radius: 8px;width:95%; }
    .history-section h4 { margin-top: 5px; font-size: 20px; color: #333; }
    .history-section table { margin-top: 10px; width: 100%; }
    .history-section table th, .history-section table td { text-align: center; }
    .history-section form { margin-bottom: 20px; }
    .search-bar { display: flex; justify-content: space-between; align-items: center; }
    .search-bar input { width: 70%; }
    .search-bar button { width: 25%; background-color: #2196F3; font-size: 16px; }
    @media (max-width: 768px) { .container { flex-direction: column; align-items: center; } .left-column, .right-column { width: 100%; margin-bottom: 20px; } .right-column { padding-left: 0; } h1 { font-size: 28px; } table th, table td { font-size: 14px; } }
.back-btn-container { display: flex; justify-content: space-between; align-items: center; }
.back-btn { text-decoration: none; padding: 6px 15px; background-color: #f5db3b; color: white; border-radius: 5px; }
.back-btn:hover { background-color: #f1d15f; }
.h1-box h1 {display: inline-block;border: 2px solid #4CAF50;padding: 10px 20px;background-color: #e8f5e9;border-radius: 5px;color: #1b5e20;}
.h1-box {text-align: center;}
     </style>

</head>
<body>
<div class="h1-box">
<h1>📥 Quản lý nhập hàng</h1>
</div>
<div class="back-btn-container">
        <a href="/muaAd" class="back-btn"><b>⬅ Quay lại</b></a> 
    </div>  
<div class=\"container\">
    <div class=\"left-column\">
    <h2>Thêm vào Phiếu Nhập</h2>
<form method=\"POST\">
    <label for=\"search\">Tìm kiếm sản phẩm:</label><br>
    <input type=\"text\" id=\"search\" placeholder=\"Tìm kiếm \" onkeyup=\"filterProducts()\" style="width:400px;"><br><br>
    <label>Sản phẩm:</label><br>
    <select name=\"product_id\" id=\"productSelect\" required>
        <option value=\"\" disabled selected>Chọn sản phẩm</option>
        {% for sp in sanphams %}
            <option value=\"{{ sp.id }}\" data-import-price=\"{{ sp.import_price }}\" >{{ sp.id }} - {{ sp.name }} - {{ sp.import_price }}đ</option>
        {% endfor %}
    </select><br><br>
    <label>Số lượng nhập:</label><br>
    <input type=\"number\" name=\"quantity\" id=\"quantity\" min=\"1\" required oninput=\"calculateUnitImportPrice()\" style="width:400px;"><br><br>
    <label>Giá nhập (đơn vị):</label><br>
    <input type="text" id="unit_import_price" disabled><br><br>
    <input type="hidden" name="unit_import_price" id="unit_import_price_hidden">

    <button type=\"submit\" name=\"add_item\">Thêm vào phiếu nhập</button>
</form>
    </div>
    <div class=\"right-column\">
        <h3>Danh sách trong phiếu nhập</h3>
        <form method=\"POST\">
            <table>
                <tr>
                    <th>ID SP</th><th>Tên SP</th><th>Số lượng</th><th>Giá nhập</th><th></th>
                </tr>
                {% for item in session['phieu_nhap'] %}
                <tr>
                    <td>{{ item.product_id }}</td>
                    <td>{{ item.product_name }}</td>
                    <td><input type=\"number\" name=\"quantity_{{ loop.index }}\" value=\"{{ item.quantity }}\" min=\"1\" required style="width:100px;"></td>
                    <td>{{ item.unit_price | int }}</td>
                    <td>
    <form method="POST" action="{{ url_for('nhaphangAd.remove_item', product_id=item.product_id) }}">
        <button type="submit" style="background-color: red; color: white; padding: 6px 12px;">Xóa</button>
    </form>
</td>


                </tr>
                {% endfor %}
            </table>
            {% if session['phieu_nhap'] %}
            <button type=\"submit\" name=\"submit_all\" style="margin-top:10px;">Xác nhận nhập hàng </button>
            {% endif %}
        </form>
    </div>
</div>
<div class=\"history-section\">
    <h2 style="text-align: center;font-size: 28px;">Lịch sử nhập hàng</h2>
    <form method=\"POST\">
        <label for=\"month\" style="font-size: 20px;">Xem theo tháng:</label><br>
        <input type=\"month\" name=\"month\" value=\"{{ current_month }}\" required><br><br>
        <button type="submit" name="filter_month" style="background-color: #ffcc80; color: white; padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer;margon-top: 0px;">
            Chọn
        </button>
    </form>
    <h4>Danh sách lịch sử nhập hàng</h4>
    <table>
        <tr>
            <th>ID</th><th>SP</th><th>Số lượng</th><th>Giá nhập</th><th>Ngày nhập</th>
        </tr>
        {% for history in history_list %}
        <tr>
            <td>{{ history.id }}</td>
            <td>{{ history.product_name }}</td>
            <td>{{ history.quantity }}</td>
            <td>{{ history.import_price }}đ</td>
            <td>{{ history.created_at }}</td>
        </tr>
        {% endfor %}
    </table>
</div>
<script>
function filterProducts() {
    var input = document.getElementById('search');
    var filter = input.value.toUpperCase();
    var options = document.getElementById('productSelect').getElementsByTagName('option');
    for (var i = 0; i < options.length; i++) {
        var txtValue = options[i].textContent || options[i].innerText;
        options[i].style.display = txtValue.toUpperCase().indexOf(filter) > -1 ? "" : "none";
    }
}
function formatCurrency(amount) {
    return amount.toLocaleString('vi-VN', { style: 'currency', currency: 'VND' });
}
function calculateUnitImportPrice() {
    var productSelect = document.getElementById('productSelect');
    var selectedOption = productSelect.options[productSelect.selectedIndex];
    var importPrice = parseFloat(selectedOption.getAttribute('data-import-price'));
    var quantity = document.getElementById('quantity').value;
    if (quantity && importPrice) {
        var unitImportPrice = importPrice * quantity;
        var formattedPrice = formatCurrency(unitImportPrice);
        document.getElementById('unit_import_price').value = formattedPrice; // Hiển thị giá nhập với định dạng
        document.getElementById('unit_import_price_hidden').value = unitImportPrice.toFixed(2); // Lưu giá trị chưa định dạng
    }
}
</script>
</body>
</html>
    """
    return render_template_string(html, sanphams=sanphams, history_list=history_list, current_month=current_month)
@nhaphangAd_bp.route('/remove_item/<int:product_id>', methods=['POST'])
def remove_item(product_id):
    session['phieu_nhap'] = [item for item in session['phieu_nhap'] if str(item['product_id']) != str(product_id)]  
    session.modified = True  
    return redirect(url_for('nhaphangAd.nhaphangAd'))  
