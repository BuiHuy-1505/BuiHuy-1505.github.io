import mysql.connector

class Database:
    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="banhkeo"
            )
            if connection.is_connected():
                return connection
        except mysql.connector.Error as err:
            print("❌ Lỗi kết nối database:", err)
            return None  

    def fetch_data(self, query, params=None):
        if self.connection is None:
            print("❌ Lỗi: Chưa kết nối database!")
            return []
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetch_one(self, query, params=None):
        if self.connection is None:
            print("❌ Lỗi: Chưa kết nối database!")
            return None
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def execute_query(self, query, params=None):
        if self.connection is None:
            print("❌ Lỗi: Chưa kết nối database!")
            return False
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        self.connection.commit()
        cursor.close()
        return True

    def insert(self, query, params=None):  # 🔹 Sửa lỗi trong hàm này
        """Thực hiện INSERT và trả về ID của dòng vừa thêm"""
        if self.connection is None:
            print("❌ Lỗi: Chưa kết nối database!")
            return None
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        self.connection.commit()
        last_id = cursor.lastrowid  # 🔹 Lấy ID của bản ghi vừa thêm
        cursor.close()
        return last_id
    def insert_and_get_id(self, query, params=None):
        """Thêm bản ghi và lấy ID của bản ghi vừa chèn."""
        if self.connection is None:
            print("❌ Lỗi: Chưa kết nối database!")
            return None
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        self.connection.commit()
        last_id = cursor.lastrowid  # Lấy ID của bản ghi vừa chèn
        cursor.close()
        return last_id
    def close(self):
        if self.connection:
            self.connection.close()
