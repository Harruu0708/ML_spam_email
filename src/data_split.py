from sklearn.model_selection import train_test_split
import pandas as pd

# Đọc dữ liệu từ file CSV
file_path = '../data_cleaned/cleaned_data.csv'  # Thay bằng đường dẫn tới file CSV của bạn
data = pd.read_csv(file_path)

# Xử lý giá trị NaN trong cột 'Message' (nếu có)
data['Message'] = data['Message'].fillna('')  # Thay NaN bằng chuỗi rỗng

# Bước 1: Chia dữ liệu thành train (70%) và tạm thời giữ lại validation + test (30%)
train, temp = train_test_split(
    data, test_size=0.3, stratify=data['Category'], random_state=42
)

# Bước 2: Chia tiếp tập validation + test (30%) thành validation (15%) và test (15%)
val, test = train_test_split(
    temp, test_size=0.5, stratify=temp['Category'], random_state=42
)

# Kiểm tra số lượng mẫu trong từng tập
print(f"Train: {len(train)} mẫu (Ham: {sum(train['Category'] == 0)}, Spam: {sum(train['Category'] == 1)})")
print(f"Validation: {len(val)} mẫu (Ham: {sum(val['Category'] == 0)}, Spam: {sum(val['Category'] == 1)})")
print(f"Test: {len(test)} mẫu (Ham: {sum(test['Category'] == 0)}, Spam: {sum(test['Category'] == 1)})")

# Lưu từng tập vào các file CSV riêng biệt
output_dir = '../data_train/'  # Thay bằng thư mục lưu của bạn
train.to_csv(output_dir + 'train.csv', index=False)
val.to_csv(output_dir + 'validation.csv', index=False)
test.to_csv(output_dir + 'test.csv', index=False)

print("Dữ liệu đã được chia và lưu thành các file:")
print(f"- Train: {output_dir}train.csv")
print(f"- Validation: {output_dir}validation.csv")
print(f"- Test: {output_dir}test.csv")
