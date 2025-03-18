from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.android import UiAutomator2Options

# Cấu hình tùy chọn cho Appium
options = UiAutomator2Options()
options.platform_name = "Android"  # Định rõ hệ điều hành Android
options.device_name = "R3CN206A5GL"  # Tên thiết bị Android
options.app = r"C:\Users\quan\Downloads\32\app_demo\build\app\outputs\flutter-apk\app-release.apk"  # Đường dẫn đến file APK
options.automation_name = "UiAutomator2"  # Dùng UiAutomator2 để tự động hóa
options.app_package = "com.example.app_demo"  # Gói ứng dụng cần kiểm thử
options.app_activity = ".MainActivity"  # Activity khởi chạy của ứng dụng
options.no_reset = True  # Không reset dữ liệu ứng dụng khi chạy test

# Khởi tạo kết nối với Appium Server
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

# Chờ ứng dụng load
time.sleep(3)

# Hàm thực hiện phép toán và kiểm tra kết quả
def calculate_and_verify(num1, operator, num2, expected_result):
    # Tìm và nhấn vào số thứ nhất
    driver.find_element(AppiumBy.XPATH, f"//android.widget.Button[@content-desc='{num1}']").click()
    # Tìm và nhấn vào toán tử
    driver.find_element(AppiumBy.XPATH, f"//android.widget.Button[@content-desc='{operator}']").click()
    # Tìm và nhấn vào số thứ hai
    driver.find_element(AppiumBy.XPATH, f"//android.widget.Button[@content-desc='{num2}']").click()
    # Nhấn nút "=" để thực hiện phép tính
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='=']").click()

    # Lấy danh sách các phần tử hiển thị kết quả
    elements  = driver.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
    result_element = elements[3]  # Kết quả thường hiển thị ở vị trí thứ 3

    # Lấy nội dung kết quả từ thuộc tính content-desc
    actual_result = result_element.get_attribute("content-desc")

    # So sánh kết quả nhận được với kết quả mong đợi
    assert (actual_result == "Error" and expected_result == "Error") or float(actual_result) == float(expected_result), \
        f"Test failed: {num1} {operator} {num2} != {actual_result}"
    
    # In ra kết quả nếu bài test thành công
    print(f"Test passed: {num1} {operator} {num2} = {actual_result}")

# Chạy các test case với các phép toán khác nhau
calculate_and_verify(3, "+", 5, 8)
calculate_and_verify(9, "-", 4, 5)
calculate_and_verify(6, "*", 7, 42)
calculate_and_verify(8, "/", 0, "Error")  # Kiểm thử phép chia cho 0
calculate_and_verify(8, "/", 2, 4)

# Đóng kết nối với Appium Server sau khi hoàn thành kiểm thử
driver.quit()
