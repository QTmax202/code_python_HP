from PyPDF2 import PdfReader
from PIL import Image

reader = PdfReader(r'C:\Users\DELL\Documents\Zalo Received Files\Thông báo nghỉ lễ 30-4.pdf')

page = reader.pages[0]
count = 0
print(page.extract_text())

# for image_file_object in page.images:
#     with open(str(count) + image_file_object.name, "wb") as fp:
#         fp.write(image_file_object.data)
#         count += 1

# reader = PdfReader(r'C:\Users\DELL\Documents\Zalo Received Files\Doc1.pdf')
# for page in reader.pages:
#     for image in page.images:
#         with open(image.name, "wb") as fp:
#             fp.write(image.data)
#             print(image.data)
