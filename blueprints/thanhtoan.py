from flask import Blueprint, session, render_template_string, redirect, url_for,request
from database import Database
import datetime
import hmac
import hashlib
import urllib.parse
import uuid

thanhtoan_bp = Blueprint('thanhtoan', __name__)
db = Database()

@thanhtoan_bp.route('/vnpay_payment/<int:order_id>')
def vnpay_payment(order_id):
    vnp_TmnCode = 'H9TA3YJ0'
    vnp_HashSecret = 'J3GV7PTLKDZN6CAKG8X3HUGCJV3E2SET'
    vnp_Url = 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html'
    vnp_Returnurl = 'http://localhost:5000/vnpay_return'

    order = db.fetch_one("SELECT total_price FROM donhang WHERE id = %s", (order_id,))
    if not order:
        return "Đơn hàng không tồn tại"

    amount = int(order['total_price']) * 100  # VNPAY yêu cầu nhân 100

    vnp_Params = {
        'vnp_Version': '2.1.0',
        'vnp_Command': 'pay',
        'vnp_TmnCode': vnp_TmnCode,
        'vnp_Amount': str(amount),
        'vnp_CurrCode': 'VND',
        'vnp_TxnRef': str(uuid.uuid4().hex[:8]),  
        'vnp_OrderInfo': f'Thanh toan don hang {order_id}',
        'vnp_OrderType': 'other',
        'vnp_Locale': 'vn',
        'vnp_ReturnUrl': vnp_Returnurl,
        'vnp_IpAddr': request.remote_addr,
        'vnp_CreateDate': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
    }

    sorted_params = sorted(vnp_Params.items())
    query_string = '&'.join([f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in sorted_params])

    hashdata = query_string 
    print("===> Hash Data (Encoded):", hashdata) 

    secure_hash = hmac.new(vnp_HashSecret.encode('utf-8'), hashdata.encode('utf-8'), hashlib.sha512).hexdigest()
    vnp_Url = f"https://sandbox.vnpayment.vn/paymentv2/vpcpay.html?{query_string}&vnp_SecureHash={urllib.parse.quote_plus(secure_hash)}"

    print("===> Final URL:", vnp_Url)
    print("===> Final URL:", vnp_Url)
    print("===> Chuỗi hash_data dùng để đối chiếu:", hashdata)
    print("===> Hash VNPAY gửi:", secure_hash)
    print("Redirect URL:", vnp_Url)

    return redirect(vnp_Url)
@thanhtoan_bp.route('/vnpay_return')
def vnpay_return():
    inputData = request.args.to_dict()
    vnp_HashSecret = 'J3GV7PTLKDZN6CAKG8X3HUGCJV3E2SET'

    vnp_SecureHash = inputData.pop('vnp_SecureHash', None)

    sorted_data = sorted(inputData.items())
    hash_data = '&'.join([f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in sorted_data])

    verify_hash = hmac.new(vnp_HashSecret.encode(), hash_data.encode(), hashlib.sha512).hexdigest()

    if vnp_SecureHash != verify_hash:
        return "⚠️ Sai checksum!"

    user_id = session.get('user_id')
    
    if not user_id:
        return redirect(url_for('dangnhap'))

    order_info = inputData.get('vnp_OrderInfo', '')
    order_id = order_info.split(':')[-1]

    return redirect(url_for('donhang.xem_donhang'))


@thanhtoan_bp.route('/thanhtoan')
def thanhtoan():
    if 'user_id' not in session:
        return redirect(url_for('dangnhap'))

    user_id = session['user_id']
    selected_products = session.get("cart_items", [])
    print("✅ Sản phẩm được chọn trong giỏ hàng:", selected_products)

    if not selected_products:
        return render_template_string(THANHTOAN_TEMPLATE, cart={}, total_price=0)

    placeholders = ', '.join(['%s'] * len(selected_products))
    query = f"""
        SELECT g.product_id, s.name, s.price, s.url_img, g.quantity
        FROM giohang g
        JOIN sanpham s ON g.product_id = s.id
        WHERE g.user_id = %s AND g.product_id IN ({placeholders})
    """
    cart_items = db.fetch_data(query, [user_id] + selected_products)

    cart = {str(item['product_id']): item for item in cart_items}
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())

    return render_template_string(THANHTOAN_TEMPLATE, cart=cart, total_price=total_price)

