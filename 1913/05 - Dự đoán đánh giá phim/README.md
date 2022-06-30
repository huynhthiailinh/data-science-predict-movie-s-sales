## Hướng dẫn chạy code 
---
### 1. CRAWL và EDA dữ liệu
-   Nguồn dữ liệu: Được Crawl dữ liệu từ [REELGOOD](https://reelgood.com/movies)
-   Thư viện được yêu cầu cài đặt: [beautifulsoup4](https://pypi.org/project/beautifulsoup4/), [pandas](https://pypi.org/project/pandas/), [numpy](https://pypi.org/project/numpy/)
-   Chạy file crawl.ipynb để thực hiện việc crawl dữ liệu và ta thu được 1 file dữ liệu chứa thông tin phim.
-   Chạy file eda_endterm.ipynb để thực hiện việc EDA dữ liệu
---
### 2. Clean và Featuring dữ liệu
- Trong bước này ta cần có các thư viện như [scikit-learn](https://scikit-learn.org/stable/index.html), [pandas](https://pypi.org/project/pandas/), [numpy](https://pypi.org/project/numpy/), [scipy](https://pypi.org/project/scipy/), [matplotlib](https://matplotlib.org/), [seaborn](https://seaborn.pydata.org/index.html)
- Chạy file clean_data.ipynb để thực hiện việc Clean dữ liệu và ta thu được 4 file dữ liệu chứa thông tin phim bao gồm Xtrain, Xtest, Ytrain, Ytest cho quá trình tiếp theo.
---
### 3. Modelling sử dụng Linear Regression, KNN Regression, Bagging Regression để dự đoán phim
-   Từ dữ liệu đã output ra từ clean và featuring, chúng ta có thể chạy file modelling.ipynb để thực hiện việc modelling.
-   Với thư viện cần có [scikit-learn](https://scikit-learn.org/stable/index.html), [numpy](https://numpy.org/doc/stable/index.html), [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html), [matplotlib](https://matplotlib.org/index.html), [seaborn](https://seaborn.pydata.org/index.html)
-   Chạy file modelling.ipynb để thực hiện việc modelling và theo dõi các markdown để xem kết quả và các thông tin của bài toán.

---
## Tất cả hướng cái file cần thiết sẽ được gói gọn trong file requirements.txt thực hiên câu lệnh : <ins> pip install -r requirements.txt </ins> để cài đặt các thư viện cần thiết 

