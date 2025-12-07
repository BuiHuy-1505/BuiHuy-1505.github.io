from flask import Blueprint, render_template_string, request, redirect, url_for, flash
import re
from database import Database  

dangky_bp = Blueprint('dangky', __name__)

@dangky_bp.route('/dangky', methods=['GET', 'POST'])
def dangky():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        sdt = request.form['sdt']
        diachi = request.form['diachi']

        if password != confirm_password:
            flash("❌ Mật khẩu không khớp!", "danger")
            return redirect(url_for('dangky.dangky'))

        if not sdt.isdigit() or len(sdt) != 10:
            flash("⚠ Số điện thoại phải là số và có đúng 10 chữ số!", "warning")
            return redirect(url_for('dangky.dangky'))

        if '@' not in email or '.' not in email:
            flash("⚠ Email không hợp lệ!", "warning")
            return redirect(url_for('dangky.dangky'))

        db = Database()
        db.connect()
        existing_user = db.fetch_data("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        if existing_user:
            flash("⚠ Tài khoản hoặc email đã tồn tại!", "warning")
            return redirect(url_for('dangky.dangky'))

        query = """
            INSERT INTO users (username, email, password, sdt, diachi, created_at) 
            VALUES (%s, %s, %s, %s, %s, NOW())
        """
        result = db.execute_query(query, (username, email, password, sdt, diachi))
        db.close()

        if result:
            return render_template_string(PAGE_TEMPLATE, success=True, username=username, password=password)

    return render_template_string(PAGE_TEMPLATE, success=False, username='', password='')

PAGE_TEMPLATE = """
    <html>
    <head>
        <style>
            body { display: flex; justify-content: center; align-items: center; height: 100vh; background: #f4f4f4;background: url('https://png.pngtree.com/thumb_back/fh260/background/20210205/pngtree-simple-and-fresh-milk-tea-time-background-image_545752.jpg') no-repeat center center/cover; }
            .container { width: 400px; padding: 20px; background: rgba(255, 255, 185, 0.85);; border-radius: 8px; box-shadow: 0 0 10px #aaa; text-align: center; }
            h2 { margin-bottom: 15px; color: #333; font-size: 30px;font-weight: bold;text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); }
            p { font-size: 14px; font-style: italic; color: #555;margin-bottom: 30px; }
            input, button { width: 100%; padding: 10px; margin: 5px 0; border: 1px solid #ddd; border-radius: 5px; }
            button { background: #28a745; color: white; border: none; cursor: pointer; }
            button:hover { background: #218838; }
            a { text-decoration: none; color: #007bff; }
            .back-btn { font-size: 14px; padding: 5px 10px; border-radius: 5px; display: inline-block; margin-top: 10px; background: #f8f9fa; border: 1px solid #ccc; }
            .popup { 
                display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                background: white; padding: 20px; box-shadow: 0 0 10px #666; border-radius: 10px;
                text-align: center; width: 300px; font-size: 18px; 
            }
            .popup.show { display: block; }
        </style>
        <script>
            function showPopup() {
                document.getElementById("popup").classList.add("show");
                setTimeout(() => { window.location.href = "/dangnhap"; }, 5000);
            }
        </script>
    </head>
    <body onload="{% if success %}showPopup(){% endif %}">
        <div class="container">
            <h2>Đăng Ký</h2>
            <p>🌟 Đăng ký tài khoản ở đây nhá !</p>
            <form method="POST">
                <input type="text" name="username" placeholder="Tên đăng nhập" required>
                <input type="email" name="email" placeholder="Email" required>
                <input type="password" name="password" placeholder="Mật khẩu" required>
                <input type="password" name="confirm_password" placeholder="Nhập lại mật khẩu" required>
                <input type="text" name="sdt" placeholder="Số điện thoại" required>
                <input type="text" name="diachi" placeholder="Địa chỉ" required>
                <button type="submit">Đăng ký</button>
            </form>
            <p>Đã có tài khoản? <a href="/dangnhap">Đăng nhập</a></p>
            <a href="/" class="back-btn">🏠 Quay lại trang chủ</a>
        </div>

        <!-- Hộp thông báo -->
        <div id="popup" class="popup">
            ✅ Đăng ký thành công!<br>
            <b>Tài khoản: {{ username }}<br></b>
            <b>Mật khẩu: {{ password }}<br></b>
            Giờ sẽ chuyển sang trang Đăng Nhập!
        </div>
    </body>
    </html>
"""