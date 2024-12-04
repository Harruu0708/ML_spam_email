import pandas as pd

# Đường dẫn tới file CSV
file_path = "../data_train/test.csv"

# Đọc file CSV
df = pd.read_csv(file_path)

# Đảm bảo tất cả giá trị trong cột 'Message' là chuỗi, thay NaN bằng chuỗi rỗng
df['Message'] = df['Message'].fillna("").astype(str)

# Tính độ dài của từng message
df['Message_Length'] = df['Message'].apply(len)

# Đếm số lượng message trong các khoảng độ dài
count_0_10 = len(df[(df['Message_Length'] >= 0) & (df['Message_Length'] <= 10)])
count_11_100 = len(df[(df['Message_Length'] >= 11) & (df['Message_Length'] <= 100)])
count_101_1000 = len(df[(df['Message_Length'] >= 101) & (df['Message_Length'] <= 1000)])
count_1001_10000 = len(df[(df['Message_Length'] >= 1001) & (df['Message_Length'] <= 10000)])
count_10001_100000 = len(df[(df['Message_Length'] >= 10001) & (df['Message_Length'] <= 100000)])

# In kết quả
print("Số lượng dữ liệu có độ dài message từ 0-10:", count_0_10)
print("Số lượng dữ liệu có độ dài message từ 11-100:", count_11_100)
print("Số lượng dữ liệu có độ dài message từ 101-1000:", count_101_1000)
print("Số lượng dữ liệu có độ dài message từ 1001-10000:", count_1001_10000)
print("Số lượng dữ liệu có độ dài message từ 10001-100000:", count_10001_100000)
