#Import toàn bộ thư viện:
import math
print(math.sqrt(16))  # 4.0

#Import một hàm hoặc lớp (class) trong thư viện:
from math import sqrt
print(sqrt(25))  # 5.0

#Import thư viện với bí danh (sử dụng tên gọi khác để sử dụng thư viện)
import numpy as np
arr = np.array([1,2,3])
print(arr) #[1 2 3]

"""

# =========================================================================================================
#   BẢNG THƯ VIỆN PYTHON THƯỜNG DÙNG
# ========================================================================================================
# Thư viện      | Mục đích                          | Ví dụ sử dụng
# --------------------------------------------------------------------------------------------------------
# math          | Các hàm toán học                  | math.sqrt(), math.sin(), math.pi
# random        | Sinh số ngẫu nhiên                | random.randint(1,10), random.choice(list)
# datetime      | Xử lý ngày giờ                    | datetime.datetime.now(), datetime.timedelta(days=5)
# os            | Quản lý file và hệ thống          | os.listdir(), os.path.exists()
# sys           | Thông tin và tham số hệ thống     | sys.argv, sys.exit()
# re            | Xử lý biểu thức chính quy         | re.match(), re.findall()
# json          | Xử lý dữ liệu JSON                | json.load(), json.dumps()
# numpy (np)    | Toán học, mảng nhiều chiều        | np.array(), np.mean()
# pandas (pd)   | Xử lý dữ liệu dạng bảng           | pd.DataFrame(), df.head()
# matplotlib    | Vẽ đồ thị                         | plt.plot(x,y), plt.show()
# seaborn (sns) | Vẽ đồ thị nâng cao                | sns.heatmap(), sns.barplot()
# requests      | Gửi HTTP request                  | requests.get(url).text
# ----------------------------------------------------------------------------------------------------------
# Lưu ý: Cần import trước khi sử dụng, ví dụ:
# import math, random, datetime, os, sys, re, json
# import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns, requests
# ==========================================================================================================

"""

"""
CÀI ĐẶT THƯ VIỆN BẰNG PIP (ĐI CÙNG KHI CÀI ĐẶT PYTHON) NẾU CHƯA CÓ:
Mở terminal và nhập lệnh:
  pip install <tên thư viện>
Thư viện sẽ được cài đặt

"""

