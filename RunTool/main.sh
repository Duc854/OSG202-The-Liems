#!/bin/bash

# Hàm hiển thị menu chính
show_main_menu() {
    selection=$(zenity --list --title="Main Menu" --text="Choose an option:" --column="Option" "Lấy dữ liệu trúng thưởng" "Đưa dữ liệu vào database" "Dua 3 so xuat hien nhieu nhat, it nhat moi giai" --height=200 --width=350)

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
        "Dua 3 so xuat hien nhieu nhat, it nhat moi giai")
            # Gọi hàm để xử lý tùy chọn 3
            python3 ~/OSG202-The-Liems/SapXep/sort.py
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

# Vòng lặp để hiển thị menu chính liên tục
while true; do
    show_main_menu
done

