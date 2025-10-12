#In ra màn hình:
print("Hello, world!")

#Biến và kiểu dữ liệu:
x = 5                   # số nguyên (int)
y = 3.14                # số thực (float)
name = "Alice"          # chuỗi (str)
is_true = True          # Boolean (True/False)

#Toán tử cơ bản:
a = 10
b = 3

# Toán tử số học
print(a + b)  # cộng
print(a - b)  # trừ
print(a * b)  # nhân
print(a / b)  # chia (kết quả float)
print(a // b) # chia lấy phần nguyên
print(a % b)  # chia lấy dư
print(a ** b) # lũy thừa

# Toán tử so sánh
print(a > b)  # lớn hơn
print(a < b)  # nhỏ hơn
print(a == b) # bằng
print(a != b) # khác

# Toán tử logic
print(a > 5 and b < 5)  # AND
print(a > 5 or b > 5)   # OR
print(not(a > 5))       # NOT

#Điều kiện:
age = 18
if age >= 18:
    print("Bạn đủ tuổi.")
elif age >= 13:
    print("Bạn là thiếu niên.")
else:
    print("Bạn còn nhỏ.")

#Vòng lặp:
# Vòng lặp for
for i in range(5):  # 0,1,2,3,4
    print(i)

# Vòng lặp while
n = 0
while n < 5:
    print(n)
    n += 1

#Danh sách (list) hoặc là mảng (array):
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
fruits.append("orange") # thêm phần tử
fruits.remove("banana") # xóa phần tử
print(len(fruits))      # số lượng phần tử

#Tuple (bộ) và Set (tập hợp)
# Tuple (không thay đổi được)
colors = ("red", "green", "blue")  #Sau khi khai báo thì sẽ không thể chỉnh sửa được
print(colors[1])

# Set (không trùng lặp)
numbers = {1, 2, 3, 3}     #Phần tử 3 chỉ được lưu 1 lần
print(numbers)  # {1,2,3}

#Dictionary (từ điển) hay còn gọi là hashmap
person = {"name": "Alice", "age": 25}
print(person["name"])   # Alice
person["age"] = 26      # cập nhật
person["city"] = "HN"   # thêm key mới

#Khai báo hàm:
def greet(name):
    return "Hello, " + name

print(greet("Alice"))

#Nhập dữ liệu từ bàn phím:
name = input("Nhập tên của bạn: ")
age = int(input("Nhập tuổi: "))
print("Xin chào", name, "Bạn", age, "tuổi.")

#Thụt đầu dòng: Bắt buộc để viết các khối lệnh

if True:
    print("Đúng")

#Comment:
#Comment 1 dòng
"""
Dùng cho
nhiều dòng
"""
