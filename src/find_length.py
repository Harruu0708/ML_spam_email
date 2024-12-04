import pandas as pd

# Đường dẫn đến file CSV
file_path = '../data_formatted/merged_file.csv'  # Thay bằng đường dẫn file của bạn

# Đọc file CSV
data = pd.read_csv(file_path)

# Xử lý giá trị NaN hoặc các giá trị không hợp lệ trong cột 'Message'
data['Message'] = data['Message'].fillna('')  # Thay NaN bằng chuỗi rỗng

# Tính độ dài của các email trong cột 'Message'
data['Message_Length'] = data['Message'].apply(len)

# Lọc các dòng có độ dài nhỏ hơn 10
short_messages = data[data['Message_Length'] <= 10]

# Đếm số lượng các dòng có độ dài nhỏ hơn 10
short_messages_count = len(short_messages)

# In kết quả
print(f"Số lượng email có độ dài nhỏ hơn 10 ký tự: {short_messages_count}")
print("Dữ liệu của các dòng có độ dài nhỏ hơn 10 ký tự:")
print(short_messages[['Category', 'Message']])
