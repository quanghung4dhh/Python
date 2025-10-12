import numpy as np                    # Thư viện numpy để xử lý các phép toán mảng và tính toán FFT 
import pandas as pd                  # Thư viện pandas để đọc file CSV 
import matplotlib.pyplot as plt      # Thư viện matplotlib để vẽ đồ thị 
 
# Đọc tín hiệu đã lọc từ file CSV vào dataframe (dữ liệu có thể là tín hiệu sau khi lọc) 
file_path = "D:/Esp-idf/Mysource/inmp441_test/data_text/Filter_test/filter_white_noise_test_2nd.csv" 
data = pd.read_csv(file_path, header=None)  # Đọc dữ liệu từ file CSV, không có header 
 
# Lấy tín hiệu từ cột đầu tiên của dataframe (giả sử tín hiệu nằm trong cột đầu tiên) 
signal = data[0].values  # Chuyển dữ liệu cột đầu tiên thành mảng numpy 
 
# Tính toán FFT của tín hiệu 
fft_signal = np.fft.fft(signal)  # Áp dụng phép biến đổi Fourier nhanh (FFT) lên tín hiệu 
frequencies = np.fft.fftfreq(len(signal), d=1/4000)  # Tính tần số tương ứng (sample rate là 4000Hz) 
 
# Lọc phần thực và phần ảo của FFT để lấy biên độ của tín hiệu 
fft_magnitude = np.abs(fft_signal)  # Biên độ (magnitude) của FFT, sử dụng giá trị tuyệt đối 
 
# Vẽ đồ thị FFT (chỉ vẽ nửa đầu của phổ tần số vì phổ là đối xứng) 
plt.plot(frequencies[:len(frequencies)//2], fft_magnitude[:len(frequencies)//2])  # Vẽ nửa đầu của tần số và biên độ 
plt.title("FFT of Filtered Signal")  # Tiêu đề của đồ thị 
plt.xlabel("Frequency (Hz)")  # Nhãn trục x: Tần số 
plt.ylabel("Biên độ")  # Nhãn trục y: Biên độ (magnitude) 
plt.grid(True)  # Bật lưới để dễ quan sát 
plt.show()  # Hiển thị đồ thị