@thanhtoan_bp.route('/xacnhan_thanhtoan', methods=['POST'])
def xacnhan_thanhtoan():
    if 'user_id' not in session:
        return redirect(url_for('dangnhap'))

    user_id = session['user_id']
    selected_products = session.get("cart_items", [])
    address = request.form.get("address")  # Lấy địa chỉ từ form

    if not selected_products or not address:
        return redirect(url_for('thanhtoan'))

    # Lấy sản phẩm trong giỏ hàng
    placeholders = ', '.join(['%s'] * len(selected_products))
    query = f"""
        SELECT g.product_id, s.price, g.quantity
        FROM giohang g
        JOIN sanpham s ON g.product_id = s.id
        WHERE g.user_id = %s AND g.product_id IN ({placeholders})
    """
    cart_items = db.fetch_data(query, [user_id] + selected_products)
    print(f"Cart items: {cart_items}")
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)

    # ✅ Thêm đơn hàng vào bảng `donhang`
    order_query = """
    INSERT INTO donhang (user_id, total_price, status, address, created_at)
    VALUES (%s, %s, %s, %s, %s)
    """
    order_id = db.insert_and_get_id(order_query, (user_id, total_price, "pending", address, datetime.datetime.now()))

    # ✅ Thêm chi tiết đơn hàng vào `chitietdonhang`
    detail_query = "INSERT INTO chitietdonhang (order_id, product_id, quantity) VALUES (%s, %s, %s)"
    for item in cart_items:
        db.execute_query(detail_query, (order_id, item['product_id'], item['quantity']))

    # Xóa sản phẩm khỏi giỏ hàng trong cơ sở dữ liệu
    delete_query = f"DELETE FROM giohang WHERE user_id = %s AND product_id IN ({placeholders})"
    db.execute_query(delete_query, [user_id] + selected_products)
    session['cart_items'] = [item for item in session.get('cart_items', []) if item not in selected_products]
    session.pop("cart_items", None)

    return redirect(url_for('thanhtoan.vnpay_payment', order_id=order_id))
    
THANHTOAN_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Thanh toán</title>
    <style>
        body { background: linear-gradient(to right, #ff9966, #ff5e62); font-family: Arial, sans-serif; text-align: center; }
        table { width: 80%; margin: 20px auto; border-collapse: collapse; background: white; }
        th, td { padding: 10px; border: 1px solid #ddd; }
        img { width: 50px; border-radius: 5px; }
        .btn { padding: 8px 12px; cursor: pointer; border: none; border-radius: 5px; }
        .btn-back { background: #ddd; text-decoration: none;margin-top:10px; }
        table { background-color: rgba(255, 255, 255, 0.7);border-collapse: collapse; border-radius: 8px; overflow: hidden;}
        img { width: auto; border-radius: 10px;max-height: 90px; }
        h2 {font-size: 30px;font-weight: bold;color: black;margin-top: 10px;background: #d3d3d3;
        padding: 10px 20px;border-radius: 7px;display: inline-block;text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);}
    </style>
</head>
<body>
    <h2>💳 Thanh toán VNPAY</h2>
    {% if not cart %}
        <p>Không có sản phẩm nào để thanh toán.</p>
        <a href="/giohang" class="btn btn-back" style="display: inline-block; margin-top: 10px; background: #ddd; padding: 8px 12px; border-radius: 5px; text-decoration: none;">
        ⏪ Quay lại giỏ hàng
    </a>
    {% else %}
<table>
    <tr>
        <th style="width: 30%;">Hình ảnh</th>  <!-- Tăng kích thước cột hình ảnh -->
        <th>Tên sản phẩm</th>
        <th>Số lượng</th>  <!-- Giữ lại cột số lượng -->
        <th>Thành tiền</th>
    </tr>
    {% for sp in cart.values() %}
    <tr>
        <td>
            <img src="{{ sp['url_img'] }}" alt="{{ sp['name'] }}" style="width: 150px; height: auto;"> <!-- Hình ảnh to hơn -->
        </td>
        <td>{{ sp['name'] }}</td>
        <td>{{ sp['quantity'] }}</td>  <!-- Hiển thị số lượng -->
        <td>{{ "{:,.0f}".format(sp['price'] * sp['quantity']) }} VNĐ</td>
    </tr>
    {% endfor %}
</table>
    <h3>Tổng tiền: {{ "{:,.0f}".format(total_price) }} VNĐ</h3>
<form method="POST" action="{{ url_for('thanhtoan.xacnhan_thanhtoan') }}">
    <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 15px;">
        <label for="address"><b>🏠 Địa chỉ giao hàng:</b></label>
        <input type="text" id="address" name="address" placeholder="Nhập địa chỉ cụ thể"
               required style="width: 500px; padding: 6px; border-radius: 5px; border: 1px solid #ddd;">
    </div>

    <button type="submit" class="btn btn-confirm"
            style="background: #00bcd4; color: white; padding: 10px 20px; font-size: 18px; border-radius: 8px;">
        ✅ Xác nhận thanh toán
    </button>
</form>

  
    <a href="/giohang" class="btn btn-back" style="margin-top: 20px; display: inline-block;">⏪ Hủy </a>
    {% endif %}
<script>
function checkAddress() {
    let address = document.getElementById("address").value.trim();
    if (address === "") {
        return false;  // Không cho phép gửi form
    }
    return true;  // Cho phép gửi form nếu địa chỉ hợp lệ
}
</script>    
</body>
</html>
"""