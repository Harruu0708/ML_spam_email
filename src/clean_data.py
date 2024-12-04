import pandas as pd

# Đường dẫn tới file CSV
file_path = "../data_formatted/merged_file.csv"

# Đọc file CSV
df = pd.read_csv(file_path)

# Đảm bảo tất cả giá trị trong cột 'Message' là chuỗi, thay NaN bằng chuỗi rỗng
df['Message'] = df['Message'].fillna("").astype(str)

# Tính độ dài của từng message
df['Message_Length'] = df['Message'].apply(len)

# Lọc bỏ các hàng có độ dài 'Message' lớn hơn 100000
df_filtered = df[df['Message_Length'] <= 100000]

# Xóa cột 'Message_Length' nếu không cần thiết
df_filtered = df_filtered.drop(columns=['Message_Length'])

# Ghi dữ liệu sau khi lọc vào file mới
filtered_file_path = "../data_cleaned/cleaned_data.csv"
df_filtered.to_csv(filtered_file_path, index=False)

print(f"Dữ liệu sau khi lọc đã được lưu vào '{filtered_file_path}'")
