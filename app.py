from flask import Flask
from blueprints.trangchu import trangchu_bp
from blueprints.dangnhap import dangnhap_bp
from blueprints.dangky import dangky_bp
from blueprints.mua import mua_bp 
from blueprints.muaAd import muaAd_bp 
from blueprints.sanphamAd import sanphamAd_bp
from blueprints.taikhoanAd import taikhoanAd_bp 
from blueprints.giohang import giohang_bp 
from blueprints.themsp import themsp_bp 
from blueprints.thanhtoan import thanhtoan_bp 
from blueprints.donhang import donhang_bp 
from blueprints.donhangAd import donhangAd_bp
from blueprints.taikhoanNv import taikhoanNv_bp 
from blueprints.thongkeAd import thongkeAd_bp 
from blueprints.doimk import doimk_bp
from blueprints.nhaphangAd import nhaphangAd_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Đăng ký Blueprint
app.register_blueprint(trangchu_bp)
app.register_blueprint(dangnhap_bp)
app.register_blueprint(dangky_bp)
app.register_blueprint(mua_bp)  
app.register_blueprint(muaAd_bp)  
app.register_blueprint(sanphamAd_bp)
app.register_blueprint(donhangAd_bp) 
app.register_blueprint(taikhoanAd_bp)  
app.register_blueprint(giohang_bp)
app.register_blueprint(themsp_bp)
app.register_blueprint(thanhtoan_bp)
app.register_blueprint(donhang_bp)
app.register_blueprint(taikhoanNv_bp) 
app.register_blueprint(thongkeAd_bp)
app.register_blueprint(doimk_bp)
app.register_blueprint(nhaphangAd_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

