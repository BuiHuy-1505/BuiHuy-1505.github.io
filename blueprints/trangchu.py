from flask import Blueprint
trangchu_bp = Blueprint('trangchu', __name__)

html_content = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Trang web bán hàng chuyên nghiệp với sản phẩm chất lượng và dịch vụ tận tâm.">
    <title>Trang chủ - Bánh Kẹo</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
            color: white;
            background: url('https://png.pngtree.com/thumb_back/fh260/back_our/20190620/ourmid/pngtree-milk-tea-poster-background-material-image_143415.jpg') no-repeat center center fixed;
            background-size: cover;
        }
        .container {padding: 30px;background: rgba(0, 0, 0, 0.6);display: inline-block;
            margin-top: 20px;border-radius: 10px;}
        .welcome-box { 
            background: rgba(0, 0, 0, 0.5); color: white; padding: 1px 70px; border-radius: 10px; 
            width: 60%; min-height: 80px; text-align: center; display: inline-block; margin-top: 10px; 
        }
        .slideshow {position: relative; width: 85vw; height: 50vh; margin: auto; overflow: hidden;
        border: 10px solid #fff; border-radius: 20px; box-shadow: 0 0 15px rgba(0,0,0,0.3);
        display: flex; justify-content: center; align-items: center;}
    .slide { width: 100%; height: 100%; object-fit: cover;position: absolute;top: 0px; left: 0;
    opacity: 0; transition: opacity 1s ease-in-out; z-index: 0;}
.slide.active { opacity: 1; z-index: 1; }
.prev, .next {position: absolute;top: calc(50% - 100px); transform: translateY(-50%);z-index: 2;
    background-color: rgba(0, 0, 0, 0.5);color: white;border: none;padding: 15px;font-size: 20px;cursor: pointer;border-radius: 50%;}
