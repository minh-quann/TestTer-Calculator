# Hướng dẫn cài đặt môi trường Appium

## Cài đặt Python
Trước tiên, cần cài đặt Python.  
Tải Python từ trang chính thức: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
Sau khi cài đặt, kiểm tra phiên bản bằng lệnh:
```sh
python --version
```

## Cài đặt pip
Python thường đi kèm với `pip`, nhưng nếu chưa có thì chạy lệnh sau để cài:
```sh
python -m ensurepip --default-pip
```
Sau khi cài đặt, kiểm tra phiên bản pip:
```sh
pip --version
```

## Cài đặt thư viện Appium cho Python
Sau khi đã có `pip`, cài đặt thư viện `Appium-Python-Client` bằng lệnh sau:
```sh
pip install Appium-Python-Client
```

## Cài đặt Appium Server
Tải và cài đặt Appium Server từ trang chính thức: [https://appium.io/](https://appium.io/)  
Sau khi cài đặt, kiểm tra xem Appium đã hoạt động chưa bằng lệnh:
```sh
appium -v
```
Để khởi chạy Appium Server, chạy lệnh:
```sh
appium
```

Sau khi hoàn thành các bước trên, môi trường Appium đã sẵn sàng để sử dụng.
