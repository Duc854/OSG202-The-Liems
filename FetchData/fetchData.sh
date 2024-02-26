read -p "Nhập ngày bắt đầu (theo định dạng YYYY-MM-DD): " start_date

read -p "Nhập ngày kết thúc (theo định dạng YYYY-MM-DD): " end_date

output_file="../KetQua/ketqua.json"

current_date="$start_date"

# Mở file để ghi kết quả
echo "{" > "$output_file"
echo '  "data": {' >> "$output_file"

# Hàm để trích xuất giải và giá trị từ đoạn HTML
extract_result() {
    local prize="$1"
    local value="$2"

    # Thay thế dấu xuống dòng bằng dấu cách
    local formatted_value=$(echo "$value" | tr '\n' ' ')

    # Xóa dấu cách cuối cùng
    formatted_value="${formatted_value%" "}"

    # Kiểm tra nếu value là mảng
    if [[ ${#value[@]} ]]; then
        # Nếu là mảng, sử dụng dấu ngoặc vuông để đại diện cho mảng trong JSON
        echo '      "'"$prize"'": [' >> "$output_file"
        
        count=0
        for val in $formatted_value; do
            echo '        "'"$val"'",' >> "$output_file"
            ((count++))
        done
        
        # Viet them vao cho du 6 phan tu
        if [[ count -lt 6 ]]; then 
            for ((i=0; i < 6 - count; i++)); do
                echo '        "'""'",' >> "$output_file"
            done
        fi
        
        # Xóa dấu phẩy cuối cùng và đóng mảng JSON
        sed -i '$ s/,$//' "$output_file"
        echo '      ],' >> "$output_file"
    else
        # Nếu không phải mảng, sử dụng chuỗi thông thường
        echo '      "'"$prize"'": ["'"$formatted_value"'"],' >> "$output_file"
    fi
}







while [ "$current_date" != "$end_date" ]; do
    formatted_date=$(date -d "$current_date" +%d-%m-%Y) 
    url="https://www.minhchinh.com/ket-qua-xo-so/$formatted_date.html"
    
    # Thực hiện lệnh curl với URL tương ứng và lưu vào file
    html_content=$(curl -s "$url")

    # Bắt đầu một ngày mới trong file JSON
    echo '    "Ngay '"$formatted_date"'": {' >> "$output_file"

    # Trích xuất giải ĐB và giá trị
    db_prize=$(echo "$html_content" | grep -oP '<td class="giai_dac_biet"><span class="box_kh khtemp">([0-9]+-[0-9]+-[0-9]+-[0-9]+-[0-9]+-[0-9]+-[0-9]+-[0-9]+ [A-Z]+)</span><div class="lq_1" data="([0-9]+)">[0-9]+</div></td>' | grep -oP 'data="([0-9]+)"' | grep -oP '[0-9]+')
    extract_result "G.DB" "$db_prize"

    # Các giải từ Nhất đến Bảy
    prizes=("Nhất" "Nhì" "Ba" "Tư" "Năm" "Sáu" "Bảy")
    nhat=$(echo "$html_content" | grep -oP '<td class="giai_nhat"><div class="lq_1" data="[0-9]+">[0-9]+</div></td>' | grep -oP 'data="([0-9]+)"' | grep -oP '[0-9]+')
    extract_result "G.Nhat" "${nhat[@]: -5}"

    nhi=$(echo "$html_content" | grep -oP '<td class="giai_nhi"><div class="lq_1" data="[0-9]+">[0-9]+</div><div class="lq_2" data="[0-9]+">[0-9]+</div></td>' | grep -oP 'data="([0-9]+)"' | grep -oP '[0-9]+')
extract_result "G.Nhi" "${nhi[@]}"

ba=$(echo "$html_content" | grep -oP '<td class="giai_ba"><div class="lq_1" data="[0-9]+">[0-9]+</div><div class="lq_2" data="[0-9]+">[0-9]+</div><div class="lq_3" data="[0-9]+">[0-9]+</div><div class="lq_4" data="[0-9]+">[0-9]+</div><div class="lq_5" data="[0-9]+">[0-9]+</div><div class="lq_6" data="[0-9]+">[0-9]+</div></td>' | grep -oP 'data="([0-9]+)"' | grep -oP '[0-9]+')
extract_result "G.Ba" "${ba[@]}"

tu=$(echo "$html_content" | grep -oP '<td class="giai_tu"><div class="lq_1" data="[0-9]+">[0-9]+</div><div class="lq_2" data="[0-9]+">[0-9]+</div><div class="lq_3" data="[0-9]+">[0-9]+</div><div class="lq_4" data="[0-9]+">[0-9]+</div></td>' | grep -oP 'data="([0-9]+)"' | grep -oP '[0-9]+')
extract_result "G.Tu" "${tu[@]}"

nam=$(echo "$html_content" | grep -oP '<td class="giai_nam"><div class="lq_1" data="[0-9]+">[0-9]+</div><div class="lq_2" data="[0-9]+">[0-9]+</div><div class="lq_3" data="[0-9]+">[0-9]+</div><div class="lq_4" data="[0-9]+">[0-9]+</div><div class="lq_5" data="[0-9]+">[0-9]+</div><div class="lq_6" data="[0-9]+">[0-9]+</div></td>' | grep -oP 'data="([0-9]+)"' | grep -oP '[0-9]+')
extract_result "G.Nam" "${nam[@]}"

sau=$(echo "$html_content" | grep -oP '<td class="giai_sau"><div class="lq_1" data="[0-9]+">[0-9]+</div><div class="lq_2" data="[0-9]+">[0-9]+</div><div class="lq_3" data="[0-9]+">[0-9]+</div></td>' | grep -oP 'data="([0-9]+)"' | grep -oP '[0-9]+')
extract_result "G.Sau" "${sau[@]: -11}"

bay=$(echo "$html_content" | grep -oP '<td class="giai_bay"><div class="lq_1" data="[0-9]+">[0-9]+</div><div class="lq_2" data="[0-9]+">[0-9]+</div><div class="lq_3" data="[0-9]+">[0-9]+</div><div class="lq_4" data="[0-9]+">[0-9]+</div></td>' | grep -oP 'data="([0-9]+)"' | grep -oP '[0-9]+')
extract_result "G.Bay" "${bay[@]}"
sed -i '$ s/,$//' "$output_file"

    # Kết thúc một ngày trong file JSON
    echo '    },' >> "$output_file"
    
    # Tăng ngày lên 1
    current_date=$(date -d "$current_date + 1 day" +%Y-%m-%d)
done

# Xóa dấu phẩy cuối cùng và đóng file JSON
sed -i '$ s/,$//' "$output_file"
echo '  }' >> "$output_file"
echo "}" >> "$output_file"