.prev { left: 3%; }
.next { right: 3%; }
.prev:hover, .next:hover { background-color: rgba(0, 0, 0, 0.8); }
.header { position: fixed; top: 0; left: 0; width: 100%; background: rgba(0, 0, 0, 0.8); color: white; padding: 8px 13px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3); z-index: 1000; }
    .logo { font-size: 24px; font-weight: bold; }
    .nav-buttons { display: flex; gap: 15px; }
    .nav-buttons button { background: #ff9800; border: none; color: white; padding: 10px 15px; font-size: 16px; cursor: pointer; border-radius: 5px; transition: 0.3s; }
    .nav-buttons button:hover { background: #e68900; }
    .nav-buttons button:last-child {
    margin-right: 20px; /* Nút cuối cùng có khoảng cách rộng hơn */}
body { padding-top: 60px; }
.top-products { background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px; text-align: center; margin: 30px auto; width: 80%; }
.top-products h2 { font-size: 24px; margin-bottom: 15px; color: #ff9800; }
.product-list { display: flex; justify-content: center; gap: 20px; }
.product { background: white; padding: 15px; border-radius: 10px; text-align: center; width: 30%; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); transition: 0.3s; }
.product img { width: 100%; height: auto; border-radius: 10px; }
.product h3 { font-size: 18px; margin: 10px 0; }
.product p { font-size: 16px; color: #444; }
.product button { background: #ff9800; color: white; border: none; padding: 8px 12px; cursor: pointer; border-radius: 5px; transition: 0.3s; }
.product button:hover { background: #e68900; }
.product:hover { transform: scale(1.05); box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3); }
.best-seller-intro { font-size: 18px; color: #333; text-align: center; margin-bottom: 20px; font-style: italic; }
.guarantee-section { width: 70%; height: 250px; display: flex; align-items: center; gap: 20px; padding: 10px; background: rgba(255, 255, 255, 0.8); border-radius: 10px; margin-top: 30px; }
.guarantee-section img { width: 220px; height: 200px; border-radius: 10px; }
.guarantee-text { text-align: left; max-width: 600px; color: #333; }
.quality-support { display: flex; justify-content: flex-end; margin-top: 20px; }
.support-box { width: 70%; height: 230px; background: rgba(255, 255, 255, 0.9); padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); }
.support-content { display: flex; align-items: center; justify-content: space-between; height: 100%; }
.text { width: 60%; color: black; }
.support-img { width: 35%; height: 180px; border-radius: 10px; object-fit: cover; }
.info-box {
    display: flex; align-items: center; width: 70%; height: 220px;
    background: rgba(255, 255, 255, 0.9); border-radius: 10px;
    padding: 15px; margin: 20px 0; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);}
.left-box { margin-left: 0; flex-direction: row; } /* Ảnh bên trái chữ */
.text-content { flex: 1; text-align: left; color: black; }
.info-image { width: 230px; height: 180px; margin-right: 20px; border-radius: 10px; }
    </style>
</head>
<body>
<div class="header">
        <div class="logo">Bánh Kẹo Shop</div>
        <div class="nav-buttons">
            <button onclick="window.location.href='/dangnhap'">Đăng nhập</button>
            <button onclick="window.location.href='/dangky'">Đăng ký</button>
        </div>
</div>        
<button class="prev" onclick="changeSlide(-1)">&#10094;</button>
<button class="next" onclick="changeSlide(1)">&#10095;</button>
    <div class="slideshow">
        <img class="slide active" src="https://vanchuyenmyviet.net/wp-content/uploads/2023/11/xu-huong-thi-truong-banh-keo-1.jpg" alt="Bánh kẹo 1">
        <img class="slide" src="https://giadinh.mediacdn.vn/2018/anh-1516075888081.jpg" alt="Bánh kẹo 2">
        <img class="slide" src="https://maydonggoianthanh.com/wp-content/uploads/2022/07/an-banh-keo-het-han-co-sao-khong-va-nhung-giai-dap-lien-quan-1.jpg" alt="Bánh kẹo 3">
        <img class="slide" src="https://cdn.tgdd.vn/Files/2020/10/16/1299375/banh-keo-meiji-gom-nhung-loai-nao-mua-loai-nao-thi-ngon-202010161102500052.jpg" alt="Bánh kẹo 4">
        <img class="slide" src="https://giadinh.mediacdn.vn/2018/anh-1516075888081.jpg" alt="Bánh kẹo 5">
        <img class="slide" src="https://vn-live-01.slatic.net/p/452d6c780b65e88377a7c7c757157f29.jpg" alt="Bánh kẹo 5">
        <img class="slide" src="https://thutucxuatnhapkhau.com/wp-content/uploads/2023/05/istockphoto-1149135424-612x612-1.jpg" alt="Bánh kẹo 5">
    </div>
    <script>
let slideIndex = 0;
function showSlide(index) {
    let slides = document.querySelectorAll(".slide");
    slides.forEach((slide, i) => {
        slide.style.opacity = (i === index) ? "1" : "0";
    });
    slideIndex = (index + slides.length) % slides.length;
}
function changeSlide(step) {
    slideIndex += step;
    showSlide(slideIndex);
}
setInterval(() => changeSlide(1), 5000); 
showSlide(slideIndex);
    </script>
    <div class="welcome-box">
            <h1>Chào mừng đến với Website Bánh Kẹo!</h1>
            <p><i class="fa-solid fa-cookie-bite"></i>Thưởng thức những hương vị ngọt ngào nhất<i class="fa-solid fa-candy-cane"></i></p>
        </div>
<div class="top-products">
    <h2>🔥 Sản phẩm bán chạy nhất</h2>
        <p class="best-seller-intro">Khám phá những món bánh kẹo được yêu thích nhất, mang đến hương vị tuyệt vời và chất lượng tuyệt hảo.</p>
    <div class="product-list">
        <div class="product">
            <a href="/dangnhap">
                <img src="https://tuoimart.vn/wp-content/uploads/2024/10/BANH-LU-310G.jpg" alt="Bánh Quy Bơ Pháp">
            </a>
            <h3 style="color: black;">Bánh quy bơ Pháp</h3>
            <p>Giá: 150.000đ</p>
        </div>
        <div class="product">
            <a href="/dangnhap">
                <img src="https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lz7izl2rf0dd6a" alt="Kẹo dâu tây">
            </a>
            <h3>Kẹo dâu tây</h3>
            <p>Giá: 30.000đ</p>
        </div>
        <div class="product">
            <a href="/dangnhap">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrTkKEq2N1IUUqfAHqBf_V9HHMENsNTI9a0Q&s" alt="Socola den">
            </a>
            <h3>Chocolate đen</h3>
            <p>Giá: 70.000đ</p>
        </div>
    </div>

</div>
<div class="guarantee-section">
    <img src="https://gianghuy.com/wp-content/uploads/2024/02/banner-blog-giang-huy.jpg" alt="Nguồn gốc nhập hàng">
    <div class="guarantee-text">
        <h3 style="margin: 0; font-size: 24px; font-weight: bold; text-align: center; width: 100%;">
        🔹 Đảm Bảo Chất Lượng & Nguồn Gốc Sản Phẩm</h3>
       <p style="font-size: 18px; color: #333; line-height: 1.6; text-align: justify; font-weight: 500;">
    Chúng tôi cam kết cung cấp các sản phẩm bánh kẹo chất lượng cao, được tuyển chọn từ những thương hiệu uy tín. 
    Mỗi sản phẩm đều có nguồn gốc rõ ràng, đảm bảo an toàn vệ sinh thực phẩm, 
    mang đến những hương vị thơm ngon và đảm bảo sức khỏe. Hãy yên tâm mua sắm và thưởng thức những sản phẩm tuyệt vời từ chúng tôi!</p>
    </div>
</div>
<div class="quality-support">
    <div class="support-box">
        <div class="support-content">
            <div class="text">
                <h3 style="text-align: center; margin-bottom: 10px; color: black;">🔹 Dịch Vụ Khách Hàng & Hỗ Trợ Mua Sắm</h3>
                <p style="line-height: 1.7; text-align: justify; color: black; letter-spacing: 0.5px;">
                    👉 Chúng tôi luôn sẵn sàng hỗ trợ khách hàng trong quá trình mua sắm, từ tư vấn chọn sản phẩm đến giải đáp thắc mắc. <br>
                    👉 Chính sách đổi trả linh hoạt giúp bạn an tâm hơn khi mua sắm trực tuyến. <br>
                    👉 Giao hàng nhanh chóng, đóng gói cẩn thận, đảm bảo sản phẩm đến tay bạn trong tình trạng tốt nhất. <br>
                    👉 Hỗ trợ nhiều phương thức thanh toán an toàn, tiện lợi.
                </p>
            </div>
            <img src="https://images.baoangiang.com.vn/image/fckeditor/upload/2023/20230103/images/T11%20(2).jpg" alt="Hỗ trợ khách hàng" class="support-img">
        </div>
    </div>
</div>
<div class="info-box left-box">
    <img src="https://blog.dktcdn.net/files/ung-dung-ship-hang-1.jpg" alt="Giao Hàng Nhanh" class="info-image">
    <div class="text-content">
        <h3 style="text-align: center; margin-bottom: 10px; color: black;">🚀 Giao Hàng Nhanh Chóng & Tiện Lợi</h3>
        <p style="line-height: 2.2; text-align: justify; color: black; letter-spacing: 0.5px;">
            ✅ Hỗ trợ giao hàng toàn quốc nhanh chóng. <br>
            ✅ Đóng gói kỹ lưỡng, bảo vệ sản phẩm nguyên vẹn. <br>
            ✅ Theo dõi đơn hàng trực tiếp trên hệ thống. <br>
            ✅ Chính sách đổi trả linh hoạt nếu có lỗi từ nhà cung cấp.
        </p>
    </div>
</div>
<button id="scrollToTop" style="position: fixed; bottom: 90px; right: 20px; display: none;">-⬆-</button>
<script>
    document.addEventListener("DOMContentLoaded", function () {
        let scrollBtn = document.getElementById("scrollToTop");
        
        window.onscroll = function () {
            scrollBtn.style.display = (window.scrollY > 1200) ? "block" : "none";
        };

        scrollBtn.onclick = function () {
            window.scrollTo({ top: 0, behavior: "smooth" });
        };
    });
</script>

<footer style="background: rgba(0, 0, 0, 0.8); color: white; text-align: center; padding: 15px; margin-top: 30px;">
    <p style="margin: 5px 0; font-size: 16px;">&copy; 2025 Bánh Kẹo Ngọt</p>
    <p style="margin: 5px 0;">Liên hệ: <a href="#" style="color: #ff9800; text-decoration: none;">banhkeoshop@gmail.com</a></p>
    <p style="margin: 5px 0;">Theo dõi chúng tôi:  
        <a href="#" style="color: #ff9800; margin: 0 8px;">Facebook</a> |  
        <a href="#" style="color: #ff9800; margin: 0 8px;">Instagram</a> |  
        <a href="#" style="color: #ff9800; margin: 0 8px;">Tiktok</a>
    </p>
    <p style="margin: 5px 0;">Địa chỉ: ....,Hà Nội </p>
</footer>

</body>
</html>
"""

@trangchu_bp.route('/')
def home():
    return html_content
