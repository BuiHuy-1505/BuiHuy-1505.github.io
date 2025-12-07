from flask import Blueprint, request, redirect, url_for, render_template_string
from database import Database

taikhoanNv_bp = Blueprint('taikhoanNv', __name__, url_prefix='/taikhoanNv')
db = Database()

@taikhoanNv_bp.route('/', methods=['GET', 'POST'])
def taikhoanNv():
    message = ""
    success = request.args.get('success')
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        sdt = request.form['sdt']
        address = request.form['address']

        if not sdt.isdigit() or len(sdt) != 10:
            message = "❌ Số điện thoại phải đủ 10 chữ số!"
        else:
            db.execute_query("INSERT INTO admin (username, email, password, sdt, address) VALUES (%s, %s, %s, %s, %s)", (username, email, password, sdt, address))
            return redirect(url_for('taikhoanNv.taikhoanNv', success=1))

    users = db.fetch_data("SELECT * FROM admin ORDER BY id ASC")
    return render_template_string(TEMPLATE, users=users, message=message, success=success)

TEMPLATE = """
<!DOCTYPE html>
<html lang=\"vi\">
<head>
    <meta charset=\"UTF-8\">
    <title>Quản lý Nhân Viên</title>
    <style>
        body { background: linear-gradient(to right, #ff9966, #ff5e62); font-family: Arial, sans-serif; text-align: center; margin: 0; padding: 20px; }  
.container { width: 85%; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2); text-align: left; }  
h2 {text-align: center;display: block;margin-bottom: 10px;width: 450px; font-size: 30px; font-weight: bold; color: #333; margin: 0 auto; background: #d3d3d3; padding: 10px 20px; border-radius: 7px; text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); border: 2px solid #ff9800; }  
.back-btn-container { text-align: left; width: 100%; }
.back-btn { margin-top: 10px; display: inline-block; margin-bottom: 15px; padding: 8px 12px; background: #ffeb3b; border-radius: 5px; text-decoration: none; color: #333; font-weight: bold; }  
.back-btn:hover { background: #f1d15f; }  
.form-container { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }  
.input-field { padding: 8px; width: 200px; border: 1px solid #ccc; border-radius: 5px; }  
.btn-add { margin-top:5px;padding: 4px 12px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; }  
.btn-add:hover { background: #218838; }  
table { width: 100%; margin-top: 20px; border-collapse: collapse; background: white; }
th, td { padding: 8px; border: 1px solid #ddd; text-align: left; }
th { background: #4facfe; color: white; } 
.delete-btn { background: #dc3545; color: white; padding: 6px 10px; border: none; border-radius: 5px; cursor: pointer; }  
.delete-btn:hover { background: #c82333; }  
.popup { height:100px;width:400px;position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
    background: #4caf50; color: white; padding: 20px 30px;border-radius: 8px; font-size: 18px; font-weight: bold;box-shadow: 0 0 15px rgba(0,0,0,0.3); z-index: 9999;}

    </style>
</head>
<body>
    <h2>👥 Quản lý Nhân Viên</h2>
<div class="back-btn-container">
    <a href="/muaAd" class="back-btn">⬅ Quay lại</a>
</div>
    <div class=\"container\">
        <div class=\"section\">
            <h3>➕ Thêm Nhân Viên</h3>
            <form method=\"POST\">
                <div class=\"form-group\">
                    <input type="text" name="username" placeholder="Tên đăng nhập" required style="padding: 12px; height: 8px; width: 200px; border: 1px solid #ccc; border-radius: 5px;">
                    <input type="email" name="email" placeholder="Email" required style="padding: 12px; height: 8px; width: 200px; border: 1px solid #ccc; border-radius: 5px;">
                    <input type="password" name="password" placeholder="Mật khẩu" required style="padding: 12px; height: 8px; width: 200px; border: 1px solid #ccc; border-radius: 5px;">
                    <input type="text" name="sdt" placeholder="Số điện thoại" required style="padding: 12px; height: 8px; width: 200px; border: 1px solid #ccc; border-radius: 5px;">
                    <input type="text" name="address" placeholder="Địa chỉ" required style="padding: 12px; height: 8px; width: 432px; border: 1px solid #ccc; border-radius: 5px;margin-top:3px;">
                </div>
                <button type=\"submit\" class=\"btn btn-add\">Thêm Nhân Viên</button>
            </form>
        </div>
        
        <div class=\"section\">
            <h3>📋 Danh Sách Nhân Viên</h3>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Tên</th>
                    <th>Email</th>
                    <th>SĐT</th>
                    <th>Địa chỉ</th>
                    <th>Ngày tạo</th>
                </tr>
                {% for user in users %}
                <tr>
                    <td>{{ user['id'] }}</td>
<td>{{ user['username'] }}</td>
<td>{{ user['email'] }}</td>
<td>{{ user['sdt'] }}</td>
<td>{{ user['address'] }}</td>
<td>{{ user['created_at'] }}</td>

                </tr>
                {% endfor %}
            </table>
        </div>
    </div>
{% if success %}
<div id="popup" class="popup"><h3>🎉 Thêm tài khoản nhân viên thành công!</h3></div>
<script>
    setTimeout(() => {
        document.getElementById('popup').style.display = 'none';
    }, 5000);
</script>
{% endif %}

</body>
</html>
"""
