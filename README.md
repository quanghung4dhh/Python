# Tìm hiểu Python

## Cài đặt Python
Truy cập trang chính thức của Python [Python download](https://www.python.org/downloads/)
## Kiểm tra cài đặt:
Mở terminal và nhập lệnh: 
```bash
python --version
```
Nếu có hiển thị phiên bản Python là đã thành công

# Chạy Vi điều khiển ESP32 bằng Python
## Nguyên tắc:
Sử dụng một phiên bản Python tối ưu cho vi xử lí (khác với Python3 trên máy tính) gọi là MicroPython <br>
Để có thể chạy vi điều khiển ESP32 bằng Python thì cần phải flash firmware MicroPython (một file .bin) vào bộ nhớ ESP32 <br>
Khi nạp code, ESP32 sẽ biên dịch thành bytecode nội bộ, thực thi trực tiếp trên đó mà không cần hệ điều hành
## Cách flash firmware MicroPython và dùng mpremote để nạp và chạy ESP32:
### Tải firmware MicroPython cho ESP32 từ trang: [https://micropython.org/download/ESP32_GENERIC/](https://micropython.org/download/ESP32_GENERIC/)
### Cài đặt thư viện esptool để cài firmware:
```bash
pip install esptool
```
### Xóa toàn bộ bộ nhớ flash của ESP32 (nếu cần):
```bash
esptool --port COMx erase_flash
```
(COMx là cổng kết nối với ESP32)
### Nạp firmware cho ESP32:
```bash
esptool --chip esp32 --port COMx write_flash -z 0x1000 <Đường dẫn đến file bin vừa tải>
```
(COMx là cổng kết nối với ESP32)
### Cài đặt thư viện mpremote để nạp và chạy code ESP32:
```bash
pip install mpremote
```
### Kiểm tra cài đặt:
```bash
mpremote --version
```
### Kiểm tra cổng kết nối với ESP32:
```bash
mpremote connect list
```
Đầu ra có thể là:
```bash
COM3 0001 10c4:ea60 Silicon Laboratories None
```
(COM3 là cổng kết nối với ESP32)
### Mở REPL
```bash
mpremote connect COM3 repl
```
Ở đây có thể viết và chạy trực tiếp code Python cho ESP32. Ví dụ:
```python
import sys
print(sys.platform)
```
Kết quả in ra:
```bash
esp32
```
Thoát REPL bằng cách nhấn tổ hợp phím Ctrl+J hoặc Ctrl+x
### Nạp code Python cho ESP32. Có thể sử dụng file python ví dụ trong blink_led_python
Nạp code cho ESP32:
```bash
mpremote connect COM3 fs cp main.py :main.py
```
Chạy code vừa nạp vào trên ESP32:
```bash
mpremote connect COM3 run main.py
```
Liệt kê ra các file có trong ESP32:
```bash
mpremote connect COM3 fs ls
```
Xóa file đã nạp:
```bash
mpremote connect COM3 fs rm main.py
```
