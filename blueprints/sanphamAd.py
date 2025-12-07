from flask import Blueprint, request, redirect, render_template_string
from database import Database  
from flask import render_template

sanphamAd_bp = Blueprint('sanphamAd', __name__, url_prefix='/sanphamAd')
db = Database()

@sanphamAd_bp.route('/')
def list_products():
    query = "SELECT * FROM sanpham"
    products = db.fetch_data(query) 
    return render_template_string(PRODUCT_TEMPLATE, products=products, selected_category=None)
# Lọc sản phẩm theo danh mục
@sanphamAd_bp.route('/loc')
def loc_sanpham():
    category_id = request.args.get('category_id', type=int)  
    if category_id:
        products = db.fetch_data("SELECT * FROM sanpham WHERE category_id = %s", (category_id,))
    else:
        products = db.fetch_data("SELECT * FROM sanpham")

    return render_template_string(PRODUCT_TEMPLATE, products=products, selected_category=category_id)
# Thêm sản phẩm
@sanphamAd_bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        category_id = request.form['category_id']
        url_img = request.form.get('url_img', '')

        query = """
        INSERT INTO sanpham (name, description, price, stock, category_id, url_img, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, NOW())
        """
        db.execute_query(query, (name, description, price, stock, category_id, url_img))
        return redirect('/sanphamAd/loc?category_id=')  
    return render_template_string(ADD_TEMPLATE, selected_category=None)
# Sửa sản phẩm
@sanphamAd_bp.route('/edit/<int:sp_id>', methods=['GET', 'POST'])
def edit_product(sp_id):
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        category_id = request.form['category_id']
        url_img = request.form.get('url_img', '')

        query = """
        UPDATE sanpham 
        SET name = %s, description = %s, price = %s, stock = %s, category_id = %s, url_img = %s
        WHERE id = %s
        """
        db.execute_query(query, (name, description, price, stock, category_id, url_img, sp_id))
        return redirect('/sanphamAd/loc?category_id=')

    query = "SELECT * FROM sanpham WHERE id = %s"
    product = db.fetch_one(query, (sp_id,))
    
    if not product:
        return "Sản phẩm không tồn tại!", 404

    return render_template_string(EDIT_TEMPLATE, product=product, selected_category=product['category_id'] )

# Xóa sản phẩm
@sanphamAd_bp.route('/delete/<int:sp_id>', methods=['POST'])
def delete_product(sp_id):
    query = "DELETE FROM sanpham WHERE id = %s"
    db.execute_query(query, (sp_id,))
    return redirect('/sanphamAd/loc?category_id=')

