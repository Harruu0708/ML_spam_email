import pandas as pd
import matplotlib.pyplot as plt

# Đọc file CSV
file_path = "../data_train/test.csv"  # Đổi thành đường dẫn file của bạn
df = pd.read_csv(file_path)

# Đảm bảo cột Message là chuỗi, thay NaN bằng chuỗi rỗng
df['Message'] = df['Message'].fillna("").astype(str)

# Tính độ dài của từng message
df['Message_Length'] = df['Message'].apply(len)

# Xác định các khoảng độ dài
bins = [0, 10, 100, 1000, 10000, 100000]
labels = ["0-10", "11-100", "101-1000", "1001-10000", "10001-100000"]

# Phân nhóm độ dài vào các khoảng
df['Length_Range'] = pd.cut(df['Message_Length'], bins=bins, labels=labels, right=True)

# Đếm số lượng trong từng khoảng
range_counts = df['Length_Range'].value_counts(sort=False)

# Tính tỷ lệ
total_messages = len(df)
range_ratios = (range_counts / total_messages)  # Tính tỷ lệ

# Tạo biểu đồ cột
plt.figure(figsize=(8, 6))
plt.bar(range_ratios.index.astype(str), range_ratios.values, color='skyblue', edgecolor='black')
plt.title('Tỷ lệ dữ liệu theo độ dài thông điệp', fontsize=16)
plt.xlabel('Khoảng độ dài thông điệp', fontsize=12)
plt.ylabel('Tỷ lệ (%)', fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0, 1.1 * range_ratios.max())  # Điều chỉnh trục Y để phù hợp với giá trị lớn nhất
plt.tight_layout()

# Hiển thị biểu đồ
plt.show()

