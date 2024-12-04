import pandas as pd

# Đường dẫn đến file CSV
file_path = '../data_formatted/merged_file.csv'  # Thay bằng đường dẫn file của bạn

# Đọc file CSV và lấy dòng đầu tiên
first_row = pd.read_csv(file_path).iloc[0]

# In ra dòng đầu tiên
print("Dòng đầu tiên của file CSV là:")
print(first_row)
