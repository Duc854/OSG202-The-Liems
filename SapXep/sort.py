import sqlite3
import pandas as pd
import os

# Xác định đường dẫn đến file database
db_file_path = '~/OSG202-The-Liems/Database/database.db'
db_file_path = os.path.expanduser(db_file_path)

# Kết nối với cơ sở dữ liệu
conn = sqlite3.connect(db_file_path)

# Định nghĩa danh sách các giải
categories = ['G.DB', 'G.Nhat', 'G.Nhi', 'G.Ba', 'G.Tu', 'G.Nam', 'G.Sau', 'G.Bay']

# Tạo một dictionary để lưu trữ kết quả
results = {'Category': [], 'Least': [], 'Least_Count': [], 'Most': [], 'Most_Count': []}

# Lặp qua từng giải và thực hiện câu lệnh SQL để lấy ra 3 số xuất hiện ít nhất và 3 số xuất hiện nhiều nhất
for category in categories:
    # Lấy 3 số xuất hiện ít nhất
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT value, COUNT(*) as appearance_count
        FROM my_table
        WHERE category_name = ?
        GROUP BY value
        ORDER BY appearance_count ASC
        LIMIT 3
    ''', (category,))
    least = [(row[0], row[1]) for row in cursor.fetchall()]
    
    # Lấy 3 số xuất hiện nhiều nhất
    cursor.execute(f'''
        SELECT value, COUNT(*) as appearance_count
        FROM my_table
        WHERE category_name = ?
        GROUP BY value
        ORDER BY appearance_count DESC
        LIMIT 3
    ''', (category,))
    most = [(row[0], row[1]) for row in cursor.fetchall()]

    # Thêm kết quả vào dictionary
    results['Category'].append(category)
    results['Least'].append(', '.join([str(num[0]) for num in least]))
    results['Least_Count'].append(', '.join([str(num[1]) for num in least]))
    results['Most'].append(', '.join([str(num[0]) for num in most]))
    results['Most_Count'].append(', '.join([str(num[1]) for num in most]))

# Tạo DataFrame từ dictionary kết quả
df = pd.DataFrame(results)

# Lưu DataFrame vào tệp Excel
output_excel_path = '~/OSG202-The-Liems/KetQua/KetQuaSort.xlsx'
df.to_excel(output_excel_path, index=False)

# Đóng kết nối với cơ sở dữ liệu
conn.close()


