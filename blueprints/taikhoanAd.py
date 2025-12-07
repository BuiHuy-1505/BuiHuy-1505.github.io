from flask import Blueprint, render_template_string, request, redirect, url_for, jsonify
from database import Database  

taikhoanAd_bp = Blueprint("taikhoanAd", __name__, url_prefix="/taikhoanAd")
db = Database()  

@taikhoanAd_bp.route("/", methods=["GET", "POST"])
def danh_sach_taikhoan():
    search = request.form.get("search", "").strip()

    query = "SELECT id, username, email, sdt, diachi, created_at FROM users"
    if search:
        query += " WHERE username LIKE %s OR email LIKE %s"
        users = db.fetch_data(query + " ORDER BY id DESC", (f"%{search}%", f"%{search}%"))
    else:
        users = db.fetch_data(query + " ORDER BY id DESC")

    html = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Quản lý tài khoản</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <style>
            body {background-image: url("https://thumb.photo-ac.com/2d/2da1c041eb14a8acc823f3477823d632_t.jpeg");  /* Đường dẫn tới ảnh */
                background-size: cover; background-position: center;background-attachment: fixed; }
            .reset-icon {font-size: 1rem;display: inline-block;transform: scale(1.5); }
            .search-box { width: 200px; }
            .table{ background-color: rgba(255, 255, 255, 0.8);border-radius: 8px; overflow: hidden;}
        </style>
    </head>
    <body class="container mt-4">
        <h2 class="text-center fw-bold text-primary" style="font-size: 2rem; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);">
            Quản lý tài khoản
        </h2>
        <form method="POST" class="mb-3 d-flex justify-content-between">
            <a href="/muaAd" style="padding: 10px 10px; border-radius: 10px; background: yellow; color: black; font-weight: bold; text-decoration: none;">
                        ⬅️ Quay lại
                    </a>
            <div class="d-flex">
                <button type="button" class="btn btn-secondary ms-2" id="resetSearch" style="margin-right:5px;">
                    <span class="reset-icon">🔄</span>
                </button>
                <input type="text" name="search" id="searchBox" class="form-control me-2" placeholder="Tìm username/email" value="{{ request.form.get('search', '') }}">
                <button type="submit" class="btn btn-primary">🔍</button>
            </div>
        </form>
        <!-- Bảng danh sách tài khoản -->
        <table class="table table-bordered">
            <thead class="table-light">
                <tr>
                    <th>ID</th>
                    <th>Tên đăng nhập</th>
                    <th>Email</th>
                    <th>Số điện thoại</th>
                    <th>Địa chỉ</th>
                    <th>Ngày tạo</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {% for user in users %}
                <tr>
                    <td>{{ user.id }}</td>
                    <td>{{ user.username }}</td>
                    <td>{{ user.email }}</td>
                    <td>{{ user.sdt }}</td>
                    <td>{{ user.diachi }}</td>
                    <td>{{ user.created_at }}</td>
                    <td class="text-center">
                        <button class="btn btn-warning btn-sm edit-btn" 
                                data-id="{{ user.id }}" data-username="{{ user.username }}" 
                                data-email="{{ user.email }}" data-sdt="{{ user.sdt }}" 
                                data-diachi="{{ user.diachi }}">Sửa</button>
                        <a href="{{ url_for('taikhoanAd.xoa_taikhoan', id=user.id) }}" 
                           class="btn btn-danger btn-sm" onclick="return confirm('Bạn có chắc muốn xóa?');">Xóa</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <!-- Form Thêm tài khoản -->
        <h4 class="mt-4">Thêm tài khoản mới</h4>
        <form method="POST" action="{{ url_for('taikhoanAd.them_taikhoan') }}">
            <div class="mb-2"><input type="text" name="username" class="form-control" placeholder="Tên đăng nhập" required></div>
            <div class="mb-2"><input type="email" name="email" class="form-control" placeholder="Email" required></div>
            <div class="mb-2"><input type="password" name="password" class="form-control" placeholder="Mật khẩu" required></div>
            <div class="mb-2"><input type="text" name="sdt" class="form-control" placeholder="Số điện thoại" required></div>
            <div class="mb-2"><input type="text" name="diachi" class="form-control" placeholder="Địa chỉ" required></div>
            <button type="submit" class="btn btn-success">Thêm tài khoản</button>
        </form>

        <!-- Popup sửa tài khoản -->
        <div class="modal fade" id="editModal" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Sửa tài khoản</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <form id="editForm">
                            <input type="hidden" id="edit-id">
                            <div class="mb-3">
                                <label class="form-label">Tên đăng nhập</label>
                                <input type="text" id="edit-username" class="form-control">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Email</label>
                                <input type="email" id="edit-email" class="form-control">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Số điện thoại</label>
                                <input type="text" id="edit-sdt" class="form-control">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Địa chỉ</label>
                                <input type="text" id="edit-diachi" class="form-control">
                            </div>
                            <div class="modal-footer d-flex justify-content-between">
                                <button type="button" class="btn btn-success" id="saveChanges">Lưu</button>
                                <button type="button" class="btn btn-danger bg-opacity-50" data-bs-dismiss="modal">Hủy</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <script>
        $(document).ready(function() {
            $(".edit-btn").click(function() {
                $("#edit-id").val($(this).data("id"));
                $("#edit-username").val($(this).data("username"));
                $("#edit-email").val($(this).data("email"));
                $("#edit-sdt").val($(this).data("sdt"));
                $("#edit-diachi").val($(this).data("diachi"));
                $("#editModal").modal("show");
            });

            $("#saveChanges").click(function() {
                let id = $("#edit-id").val();
                let data = {
                    username: $("#edit-username").val(),
                    email: $("#edit-email").val(),
                    sdt: $("#edit-sdt").val(),
                    diachi: $("#edit-diachi").val()
                };

                $.post(`/taikhoanAd/sua/${id}`, data, function(response) {
                    if (response.success) {
                        location.reload();
                    } else {
                        alert("Lỗi cập nhật!");
                    }
                });
            });
        });
        </script>
        <script>
            document.getElementById("resetSearch").addEventListener("click", function() {
                document.getElementById("searchBox").value = ""; // Xóa nội dung ô tìm kiếm
                document.forms[0].submit(); // Gửi lại form để hiển thị toàn bộ danh sách
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html, users=users)

@taikhoanAd_bp.route("/them", methods=["POST"])
def them_taikhoan():
    query = "INSERT INTO users (username, email, password, sdt, diachi) VALUES (%s, %s, %s, %s, %s)"
    db.execute_query(query, (request.form["username"], request.form["email"], request.form["password"], request.form["sdt"], request.form["diachi"]))
    return redirect(url_for("taikhoanAd.danh_sach_taikhoan"))

@taikhoanAd_bp.route("/xoa/<int:id>")
def xoa_taikhoan(id):
    db.execute_query("DELETE FROM users WHERE id = %s", (id,))
    return redirect(url_for("taikhoanAd.danh_sach_taikhoan"))

@taikhoanAd_bp.route("/sua/<int:id>", methods=["POST"])
def sua_taikhoan(id):
    success = db.execute_query("UPDATE users SET username=%s, email=%s, sdt=%s, diachi=%s WHERE id=%s", 
                               (request.form["username"], request.form["email"], request.form["sdt"], request.form["diachi"], id))
    return jsonify({"success": success})
