import sqlite3
import os

# Xác định đường dẫn đến file database
db_file_path = '~/OSG202-The-Liems/Database/database.db'
db_file_path = os.path.expanduser(db_file_path)

# Đường dẫn đến tệp KetQuaSort.txt trong cùng thư mục
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'KetQuaSort.txt')

# Kết nối với cơ sở dữ liệu
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# Tạo hoặc mở tệp KetQuaSort.txt để ghi kết quả
with open(output_file_path, 'a') as output_file:
    # Định nghĩa danh sách các giải
    categories = ['G.DB', 'G.Nhat', 'G.Nhi', 'G.Ba', 'G.Tu', 'G.Nam', 'G.Sau', 'G.Bay']

    # Lặp qua từng giải và thực hiện câu lệnh SQL để lấy ra 3 số xuất hiện ít nhất và 3 số xuất hiện nhiều nhất
    for category in categories:
        # Lấy 3 số xuất hiện ít nhất
        cursor.execute(f'''
            SELECT value, COUNT(*) as appearance_count
            FROM my_table
            WHERE category_name = ?
            GROUP BY value
            ORDER BY appearance_count ASC
            LIMIT 3
        ''', (category,))
        output_file.write(f'3 số ít nhất của {category}:\n')
        for row in cursor.fetchall():
            output_file.write(f'Số {row[0]} xuất hiện {row[1]} lần\n')

        # Lấy 3 số xuất hiện nhiều nhất
        cursor.execute(f'''
            SELECT value, COUNT(*) as appearance_count
            FROM my_table
            WHERE category_name = ?
            GROUP BY value
            ORDER BY appearance_count DESC
            LIMIT 3
        ''', (category,))
        output_file.write(f'3 số nhiều nhất của {category}:\n')
        for row in cursor.fetchall():
            output_file.write(f'Số {row[0]} xuất hiện {row[1]} lần\n')

# Đóng kết nối với cơ sở dữ liệu
conn.close()


