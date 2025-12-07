from flask import Blueprint, request, render_template_string
from database import Database  

mua_bp = Blueprint('mua', __name__)
db = Database()  

@mua_bp.route("/mua", methods=["GET", "POST"])
def trang_mua():
    search = request.form.get("search", "").strip()
    scroll = request.form.get("scroll", "false")  # Lấy giá trị cuộn
    category_id = request.args.get("category_id")
    query = "SELECT * FROM sanpham"
    params = []
    if category_id:  # Nếu có category_id, lọc sản phẩm theo danh mục
        query += " WHERE category_id = %s"
        params.append(category_id)
    if search:
        query += " WHERE name LIKE %s"
        params.append(f"%{search}%")

    query += " ORDER BY id DESC"
    products = db.fetch_data(query, tuple(params))

    return render_template_string(PAGE_TEMPLATE, products=products, search_query=search, scroll=scroll)
PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🛒 Mua Hàng</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f5f5f5; }
        .header-container { width: 100%; position: relative; }
        .slideshow-container { width: 100%; height: 250px; overflow: hidden; position: relative; }
        .slide { display: none; width: 100%; height: 100%; object-fit: cover; }

        /* Menu bên trái */
        .container { display: flex; }
        .menu { width: 180px;background-color: #122; color: white; padding: 15px; height: 100vh; position: fixed; top: 0; left: 0; }
        .menu h3 { text-align: center; }
        .menu ul { list-style: none; padding: 0; }
        .menu ul li { padding: 10px; border-bottom: 1px solid #555; text-align: center; }
        .menu ul li a { text-decoration: none; color: white; display: block; }
        .menu ul li:hover { background: #444; }
        .main-content { flex: 1; padding: 20px; margin-left: 220px; } /* Dịch sang phải để không che menu */
        .product-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 20px; }
        .product-card { background: white; padding: 10px; border-radius: 10px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.2); }
        .product-card img { width: 100%; height: 150px; object-fit: cover; border-radius: 5px; }
        .product-card h4 { margin: 10px 0; font-size: 16px; }
        .product-card p { font-weight: bold; color: #e44d26; }
        .buy-btn { display: block; background: #ff9800; color: white; padding: 8px; border-radius: 5px; text-decoration: none; margin-top: 10px; }
.product-header { text-align: center; background: #fffae6; border-radius: 10px; margin-bottom: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); }  
.product-header h2 { color: #ff6600; font-size: 24px; margin-bottom: 5px; }  
.product-header p { color: #333; font-size: 16px; }
.product-header { height: 80px; padding: 12px 0;margin-top: 4px; padding-top: 1px; }
.search-container {display: flex;justify-content: flex-end;width: 100%; }
#searchBox {width: 350px;  height: 5px; font-size: 11px; padding: 10px;  }
#resetSearch {background-color: #666;font-size: 16px;padding: 4px 4px; border-radius: 8px; }
.header-container { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; }
.cart-icon { font-size: 20px; text-decoration: none; padding: 8px 12px; border-radius: 5px; transition: 0.3s;background:#eea366; }
.cart-icon:hover { background: #f39c12; color: white; }
.logout-container { display: flex;position: absolute; bottom: 35px; left: 50%; transform: translateX(-50%); width: auto; } 
.logout-container { display: flex; position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%); }  
.logout-btn { display: flex; align-items: center; gap: 5px; justify-content: center; padding: 10px 20px; font-size: 14px; background: #ff4444; color: white; text-decoration: none; border-radius: 5px; }  
.logout-btn:hover { background: #cc0000; }  
.logout-btn img { width: 16px; height: 16px; }  

.popup { display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: #ddd; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); text-align: center; z-index: 1001; width: 300px; }
.popup button { margin: 10px; padding: 8px 15px; border: none; border-radius: 5px; cursor: pointer; }
.popup .confirm { background: #ff4444; color: white; }
.popup .cancel { background: #ddd; color: black; }
.overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5); z-index: 1000; }

    </style>
</head>
<body>
    <div class="header-container">
        <div class="slideshow-container">
            <img class="slide" src="https://cdn.shopify.com/s/files/1/0563/5745/4002/products/93694e51b818d85eeb356a39e521f36f.jpg?v=1623387479" alt="Slide 1">
            <img class="slide" src="https://afamilycdn.com/2019/12/9/dscf1949-1575867079277701935739.jpg" alt="Slide 2">
            <img class="slide" src="https://pos.nvncdn.com/4e732c-26/art/artCT/20230717_f7vvsIx6.jpg" alt="Slide 3">
        </div>
    </div>

    <div class="container">
        <!-- Menu bên trái -->
        <div class="menu">
            <h3 style="color: #80dfff; font-size: 25px;">Menu</h3>
            <ul>
                <li><a href="/mua#sanpham">Tất cả sản phẩm</a></li>
                <li><a href="/mua?category_id=1#sanpham">Chocolate</a></li>
                <li><a href="/mua?category_id=2#sanpham">Kẹo dẻo</a></li>
                <li><a href="/mua?category_id=3#sanpham">Bánh quy</a></li>
            </ul>
            <a href="/giohang" style="color: #80dfff; font-size: 17px; font-weight: bold; text-decoration: none; display: block; margin-top: 40px;">
                + Giỏ hàng của bạn
            </a>
            <a href="/donhang" style="color: #80dfff; font-size: 17px; font-weight: bold; text-decoration: none; display: block; margin-top: 8px;">
                + Đơn hàng của bạn
            </a>
            <a href="/doimk" style="color: #80dfff; font-size: 17px; font-weight: bold; text-decoration: none; display: block; margin-top: 8px;">
                + Thay đổi mật khẩu
            </a>
                <div class="logout-container">
                    <a href="#" class="logout-btn" onclick="showPopup()">
                        Đăng xuất
                    </a>
                    </div>

                    <div class="overlay" id="overlay"></div>
                    <div class="popup" id="logoutPopup">
                        <p style="color: black;">Bạn có chắc chắn muốn đăng xuất?</p>
                        <button class="confirm" onclick="logout()">OK</button>
                        <button class="cancel" onclick="closePopup()" style="background: #aaa;">Hủy</button>
                    </div>
            </div>
        <!-- Phần hiển thị sản phẩm -->      
        <div class="main-content">
         <div class="product-header">
            <h2 id="sanpham">🛍️ Chào mừng đến với cửa hàng   </h2>
            <p><i>Sản phẩm chính hãng, giá tốt – Chọn ngay món hàng yêu thích!</i></p>
        </div>
            <div class="header-container">
                <h2>😋 Sản Phẩm của chúng tôi</h2>
                <a href="/giohang" class="cart-icon" style="color: #fee;"><b>Giỏ hàng</b> 🛒</a>
            </div>
<form method="POST" action="/mua" id="searchForm" class="search-container">
    <input type="hidden" name="scroll" value="true">
    
    <div class="d-flex">
        <!-- Nút reset -->
        <button type="button" class="btn btn-secondary" id="resetSearch">
            <span class="reset-icon">🔄</span>
        </button>
        <input type="text" name="search" id="searchBox" class="form-control me-2" 
            placeholder="Tìm kiếm sản phẩm" value="{{ search_query }}">
        <button type="submit" class="btn btn-primary me-2">🔍</button>      
    </div>
</form>       
            <div class="product-grid">
                {% for product in products %}
                    <div class="product-card">
                        <img src="{{ product['url_img'] }}" alt="{{ product['name'] }}">
                        <h4>{{ product['name'] }}</h4>
                        <p>{{ "{:,.0f}".format(product['price']) }} VNĐ</p>
                        <a href="{{ url_for('themsp.themsp', product_id=product['id']) }}" class="buy-btn">Thêm vào giỏ hàng</a>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>
    <script>
        let index = 0;
        function showSlides() {
            let slides = document.getElementsByClassName("slide");
            for (let i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            index++;
            if (index > slides.length) { index = 1; }
            slides[index - 1].style.display = "block";
            setTimeout(showSlides, 3000);
        }
        showSlides();
    </script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        let shouldScroll = "{{ scroll }}" === "true";
        if (shouldScroll) {
            let target = document.getElementById("sanpham");
            if (target) {
                target.scrollIntoView({ behavior: "smooth" });
            }
        }

        // Xử lý nút reset
        document.getElementById("resetSearch").addEventListener("click", function() {
            document.getElementById("searchBox").value = "";  
            document.forms["searchForm"].submit();  
        });
    });
</script>
<script>
function showPopup() {
    document.getElementById("logoutPopup").style.display = "block";
    document.getElementById("overlay").style.display = "block";
}

function closePopup() {
    document.getElementById("logoutPopup").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}

function logout() {
    window.location.href = "/"; 
}
</script>
</body>
</html>
"""
