
import pandas as pd  # Thư viện pandas để đọc file CSV 
import matplotlib.pyplot as plt  # Thư viện matplotlib để vẽ biểu đồ 
 
# Đọc dữ liệu từ file CSV vào biến data_fame (dataframe của pandas) 
data_fame = pd.read_csv("D:/Esp-idf/Mysource/sph0645_test/data_text/data_test400Hz_3rd.csv") 
 
# Tạo trục x là các chỉ số từ 0 đến số lượng dòng của data_fame 
x = range(len(data_fame))  # x là dãy số thứ tự các mẫu 
 
# Vẽ biểu đồ với marker là "x" (dấu x nhỏ ở mỗi điểm) và đường nối giữa các điểm 
plt.plot(x, data_fame, marker="x", linestyle='-') 
 
# Thiết lập nhãn cho trục x 
plt.xlabel('Chỉ số dòng')  # Ghi chú trục x là "Chỉ số dòng" 
 
# Thiết lập nhãn cho trục y 
plt.ylabel('Biên độ')  # Ghi chú trục y là "Biên độ" 
 
# Đặt tiêu đề cho biểu đồ 
plt.title('Biểu đồ dữ liệu từ file CSV') 
 
# Hiển thị biểu đồ ra màn hình 
plt.show() 

