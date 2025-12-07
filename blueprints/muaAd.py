from flask import Blueprint, render_template_string

muaAd_bp = Blueprint('muaAd', __name__, url_prefix='/muaAd')

@muaAd_bp.route('/')
def index():
    return render_template_string(PAGE_TEMPLATE)

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📦 Quản lý Mua Hàng</title>
<style>
    body { font-family: 'Poppins', Arial, sans-serif; background: linear-gradient(to right, #f7b42c, #fc575e); margin: 0; padding: 0; display: flex; justify-content: flex-start; height: 100vh; color: #fff; flex-direction: column; }
    .header { width: 100%; background: rgba(255, 255, 255, 0.75); padding: 10px 16px; text-align: center; font-size: 24px; font-weight: bold; color: #333; border-bottom: 2px solid #ff9800; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); position: fixed; top: 0; left: 0; z-index: 1000; }
    .grid-container { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; width: 100%; max-width: 700px; margin-top: px; justify-content: flex-start; }
    .grid-box { padding: 10px; border: 2px solid #ff9800; border-radius: 12px; background: rgba(255, 255, 255, 0.9); box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15); width: 100%;margin-left:10px; }
    .grid-item { display: flex; justify-content: center; align-items: center; height: 130px; background: #ff9800; color: white; font-weight: bold;
      text-decoration: none; font-size: 18px; border-radius: 8px; transition: 0.3s; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; }
    .grid-item:hover { background: #ff5722; transform: scale(1.05); }
    .logout { position: fixed; width: 600px; max-width: 600px; text-align: center; bottom: 20px;right: 0px; }
    .logout-btn { width: 600px; text-align: center; background-color: #FF6F00; color: white; border-radius: 8px; padding: 12px; font-weight: bold; text-decoration: none; transition: 0.3s; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); display: block;margin-left: 0px; }
    .logout-btn:hover { background-color: #FF3D00; transform: scale(1.05); }
    .overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5); z-index: 999; }
    .popup { flex-direction: column; align-items: center; display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: #fff; padding: 20px; border-radius: 8px; z-index: 1000; }
    .popup p { margin: 15px 0; font-size: 16px; color: #333; }
    .popup button { padding: 8px 15px; border-radius: 5px; font-size: 10px; margin: 10px 5px; cursor: pointer; width: 40% }
    .popup .confirm { background-color: #FF6F00; color: white; border: none; }
    .popup .cancel { background-color: #aaa; }
    .popup button:hover { transform: scale(1.05); }
</style>

</head>
<body>
    <div class="header">📦 Trang Quản lý Bán Hàng của Admin</div>  
<div class="grid-container grid-3" style=" margin-top: 70px;">
    <div class="grid-box"><a href="/sanphamAd/loc?category_id=" class="grid-item">📦 Quản lý sản phẩm</a></div>
    <div class="grid-box"><a href="/taikhoanNv" class="grid-item">🏢 Quản lý Nhân viên</a></div>
    <div class="grid-box"><a href="/thongkeAd" class="grid-item">📊 Báo cáo thống kê</a></div>
</div>

<div class="grid-container grid-2">
    <div class="grid-box"><a href="/taikhoanAd" class="grid-item">👤 Tài khoản khách hàng</a></div>
    <div class="grid-box"><a href="/donhangAd" class="grid-item">🛒 Quản lý đơn hàng</a></div>
</div>

<div class="grid-container grid-1">
    <div class="grid-box"><a href="/nhaphangAd" class="grid-item">📥 Quản lý nhập hàng</a></div>
</div>

    <div class="logout">
        <a href="#" class="logout-btn" onclick="showPopup()">↩️ Đăng xuất</a>
    </div>
    <div class="overlay" id="overlay"></div>
    <div class="popup" id="logoutPopup">
        <p>Bạn có chắc chắn muốn đăng xuất?</p>
        <button class="confirm" onclick="logout()">OK</button>
        <button class="cancel" onclick="closePopup()">Hủy</button>
    </div>

    <script>
        function showPopup() {
            document.getElementById("overlay").style.display = "block";
            document.getElementById("logoutPopup").style.display = "block";
        }
        function closePopup() {
            document.getElementById("overlay").style.display = "none";
            document.getElementById("logoutPopup").style.display = "none";
        }
        function logout() {
            window.location.href = "/";  
        }
    </script>
</body>
</html>
"""
