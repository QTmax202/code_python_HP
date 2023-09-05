import requests

response = requests.get("https://tuoitre.vn/tin-moi-nhat.htm")

print(response.content)