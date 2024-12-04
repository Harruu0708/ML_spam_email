import pandas as pd
import os

# Đường dẫn thư mục chứa các file CSV cần ghép
folder_path = '../data_formatted'  # Thay bằng đường dẫn thư mục của bạn

# Lấy danh sách tất cả các file CSV trong thư mục
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Đọc và ghép tất cả các file CSV
all_data = pd.concat([pd.read_csv(os.path.join(folder_path, f)) for f in csv_files], ignore_index=True)

# Lưu kết quả vào một file CSV mới
output_file_path = '../data_formatted/merged_file.csv'
all_data.to_csv(output_file_path, index=False)

print(f"Đã ghép các file và lưu tại: {output_file_path}")
