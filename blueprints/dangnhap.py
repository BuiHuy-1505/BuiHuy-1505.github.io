from flask import Blueprint, render_template_string, request, redirect, url_for, session
from database import Database

dangnhap_bp = Blueprint('dangnhap', __name__)
@dangnhap_bp.route('/dangnhap', methods=['GET', 'POST'])
def dangnhap():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = Database()
        db.connect()
        
        admin_query = "SELECT * FROM admin WHERE username = %s AND password = %s"
        admin_result = db.fetch_data(admin_query, (username, password))
        user_query = "SELECT * FROM users WHERE username = %s AND password = %s"
        user_result = db.fetch_data(user_query, (username, password))       
        db.close()    
        if admin_result:
            session['admin_id'] = admin_result[0]['id']
            session['user'] = username
            return redirect(url_for('muaAd.index'))
        elif user_result:
            session['user_id'] = user_result[0]['id']  
            session['user'] = user_result[0]['username']
            return redirect(url_for('mua.trang_mua'))
        else:
            return render_template_string(HTML_TEMPLATE, error="SAI TÀI KHOẢN HOẶC MẬT KHẨU!")

    return render_template_string(HTML_TEMPLATE, error=None)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đăng Nhập</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: Arial, sans-serif; }
        body { display: flex; justify-content: center; align-items: center; height: 100vh; 
            background: url('https://haycafe.vn/wp-content/uploads/2022/03/background-tra-sua-hoat-hinh-800x430.jpg') no-repeat center center/cover; }
        .container { width: 440px; padding: 30px; background: rgba(255, 255, 255, 0.85);]
        height: 500px; border-radius: 10px; box-shadow: 0 0 15px rgba(0, 0, 0, 0.1); text-align: center; }
        h1 { margin-bottom: 15px; color: #333; font-size: 30px;font-weight: bold;text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); }
        input, button { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; }
        button { background: #007bff; color: white; border: none; cursor: pointer; font-size: 18px; }
        button:hover { background: #0056b3; }
        .error { color: red; margin-bottom: 10px; font-size: 14px; }
        a { text-decoration: none; color: #007bff; font-size: 16px; }
        .back-btn {font-size: 13px;padding: 4px 8px; border-radius: 5px; width: 60%;
          margin: 8px auto; text-align: center;background: #aaa;border: 1px solid #ccc; margin-bottom: 65px;}  
        .back-btn:hover { background: #545b62; }
        .subtitle { font-style: italic; color: #333; font-size: 14px; margin-bottom: 5px; }
        .candy-icons { font-size: 20px; margin-bottom: 35px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Đăng Nhập</h1>
        <p class="subtitle">🍭 Một cú click – Cả thế giới bánh kẹo đang chờ bạn! 🍫</p>
        <div class="candy-icons">🧁 🍩 🎂</div>
        {% if error %}
            <p class="error">{{ error }}</p>
        {% endif %}
        <form method="POST">
            <input type="text" name="username" placeholder="Tên đăng nhập" required>
            <input type="password" name="password" placeholder="Mật khẩu" required>
            <button type="submit">Đăng nhập</button>
            <a href="{{ url_for('trangchu.home') }}"><button type="button" class="back-btn">🏠 Quay lại Trang Chủ</button></a>
        </form>
        <p><i>Chưa có tài khoản? <a href="{{ url_for('dangky.dangky') }}">Đăng ký</a></i></p>
    </div>
</body>
</html>
"""
