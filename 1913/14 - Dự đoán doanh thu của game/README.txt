Các file trong thư mục và công dụng của chúng:
- 1 file pdf: đây là file báo cáo
- 3 file csv:
    + raw_data.csv: đây là file dữ liệu chưa xử lí sau khi cào dữ liệu về
    + clean_data.csv: đây là file dữ liệu đã được làm sạch giá trị nan và labelencode các đặc trưng cần thiết
    + view.csv: đây là file clean được thêm vào 1 vài đặc trưng gốc, phục vụ cho việc kiểm tra dữ liệu thông qua quan sát bằng mắt thường
- 2 file png:
    + Dữ liệu trên trang web: đây là hình ảnh giao diện của trang web mà nhóm sử dụng để cào dữ liệu
    + Lựa chọn đặt trưng: đây là hình ảnh mà nhóm lựa chọn các đặt trưng để cào thẻ HTML
- 3 file ipynb và thứ tự chạy, công dụng:
    + crawl_data: chạy file này đầu tiên để cào dữ liệu từ web, tạo ra file raw_data.csv
    + clean_data: chạy file này thứ hai để xử lý raw.csv, tạo ra 2 file clean_data.csv và view.csv
    + mainCode: chạy file này thứ ba để thực hiện các bước chính còn lại như chuẩn hoá, EDA, mô hình hoá dữ liệu, so sánh,...