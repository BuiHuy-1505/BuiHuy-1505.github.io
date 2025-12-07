from flask import Blueprint, session, request, redirect, url_for, render_template_string,make_response
from database import Database

giohang_bp = Blueprint('giohang', __name__)
db = Database()

@giohang_bp.route('/them/<int:product_id>/<int:quantity>')
def them_vao_gio(product_id, quantity):
    if 'user_id' not in session:
        return redirect(url_for('dangnhap'))

    user_id = session['user_id']
    product = db.fetch_one("SELECT id, name, price FROM sanpham WHERE id = %s", (product_id,))
    if not product:
        print(f"❌ Không tìm thấy sản phẩm với ID {product_id}")
        return redirect(url_for('giohang.xem_gio'))

    existing = db.fetch_one("SELECT quantity FROM giohang WHERE user_id = %s AND product_id = %s", (user_id, product_id))

    if existing:
        new_quantity = existing['quantity'] + quantity
        db.execute_query("UPDATE giohang SET quantity = %s WHERE user_id = %s AND product_id = %s", (new_quantity, user_id, product_id))
    else:
        db.execute_query("INSERT INTO giohang (user_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)", 
                   (user_id, product_id, quantity, product['price']))

    return redirect(url_for('giohang.xem_gio'))

@giohang_bp.route('/chuan_bi_thanhtoan', methods=['POST'])
def chuan_bi_thanhtoan():
    if 'user_id' not in session:
        return redirect(url_for('dangnhap'))
    selected_ids = request.form.getlist('selected_products')
    if not selected_ids:
        print("⚠️ Không có sản phẩm nào được chọn để thanh toán.")
        return redirect(url_for('giohang.xem_gio'))

    session['cart_items'] = list(map(int, selected_ids))
    print("✅ Đã lưu vào session['cart_items']:", session['cart_items'])
    return redirect(url_for('thanhtoan.thanhtoan'))

@giohang_bp.route('/giohang', methods=['GET'])
def xem_gio():
    if 'user_id' not in session:
        return redirect(url_for('dangnhap'))  

    user_id = session['user_id']

    query = """
        SELECT g.product_id, s.name, s.price, s.url_img, g.quantity
        FROM giohang g
        JOIN sanpham s ON g.product_id = s.id
        WHERE g.user_id = %s
    """
    cart_items = db.fetch_data(query, (user_id,))

    cart = {str(item['product_id']): item for item in cart_items}
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    response = make_response(render_template_string(GIOHANG_TEMPLATE, cart=cart, total_price=total_price))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return render_template_string(GIOHANG_TEMPLATE, cart=cart, total_price=total_price)

GIOHANG_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset=\"UTF-8\">
    <title>Giỏ hàng</title>
    <style>
        body {  background-image: url('https://taoanhdep.com/wp-content/uploads/2022/08/hinh-nen-may-cuc-dep.jpeg'); 
        background-size: cover;background-attachment: fixed;font-family: Arial, sans-serif; text-align: center;}
        table { width: 80%; margin: 20px auto; border-collapse: collapse; background-color: rgba(255, 255, 255, 0.8);border-radius: 8px; overflow: hidden; }
        th, td { padding: 10px; border: 1px solid #ddd; }
        img { width: 50px; border-radius: 5px; }
        .btn { padding: 5px 10px; cursor: pointer; border: none; border-radius: 3px; }
        .btn-update { background: #ffa500; color: white; }
        .btn-delete { background: #ff4444; color: white; }
        .product-checkbox {transform: scale(1.5); }
    </style>
</head>
<body>
<form method="POST" action="{{ url_for('giohang.chuan_bi_thanhtoan') }}">
    <div style="text-align: center;">
        <h2 style="border: 2px solid #ff6600; padding: 10px 80px; display: inline-block; border-radius: 10px; background: #fff4e6;">
            🛒 Giỏ hàng của bạn
        </h2>
    </div>
    
    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
        <a href="/mua" class="btn btn-back" style="font-size: 13px; background: #ddd; padding: 8px 12px; border-radius: 5px; text-decoration: none;">
            <b>⏪<i> Chọn thêm sản phẩm</i></b>
        </a>
        <button type="submit" class="btn" style="background: #ff6600; color: white; padding: 8px 12px; border-radius: 5px;">
            💳 Thanh toán
        </button>
    </div>

    {% if not cart %}
        <p>Giỏ hàng trống.</p>
    {% else %}
        <table>
            <tr>
                <th>Chọn</th>
                <th width="20%">Hình ảnh</th>
                <th>Tên sản phẩm</th>
                <th>Giá</th>
                <th width="10%">Số lượng</th>
                <th>Thành tiền</th>
                <th></th>
            </tr>
            {% for sp in cart.values() %}
            <tr style="height: 100px;">
                <td>
                    <input type="checkbox" name="selected_products" value="{{ sp['product_id'] }}" class="product-checkbox" onchange="updateTotal()">
                </td>
                <td><img src="{{ sp['url_img'] }}" alt="{{ sp['name'] }}" style="width: 100px;"></td>
                <td>{{ sp['name'] }}</td>
                <td>{{ "{:,.0f}".format(sp['price']) }} VNĐ</td>
                <td>{{ sp['quantity'] }}</td>
                <td class="subtotal">{{ "{:,.0f}".format(sp['price'] * sp['quantity']) }}</td>
                <td>
                    <a href="{{ url_for('giohang.xoa_sanpham', product_id=sp['product_id']) }}" class="btn btn-delete">❌ Xóa</a>
                </td>
            </tr>
            {% endfor %}
        </table>
    {% endif %}

    <h3>Tổng tiền: <span id="total-price">0</span> VNĐ</h3>
</form>

<script>
    function updateTotal() {
        let total = 0;
        document.querySelectorAll(".product-checkbox").forEach((checkbox, index) => {
            if (checkbox.checked) {
                let price = parseInt(document.querySelectorAll(".subtotal")[index].innerText.replace(/,/g, ""));
                total += price;
            }
        });
        document.getElementById("total-price").innerText = total.toLocaleString();
    }
</script>
</body>

</html>
"""

@giohang_bp.route('/capnhat_gio', methods=['POST'])
def capnhat_gio():
    if 'user_id' not in session:
        return redirect(url_for('dangnhap'))
    user_id = session['user_id']
    for key, value in request.form.items():
        if key.startswith("quantity_"):
            try:
                product_id = int(key.split("_")[1])
                new_quantity = int(value)
                if new_quantity > 0:
                    existing = db.fetch_one(
                        "SELECT * FROM giohang WHERE user_id = %s AND product_id = %s",
                        (user_id, product_id)
                    )
                    if existing:
                        db.execute_query(
                            "UPDATE giohang SET quantity = %s WHERE user_id = %s AND product_id = %s",
                            (new_quantity, user_id, product_id)
                        )
                else:
                    print(f"⚠️ Không cập nhật do số lượng không hợp lệ: {new_quantity}")
            except ValueError:
                print("❌ Lỗi: Giá trị số lượng không hợp lệ")
                continue
    return redirect(url_for('giohang.xem_gio'))

@giohang_bp.route('/xoa/<int:product_id>')
def xoa_sanpham(product_id):
    if 'user_id' not in session:
        return redirect(url_for('dangnhap'))
    user_id = session['user_id']
    db.execute_query("DELETE FROM giohang WHERE user_id = %s AND product_id = %s", (user_id, product_id))
    return redirect(url_for('giohang.xem_gio'))
