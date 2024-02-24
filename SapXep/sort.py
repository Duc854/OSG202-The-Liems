import sqlite3
import os

# Xác định đường dẫn đến file database
db_file_path = '~/OSG202-The-Liems/Database/database.db'
db_file_path = os.path.expanduser(db_file_path)	
# Kết nối với cơ sở dữ liệu	
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS my_table (
        category_name TEXT,
        value INTEGER
    )
''')
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
    print(f'3 số ít nhất của {category}:')
    for row in cursor.fetchall():
        print(f'Số {row[0]} xuất hiện {row[1]} lần')

    # Lấy 3 số xuất hiện nhiều nhất
    cursor.execute(f'''
        SELECT value, COUNT(*) as appearance_count
        FROM my_table
        WHERE category_name = ?
        GROUP BY value
        ORDER BY appearance_count DESC
        LIMIT 3
    ''', (category,))
    print(f'3 số nhiều nhất của {category}:')
    for row in cursor.fetchall():
        print(f'Số {row[0]} xuất hiện {row[1]} lần')

conn.close()