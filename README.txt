1. Vào trang chrome://version/ kiểm tra phiên bản chrome, tìm ở dòng đầu tiên
	(vd: 102.0.5005.115)
2. Vào trang https://chromedriver.chromium.org/downloads tải về đúng phiên bản, giải nén để vào thư mục mong muốn, để đường dẫn đến file đó vào dòng 11 của file crawler.py
	(vd: self.driver = webdriver.Chrome("C://setup//chromedriver_win32//chromedriver.exe")
3. mở Command Prompt, đến vị trí file crawler.py được lưu
4. gõ python drawler.py