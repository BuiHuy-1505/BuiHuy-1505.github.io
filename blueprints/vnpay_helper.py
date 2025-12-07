import hmac
import hashlib
import urllib.parse
import datetime

def create_vnpay_url(tmn_code, hash_secret, return_url, order_id, amount, order_info):
    base_url = "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html"
    vnp_params = {
        "vnp_Version": "2.1.0",
        "vnp_Command": "pay",
        "vnp_TmnCode": tmn_code,
        "vnp_Amount": str(amount * 100),  
        "vnp_CurrCode": "VND",
        "vnp_TxnRef": str(order_id),
        "vnp_OrderInfo": order_info,
        "vnp_OrderType": "other",
        "vnp_Locale": "vn",
        "vnp_ReturnUrl": return_url,
        "vnp_CreateDate": datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
    }

    # Sắp xếp theo thứ tự A-Z để mã hóa
    sorted_params = sorted(vnp_params.items())
    query_string = urllib.parse.urlencode(sorted_params)

    # Tạo chuỗi để mã hóa
    hash_data = '&'.join(f"{k}={v}" for k, v in sorted_params)
    secure_hash = hmac.new(hash_secret.encode(), hash_data.encode(), hashlib.sha512).hexdigest()

    # Thêm secure hash vào URL
    payment_url = f"{base_url}?{query_string}&vnp_SecureHash={secure_hash}"
    return payment_url
