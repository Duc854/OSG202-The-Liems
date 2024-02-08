import json
import sqlite3
import os

# Đường dẫn đến tệp JSON
json_file_path = '~/OSG202-The-Liems/KetQua/ketqua.json'

# Chuyển đổi ~ thành đường dẫn thực sự của thư mục home
json_file_path = os.path.expanduser(json_file_path)

# In đường dẫn để kiểm tra
print("Đường dẫn đến tệp JSON:", json_file_path)

# Đọc nội dung từ file JSON
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Kết nối đến cơ sở dữ liệu SQLite (hoặc cơ sở dữ liệu của bạn)
conn = sqlite3.connect('output2.db')
cursor = conn.cursor()

# Tạo bảng trong cơ sở dữ liệu (sửa lại cột 'category' thành 'category_name')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS my_table (
        date TEXT,
        category_name TEXT,  -- Thay đổi 'category' thành 'category_name'
        value TEXT
    )
''')

# Chuyển đổi dữ liệu từ JSON thành bảng SQL
for date, values in data['data'].items():
    for category, category_values in values.items():
        for value in category_values:
            # Kiểm tra giá trị trống và bỏ qua nếu giá trị là rỗng
            if value != "":
                cursor.execute('''
                    INSERT INTO my_table (date, category_name, value)
                    VALUES (?, ?, ?)
                ''', (date, category, value))

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

