def get_data():
	url = "https://chuyencuadev.com/captcha"
	for i in range (1, 1000):
		filename = '{0:04}.jpg'.format(i)
		print(filename)
		with open(filename, 'wb') as f:
			response = requests.get(url)
			if response.ok: f.write(response.content)
