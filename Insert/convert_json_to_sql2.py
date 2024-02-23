import json
import sqlite3
import os

# Hàm để cập nhật cơ sở dữ liệu từ tệp JSON
def update_database_from_json(json_file_path, db_file_path):
    # Đọc nội dung từ file JSON
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Kiểm tra và thêm bảng nếu chưa tồn tại
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS my_table (
            date TEXT,
            category_name TEXT,
            value TEXT
        )
    ''')

    # Xóa toàn bộ dữ liệu cũ trong cơ sở dữ liệu
    cursor.execute("DELETE FROM my_table")

    # Duyệt qua dữ liệu từ tệp JSON và thêm vào cơ sở dữ liệu
    for date, values in data['data'].items():
        for category, category_values in values.items():
            for value in category_values:
                # Kiểm tra xem giá trị có rỗng không
                if value.strip():
                    # Thêm dữ liệu vào cơ sở dữ liệu
                    cursor.execute('''
                        INSERT INTO my_table (date, category_name, value)
                        VALUES (?, ?, ?)
                    ''', (date, category, value))

    # Lưu thay đổi và đóng kết nối
    conn.commit()
    conn.close()

# Đường dẫn đến tệp JSON và cơ sở dữ liệu SQLite
# Đường dẫn đến tệp JSON và cơ sở dữ liệu SQLite
json_file_path = '~/OSG202-The-Liems/KetQua/ketqua.json'
json_file_path = os.path.expanduser(json_file_path)
db_file_path = '~/OSG202-The-Liems/Database/database.db'
db_file_path = os.path.expanduser(db_file_path)


# Cập nhật cơ sở dữ liệu từ tệp JSON
update_database_from_json(json_file_path, db_file_path)

