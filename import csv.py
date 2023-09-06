import csv
# Create a list of data to write to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Mary', 25, 'Boston'],
    ['Bob', 40, 'Chicago']
]
# Open a CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the data to the CSV file
    csvwriter.writerows(data)

# Trong tài liệu mô-đun CSV, bạn có thể tìm thấy các hàm sau:

# csv.field_size_limit - trả lại kích thước trường tối đa

# csv.get_dialect - lấy dữ liệu được liên kết với tên

# csv.list_dialects - hiển thị tất cả các dữ liệu đã đăng ký

# csv.reader - đọc dữ liệu từ tệp csv

# csv.register_dialect - liên kết dữ liệu với tên

# csv.writer - ghi dữ liệu vào tệp csv

# csv.unregister_dialect - xóa dữ liệu liên quan đến tên đăng ký

# csv.QUOTE_ALL - Trích dẫn mọi thứ, không phân biệt kiểu.

# csv.QUOTE_MINIMAL – Trích dẫn các trường chứa ký tự đặc biệt

# csv.QUOTE_NONNUMERIC - Trích dẫn tất cả các trường không có giá trị số

# csv.QUOTE_NONE - Không trích dẫn bất cứ điều gì ở đầu ra