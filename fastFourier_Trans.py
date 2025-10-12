import numpy as np  # Thư viện numpy để xử lý các phép toán mảng và tính toán FFT 
import pandas as pd  # Thư viện pandas để đọc và xử lý dữ liệu từ file CSV 
import matplotlib.pyplot as plt  # Thư viện matplotlib để vẽ đồ thị 
 
# Đọc dữ liệu từ file CSV (giả sử tín hiệu ở dạng 16-bit) 
data = pd.read_csv("D:\Esp-idf\Mysource\sph0645_test\data_text\data_heartSound_3rd.csv", header=None)  # Đọc file CSV vào dataframe 
data.columns = ['Amplitude']  # Đặt tên cho cột dữ liệu là 'Amplitude' 
 
# Chuyển dữ liệu từ cột Amplitude thành numpy array và ép kiểu thành số nguyên 16-bit 
signal = data['Amplitude'].to_numpy(dtype=np.int16)  # Chuyển dữ liệu cột 'Amplitude' thành mảng numpy và ép kiểu int16 
 
# Tham số tín hiệu 
fs = 4000  # Tần số lấy mẫu (Hz), cần thay đổi nếu tín hiệu thực tế có tần số mẫu khác 
N = len(signal)  # Số mẫu của tín hiệu (số phần tử trong mảng) 
T = 1 / fs  # Chu kỳ lấy mẫu (thời gian giữa hai mẫu liên tiếp) 
 
# Sử dụng windowing (hàm Hanning) để làm mượt phổ tín hiệu, giảm bớt nhiễu 
windowed_signal = signal * np.hanning(len(signal))  # Áp dụng hàm Hanning lên tín hiệu 
 
# Thực hiện FFT (biến đổi Fourier nhanh) trên tín hiệu đã được windowing 
fft_values = np.abs(np.fft.fft(windowed_signal))  # Lấy giá trị tuyệt đối của FFT để có biên độ 
frequencies = np.fft.fftfreq(N, d=T)  # Tính tần số tương ứng cho các giá trị FFT 
 
# Tính biên độ (magnitude) của tín hiệu trong miền tần số, chuẩn hóa theo số mẫu 
amplitude = 2 / N * np.abs(fft_values)  # Chuẩn hóa biên độ của tín hiệu trong miền tần số 
 
# Tạo trục thời gian cho tín hiệu gốc 
time = np.linspace(0, N * T, N)  # Tạo mảng thời gian với số phần tử tương ứng với số mẫu tín hiệu 
 
# Vẽ đồ thị 
plt.figure(figsize=(12, 8))  # Thiết lập kích thước đồ thị 
 
# Đồ thị 1: Tín hiệu trong miền thời gian (Time Domain) 
plt.subplot(2, 1, 1)  # Tạo một biểu đồ con trong một cửa sổ (2 hàng, 1 cột) 
plt.plot(time, signal, linewidth=0.7, color='blue')  # Vẽ tín hiệu gốc trong miền thời gian 
plt.title("Miền thời gian (Time Domain)")  # Tiêu đề cho đồ thị 
plt.xlabel("Thời gian (s)")  # Nhãn trục x: thời gian (giây) 
plt.ylabel("Cường độ sóng âm")  # Nhãn trục y: biên độ tín hiệu 
plt.grid()  # Bật lưới 
 
# Đồ thị 2: Phổ tần số (Frequency Domain) 
plt.subplot(2, 1, 2)  # Đồ thị con thứ 2 
plt.plot(frequencies, amplitude, linewidth=0.7, color='red')  # Vẽ phổ tần số của tín hiệu 
plt.title("Miền tần số (Frequency Domain)")  # Tiêu đề cho đồ thị 
plt.xlabel("Tần số (Hz)")  # Nhãn trục x: tần số (Hz) 
plt.ylabel("Cường độ tần số")  # Nhãn trục y: biên độ tần số 
plt.grid()  # Bật lưới 
 
plt.tight_layout()  # Điều chỉnh khoảng cách giữa các đồ thị con 
plt.show()  # Hiển thị đồ thị 