PRODUCT_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Quản lý sản phẩm</title>
    <style>
    body { font-family: Arial, sans-serif; background: #f8d775; }
    .container { width: 80%; margin: auto; background: white; padding: 20px; border-radius: 10px; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    th, td { border: 1px solid black; padding: 10px; text-align: center; }

    a, button { padding: 8px 12px; text-decoration: none; color: white; border: none; cursor: pointer; }
    .edit { background: blue; border-radius: 5px; }  
    .delete { background: red; border-radius: 5px; }  
    .add { background: green; border-radius: 5px; }  
    img { width: 120px; height: auto; border-radius: 8px; }

    .add-btn { padding: 12px 25px; border-radius: 10px; background: #28a745; color: white; font-weight: bold; }
    .add-btn:hover { background: #218838; transform: scale(1.05); }
    td:nth-child(2), th:nth-child(2) { font-weight: bold;max-width: 150px; }
    td:nth-child(3), th:nth-child(3) { max-width: 100px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    td:nth-child(6), th:nth-child(6) { max-width: 200px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    td:nth-child(3):hover, td:nth-child(6):hover { white-space: normal; background: #f8f9fa; }
</style>
</head>
<body>
    <div class="container">
        <h1>📦 Quản lý Sản phẩm</h1>
        <div style="display: flex; justify-content: space-between;">
            <a href="/sanphamAd/add" class="add-btn">➕ Thêm sản phẩm</a>
            <a href="/muaAd" style="padding: 10px 6px; border-radius: 8px; background: yellow; color: black; font-weight: bold; text-decoration: none;">
                ⬅️ Quay lại <br>
            </a>
        </div>
<div style="display: flex; justify-content: center; margin-top: 10px;">
    <form method="GET" action="/sanphamAd/loc"> 
        <label for="category">Chọn danh mục:</label>
        <select name="category_id" id="category" onchange="this.form.submit()">
            <option value="" {% if not selected_category %}selected{% endif %}>Tất cả</option>
            <option value="1" {% if selected_category|int == 1 %}selected{% endif %}>1. Chocolate</option>
            <option value="2" {% if selected_category|int == 2 %}selected{% endif %}>2. Kẹo dẻo</option>
            <option value="3" {% if selected_category|int == 3 %}selected{% endif %}>3. Bánh quy</option>
        </select>
    </form>
</div>
        <table>
    <tr>
        <th>ID</th><th>Tên</th><th>Mô tả</th><th>Giá</th><th>Số lượng</th><th>Ảnh</th><th></th>
    </tr>
    {% for sp in products %}
    <tr>
        <td>{{ sp.id }}</td>
        <td>{{ sp.name }}</td>
        <td>{{ sp.description }}</td>
        <td>{{ "{:,.0f}".format(sp.price) }}</td>
        <td>{{ sp.stock }}</td>
        <td><img src="{{ sp.url_img }}" alt="Hình ảnh"></td>
        <td>
            <a href="/sanphamAd/edit/{{ sp.id }}" class="edit" style="border-radius: 5px;">✏ Sửa</a>
            <form action="/sanphamAd/delete/{{ sp.id }}" method="POST" style="display:inline;"
                  onsubmit="confirmDelete(this);">
                <button type="submit" class="delete" style="border-radius: 5px;">❌ Xóa</button>
            </form>
        </td>
    </tr>
    {% endfor %}
</table>

<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
<script>
function confirmDelete(form) {
    event.preventDefault();
    Swal.fire({
        title: 'Xác nhận xóa?',
        text: "Bạn có chắc chắn muốn xóa sản phẩm này?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Xóa',
        cancelButtonText: 'Hủy',
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6'
    }).then((result) => {
        if (result.isConfirmed) {
            form.submit();
        }
    });
}
</script>
 
</body>
</html>
"""
# 🎨 Giao diện thêm sản phẩm
ADD_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Thêm sản phẩm</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f8d775; }
        .container { width: 50%; margin: auto; background: white; padding: 20px; border-radius: 10px;margin-top:50px; }
        input, textarea { width: 100%; margin-bottom: 10px; padding: 5px; }
        button { padding: 10px; background: green; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Thêm sản phẩm</h1>
        <form method="POST">
            <label>Tên sản phẩm:</label>
            <input type="text" name="name" required>
            
            <label>Mô tả:</label>
            <textarea name="description" required></textarea>
            
            <label>Giá:</label>
            <input type="number" name="price" required>
            
            <label>Số lượng:</label>
            <input type="number" name="stock" required>
<label for="category">Chọn danh mục:</label>
<select name="category_id" id="category">
    <option value="" {% if not selected_category %}selected{% endif %}>Chọn</option>
    <option value="1" {% if selected_category|int == 1 %}selected{% endif %}>1. Chocolate</option>
    <option value="2" {% if selected_category|int == 2 %}selected{% endif %}>2. Kẹo dẻo</option>
    <option value="3" {% if selected_category|int == 3 %}selected{% endif %}>3. Bánh quy</option>
</select>


            <label style="display:block;margin-top:12px;">URL ảnh:</label>
            <input type="text" name="url_img">

            <div style="display: flex; justify-content: space-between; align-items: center;">
                <button type="submit" style="border-radius: 8px; padding: 10px 20px; cursor: pointer;">
                    Thêm sản phẩm
                </button>
                <button onclick="window.location.href='/sanphamAd'" 
                    style="background-color: red; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer;">
                    Hủy
                </button>
            </div>
    </div>
</body>
</html>
"""
# 🎨 Giao diện sửa sản phẩm
EDIT_TEMPLATE = ADD_TEMPLATE.replace("Thêm sản phẩm", "Sửa sản phẩm").replace("Thêm", "Lưu").replace(
    '<input type="text" name="name" required>',
    '<input type="text" name="name" value="{{ product.name }}" required>'
).replace(
    '<textarea name="description" required></textarea>',
    '<textarea name="description" required>{{ product.description }}</textarea>'
).replace(
    '<input type="number" name="price" required>',
    '<input type="number" name="price" value="{{ product.price }}" required>'
).replace(
    '<input type="number" name="stock" required>',
    '<input type="number" name="stock" value="{{ product.stock }}" required>'
).replace(
    '<input type="number" name="category_id" required>',
    '<input type="number" name="category_id" value="{{ product.category_id }}" required>'
).replace(
    '<input type="text" name="url_img">',
    '<input type="text" name="url_img" value="{{ product.url_img }}">'
)

