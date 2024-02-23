#!/bin/bash

# Hiển thị menu chính
show_main_menu() {
    selection=$(zenity --list --title="Main Menu" --text="Choose an option:" --column="Option" "Lấy dữ liệu trúng thưởng" "Đưa dữ liệu vào database" "Update data" --height=250 --width=300)

    case $selection in
        "Lấy dữ liệu trúng thưởng")
            # Hiển thị thông báo trước khi thực hiện tác vụ
            # Thực thi tập lệnh fetchData.sh trong giao diện đồ họa
            gnome-terminal -- bash -c "cd ~/OSG202-The-Liems/FetchData && ./fetchData.sh; bash"
            ;;
        "Đưa dữ liệu vào database")
            # Thực thi tùy chọn 2
            python3 ~/OSG202-The-Liems/Insert/convert_json_to_sql2.py
            ;;
        "Update data")
            # Gọi hàm để xử lý tùy chọn 3
            handle_update_data
            ;;
        *)
            # Người dùng chọn thoát hoặc đóng cửa sổ
            ;;
    esac
}

# Xử lý tùy chọn "Update data"
handle_update_data() {
    # Cập nhật dữ liệu tới trước ngày hiện tại
    # Thực hiện các thao tác cần thiết
    # Đưa ra kết quả cho người dùng
    zenity --info --text="Updating data to before the current date."
}

# Hiển thị menu chính khi chạy script
show_main_menu

