
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.signal import iirnotch, filtfilt 
 
# Đọc tín hiệu gốc từ file CSV 
file_path = "D:/Esp-idf/Mysource/inmp441_test/data_text/Filter_test/filter_white_noise_test_1st.csv"  # Đường dẫn tới file CSV 
data = pd.read_csv(file_path, header=None)  # Đọc file CSV không có header 
 
# Lấy tín hiệu từ cột đầu tiên (giả sử dữ liệu chỉ có 1 cột) 
signal = data[0].values  # Chuyển cột đầu tiên thành mảng numpy để xử lý 
 
# Thông số của bộ lọc Notch 
notch_freq = 50.0  # Tần số nhiễu cần loại bỏ (thường là nhiễu điện lưới 50Hz) 
sample_rate = 4000  # Tần số lấy mẫu của tín hiệu, đơn vị Hz 
 
# Tính toán tần số góc w0 và hệ số alpha cho bộ lọc Notch (Không thực sự cần vì scipy đã lo) 
w0 = 2 * np.pi * notch_freq / sample_rate 
alpha = np.sin(w0) / (2 * 50)  # Giả sử hệ số Q=30, công thức gốc để tự thiết kế bộ lọc Notch 
 
# Tạo bộ lọc Notch sử dụng scipy 
b, a = iirnotch(notch_freq, 50, sample_rate)  # Tạo bộ lọc Notch, tham số 50 là hệ số Q (Q-factor càng cao lọc càng sắc) 
 
# Áp dụng bộ lọc Notch vào tín hiệu gốc 
filtered_signal = filtfilt(b, a, signal)   
# filtfilt: lọc tiến và lùi để tránh bị lệch pha 
 
# Tính toán FFT của tín hiệu gốc và tín hiệu đã lọc 
fft_signal = np.fft.fft(signal)  # FFT của tín hiệu gốc 
fft_filtered_signal = np.fft.fft(filtered_signal)  # FFT của tín hiệu đã lọc 
 
# Tính mảng tần số và biên độ tương ứng 
frequencies = np.fft.fftfreq(len(signal), d=1/sample_rate)  # Mảng tần số tương ứng với FFT 
fft_signal_magnitude = np.abs(fft_signal)  # Biên độ phổ của tín hiệu gốc 
fft_filtered_signal_magnitude = np.abs(fft_filtered_signal)  # Biên độ phổ của tín hiệu đã lọc 
 
# Vẽ đồ thị so sánh tín hiệu trước và sau lọc 
plt.figure(figsize=(10, 6))  # Tạo figure kích thước 10x6 inch 
 
# Đồ thị FFT của tín hiệu gốc 
plt.plot(frequencies[:len(frequencies)//2], fft_signal_magnitude[:len(frequencies)//2], color='red', label='Original Signal') 
 
# Đồ thị FFT của tín hiệu đã lọc 
plt.plot(frequencies[:len(frequencies)//2], fft_filtered_signal_magnitude[:len(frequencies)//2], color='blue', label='Filtered Signal') 
 
# Thiết lập tiêu đề và nhãn trục 
plt.title("FFT Comparison of Original and Filtered Signal (Notch Filter at 50Hz)")  # Tiêu đề đồ thị 
plt.xlabel("Frequency (Hz)")  # Nhãn trục x 
plt.ylabel("Magnitude")  # Nhãn trục y 
plt.legend()  # Hiển thị chú thích 
plt.grid(True)  # Bật lưới 
 
# Giới hạn tần số hiển thị từ 0Hz đến 100Hz để dễ quan sát hiệu quả lọc 50Hz 
plt.xlim(0, 100) 
 
# Hiển thị đồ thị 
plt.show() 

