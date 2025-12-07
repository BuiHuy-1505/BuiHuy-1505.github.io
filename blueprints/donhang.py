from flask import Blueprint, session, render_template_string,request,redirect,url_for
from database import Database

donhang_bp = Blueprint('donhang', __name__)
db = Database()

@donhang_bp.route('/donhang', methods=['GET', 'POST'])
def xem_donhang():
    user_id = session.get('user_id')
    status_filter = request.args.get('status', 'pending')

    if status_filter:
        query = """
            SELECT id, total_price, status, address, created_at 
            FROM donhang 
            WHERE user_id = %s AND status = %s 
            ORDER BY created_at DESC
        """
        orders = db.fetch_data(query, (user_id, status_filter))
    else:
        query = """
            SELECT id, total_price, status, address, created_at 
            FROM donhang 
            WHERE user_id = %s 
            ORDER BY created_at DESC
        """
        orders = db.fetch_data(query, (user_id,))
    for order in orders:
        query_products = """
            SELECT sp.name, ctdh.quantity 
            FROM chitietdonhang ctdh
            JOIN sanpham sp ON ctdh.product_id = sp.id
            WHERE ctdh.order_id = %s
        """
        products = db.fetch_data(query_products, (order['id'],))
        order['products'] = [f"{p['name']} x ({p['quantity']})" for p in products]

        status_mapping = {
            "pending": "⏳ Chuẩn bị hàng",
            "shipped": "🚚 Đang giao hàng",
            "completed": "✅ Hoàn thành",
        }
        order['status'] = status_mapping.get(order['status'], order['status'])

    return render_template_string(DONHANG_TEMPLATE, orders=orders)
@donhang_bp.route('/nhan_hang/<int:order_id>', methods=['POST'])
def nhan_hang(order_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('dangnhap'))
    update_query = """
        UPDATE donhang SET status = 'completed' WHERE id = %s AND user_id = %s AND status = 'shipped'
    """
    db.execute_query(update_query, (order_id, user_id))

    return redirect(url_for('donhang.xem_donhang'))
DONHANG_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Đơn hàng của bạn</title>
    <style>
        body { background: linear-gradient(to right, #ff9966, #ff5e62); font-family: Arial, sans-serif; text-align: center; }
        th, td { padding: 10px; border: 1px solid #ddd; text-align: center; }
        th { background: #00bcd4; color: white; }
        .btn { padding: 8px 12px; text-decoration: none; border-radius: 5px; color: white; display: inline-block; }
        .btn-back { background: #ff5e62; margin-top: 0px; }
        table { width: 95%; margin: 20px auto; border-collapse: collapse; background-color: rgba(255, 255, 255, 0.75); border-radius: 8px; overflow: hidden; }
        .h1-box { display: block; padding: 10px 20px; border: 3px solid #ff5e62; border-radius: 8px; background: rgba(255, 255, 255, 0.8); width: 600px; margin: 20px auto;
          text-align: center; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2); color: #333; font-size: 25px; font-weight: bold; text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.3); }
        .user-id {position: absolute;top: 10px;left: 10px;font-size: 11px;color: #fff;background-color: rgba(0, 0, 0, 0.4);padding: 5px 10px;border-radius: 5px;}
    </style>
</head>
<body>
<div class="user-id">
        ID Khách Hàng: {{ session['user_id'] }}
    </div>
    <h1 class="h1-box">📦 Danh sách đơn hàng của bạn</h1>

    <a href="/mua" class="btn btn-back" style="font-size: 13px; background: #aaa; padding: 8px 12px; border-radius: 5px; text-decoration: none;">
        <b>⏪<i> Quay lại trang chủ</i></b>
    </a>

    <!-- Nút lọc trạng thái, luôn hiển thị -->
    <div style="margin: 20px; display: flex; justify-content: center; gap: 10px;">
        <form method="get" action="{{ url_for('donhang.xem_donhang') }}">
            <input type="hidden" name="status" value="pending">
            <button type="submit" class="btn" style="background: orange;">🕒 Đang xử lý</button>
        </form>
        <form method="get" action="{{ url_for('donhang.xem_donhang') }}">
            <input type="hidden" name="status" value="shipped">
            <button type="submit" class="btn" style="background: dodgerblue;">✅Xác nhận đơn hàng</button>
        </form>
        <form method="get" action="{{ url_for('donhang.xem_donhang') }}">
            <input type="hidden" name="status" value="completed">
            <button type="submit" class="btn" style="background: green;">📜 Lịch sử</button>
        </form>
    </div>
    {% if not orders %}
        <p>Không có đơn hàng nào.</p>
    {% else %}
<table>
    <tr>
        <th>Mã đơn</th>
        <th>Sản phẩm</th>
        <th>Tổng tiền</th>
        <th>Trạng thái</th>
        <th>Địa chỉ</th>
        <th>Ngày đặt</th>
    </tr>
    {% for order in orders %}
    <tr>
        <td>#{{ order.id }}</td>
        <td>
            <ul style="list-style: none; padding: 0;">
                {% for product in order.products %}
                    <li>{{ product }}</li>
                {% endfor %}
            </ul>
        </td>
        <td>{{ "{:,.0f}".format(order.total_price) }} VNĐ</td>
        <td>
            {{ order.status }}
            {% if order.status == "🚚 Đang giao hàng" %}
                <form method="POST" action="{{ url_for('donhang.nhan_hang', order_id=order.id) }}">
                    <button type="submit" class="btn" style="background: #4CAF50;margin-top:6px;">Đã nhận hàng thành công</button>
                </form>
            {% endif %}
        </td>
        <td>{{ order.address }}</td>
        <td>{{ order.created_at }}</td>
    </tr>
    {% endfor %}
</table>
    {% endif %}
</body>

</html>
"""
