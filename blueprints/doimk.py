from flask import Blueprint, request, session, redirect, render_template_string
from database import Database

doimk_bp = Blueprint("doimk", __name__)
db = Database()

@doimk_bp.route("/doimk", methods=["GET", "POST"])
def doi_mat_khau():
    if "user_id" not in session:
        return redirect("/dangnhap")

    user_id = session["user_id"]
    user = db.fetch_one("SELECT * FROM users WHERE id = %s", (user_id,))

    if not user:
        return "Không tìm thấy người dùng.", 404

    username = user["username"]
    message = ""

    if request.method == "POST":
        old_pw = request.form["old_password"]
        new_password = request.form['new_password']
        confirm_pw = request.form["confirm_password"]

        if user["password"] != old_pw:
            message = "❌ Mật khẩu cũ không đúng!"
        elif new_password != confirm_pw:
            message = "❌ Mật khẩu mới không khớp!"
        elif len(new_password) < 3:
            message = "❌ Mật khẩu mới phải có ít nhất 3 ký tự!"
        else:
            
            db.execute_query("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
            message = "✅ Đổi mật khẩu thành công!"

    return render_template_string(TEMPLATE, username=username, message=message)

TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>🔐 Đổi Mật Khẩu</title>
    <style>
        body { font-family: Arial, sans-serif; background: linear-gradient(to right, #f9f9f9, #ffe0b2); display: flex; justify-content: center; align-items: center; height: 100vh; }
        .form-container { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); width: 400px; text-align: center;height:450px; }
        h3 { color: #aaa; margin-bottom: 35px; }
        .form-group { margin-bottom: 15px; text-align: left; }
        label { display: block; font-weight: bold; margin-bottom: 5px; }
        input[type="password"] { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; }
        .btn { background-color: #ff6600; color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; width: 100%; }
        .btn:hover { background-color: #e65c00; }
        .message { margin-top: 15px; color: red; font-weight: bold; }
        .username { text-align: center; font-size: 26px; font-weight: bold; margin-top: 10px; color: #ff6600; }
        .cancel-btn { background: #aaa; color: black; padding: 10px; width: 10%; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; position: absolute; bottom: 10px; left: 0;left: 50%;transform: translateX(-50%); }
        .cancel-btn:hover { background: #777; }
    </style>
</head>
<body>
    <div class="form-container">
        <div class="username">👋 Xin chào, {{ username }}</div>
        <h3><i>🔐 Đổi mật khẩu</i></h3>
        <form method="post">
            <div class="form-group">
                <label for="old_password">Mật khẩu cũ:</label>
                <input type="password" id="old_password" name="old_password" required>
            </div>
            <div class="form-group">
                <label for="new_password">Mật khẩu mới:</label>
                <input type="password" id="new_password" name="new_password" required>
            </div>
            <div class="form-group">
                <label for="confirm_password">Nhập lại mật khẩu mới:</label>
                <input type="password" id="confirm_password" name="confirm_password" required>
            </div>
            <button type="submit" class="btn">Đổi mật khẩu</button>
            <button type="button" class="cancel-btn" onclick="window.location.href='/mua'">Quay lại</button>
        </form>
        {% if message %}
            <div class="message">{{ message }}</div>
        {% endif %}
    </div>
</body>
</html>
"""
