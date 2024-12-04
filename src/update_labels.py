import pandas as pd

# Đọc file CSV gốc
file_path = '../data/completeSpamAssassin.csv'  # Thay bằng đường dẫn file của bạn
data = pd.read_csv(file_path)

# Đổi tên cột để phù hợp với định dạng mới
data = data.rename(columns={'Label': 'Category', 'Body': 'Message'})

# Giữ lại chỉ hai cột cần thiết
data = data[['Category', 'Message']]

# Đổi nhãn 'spam' thành 1 và 'ham' thành 0
# data['Category'] = data['Category'].map({'spam': 1, 'ham': 0})

# Lưu lại file CSV đã định dạng
output_file_path = '../data/completeSpamAssassin_formatted.csv'  # Thay bằng đường dẫn file của bạn
data.to_csv(output_file_path, index=False)

print(f"File đã được định dạng lại và lưu tại: {output_file_path}")
