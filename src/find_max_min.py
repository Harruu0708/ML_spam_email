import pandas as pd

# Đường dẫn đến file CSV
file_path = '../data_cleaned/cleaned_file.csv'  # Thay bằng đường dẫn file của bạn

# Đọc file CSV
data = pd.read_csv(file_path)

# Xử lý giá trị NaN hoặc các giá trị không hợp lệ trong cột 'Message'
data['Message'] = data['Message'].fillna('')  # Thay NaN bằng chuỗi rỗng

# Tính độ dài của các email trong cột 'Message'
data['Message_Length'] = data['Message'].apply(len)

# Tìm email có độ dài ngắn nhất và dài nhất
shortest_email = data.loc[data['Message_Length'].idxmin()]
longest_email = data.loc[data['Message_Length'].idxmax()]

# In ra kết quả
print("Email có độ dài ngắn nhất:")
print(f"Chỉ mục dòng: {shortest_email.name}")
print(f"Category: {shortest_email['Category']}, Length: {shortest_email['Message_Length']}")
print(f"Message: {shortest_email['Message']}\n")

print("Email có độ dài dài nhất:")
print(f"Category: {longest_email['Category']}, Length: {longest_email['Message_Length']}")
# print(f"Message: {longest_email['Message']}")
