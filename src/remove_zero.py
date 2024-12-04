import pandas as pd

# Đường dẫn đến file CSV
file_path = '../data_formatted/merged_file.csv'  # Thay bằng đường dẫn file của bạn

# Đọc file CSV
data = pd.read_csv(file_path)

# Xử lý giá trị NaN hoặc các giá trị không hợp lệ trong cột 'Message'
data['Message'] = data['Message'].fillna('')  # Thay NaN bằng chuỗi rỗng

# Tính độ dài của các email trong cột 'Message'
data['Message_Length'] = data['Message'].apply(len)

# Tìm email có độ dài ngắn nhất
shortest_email_length = data['Message_Length'].min()

# Lọc các dòng có độ dài giống với email ngắn nhất
shortest_email_rows = data[data['Message_Length'] == shortest_email_length]

# Đếm số lượng các dòng này
shortest_email_count = len(shortest_email_rows)

# Xóa các dòng có độ dài ngắn nhất khỏi dữ liệu
data_cleaned = data[data['Message_Length'] != shortest_email_length]

# Lưu lại dữ liệu sau khi xóa
output_file_path = '../data_cleaned/cleaned_file.csv'
data_cleaned.to_csv(output_file_path, index=False)

# In kết quả
print(f"Số lượng email có độ dài ngắn nhất ({shortest_email_length} ký tự): {shortest_email_count} đã bị xóa.")
print(f"Dữ liệu đã được lưu vào file: {output_file_path}")
