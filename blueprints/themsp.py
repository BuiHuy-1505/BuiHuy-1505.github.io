from flask import Blueprint, request, render_template, redirect, url_for, session, render_template_string
from database import Database  

themsp_bp = Blueprint('themsp', __name__)
db = Database()
@themsp_bp.route('/themsp/<int:product_id>', methods=['GET', 'POST'])
def themsp(product_id):
    product = db.fetch_one("SELECT * FROM sanpham WHERE id = %s", (product_id,))

    if not product:
        return "Sản phẩm không tồn tại", 404

    if request.method == "POST":
        try:
            quantity = int(request.form.get("quantity", 1))
            if quantity < 1:
                raise ValueError
        except ValueError:
            return "Số lượng không hợp lệ", 400
        return redirect(url_for("giohang.them_vao_gio", product_id=product_id, quantity=quantity))

    return render_template_string(PAGE_TEMPLATE, product=product)

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thêm Sản Phẩm</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <style>
        body { background-image: url('https://png.pngtree.com/png-vector/20220615/ourmid/pngtree-hand-drawn-confectionery-background-bakery-homemade-png-image_5092287.png'); 
         background-size: cover; background-position: center; background-repeat: no-repeat; }
        .product-container { display: flex; flex-direction: column; align-items: center; max-width: 1100px;height: 450px; 
            margin: auto; padding: 20px; background: #FFF9C4; border-radius: 10px;box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        .product-img img { width: 300px; border-radius: 8px;max-height: 310px;object-fit: contain; }
        .product-title { font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 15px; }
        .product-content { display: flex; align-items: center; gap: 20px; width: 100%; }
        .product-info { flex: 1; }
        .product-price { font-size: 20px; color: #ff6600; font-weight: bold; margin-bottom: 10px; }
        .product-desc { color: #555; text-align: justify; margin-bottom: 10px; }
        .quantity-input { width: 60px; text-align: center; margin-left: 10px; }
        .total-price { font-weight: bold; font-size: 18px; color: #ff6600; }
        .btn-container { display: flex; gap: 10px; margin-top: 15px; justify-content: center; }
        .btn-back { background: #ddd; color: #000; padding: 10px 15px; border-radius: 5px; text-decoration: none; }
        .btn-primary { background-color: #ff6600; border: none; padding: 10px 15px; border-radius: 5px; color: white; }
    </style>
</head>
<body>
    <div class="container mt-4">
        <h2 class="text-center text-primary" style="margin-bottom:20px;"><b>Thêm sản phẩm vào giỏ hàng</b></h2>

        <div class="product-container">
            <!-- Tên sản phẩm -->
            <h2 class="product-title">{{ product['name'] }}</h2>

            <!-- Ảnh + Thông tin sản phẩm -->
            <div class="product-content">
                <div class="product-img">
                    <img src="{{ product['url_img'] }}" alt="{{ product['name'] }}">
                </div>
                <div class="product-info">
                    <div class="product-price">{{ "{:,.0f}".format(product['price']) }} VNĐ</div>
                    <p class="product-desc">{{ product['description'] }}</p>
                    <form method="POST">
                        <label>Số lượng:</label>
                        <input type="number" name="quantity" id="quantity" class="quantity-input" value="1" min="1" oninput="updateTotal()">
                        <p class="total-price">Tổng tiền: <span id="total">{{ "{:,.0f}".format(product['price']) }}</span> VNĐ</p>
                        <button type="submit" class="btn btn-primary">🛒 Thêm vào giỏ hàng</button>
                    </form>
                </div>
            </div>
            <div class="btn-container">
                <a href="/mua" class="btn btn-back">⏪ Quay lại</a>
            </div>
        </div>
    </div>
   <script>
    function updateTotal() {
        let price = {{ product['price'] }};
        let quantity = document.getElementById("quantity").value;
        let total = price * quantity;
        document.getElementById("total").innerText = total.toLocaleString() ;
    }
</script> 
</body>
</html>
"""
