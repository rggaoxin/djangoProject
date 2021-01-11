import time
from datetime import datetime

print(time.time())  # 获当前时间的时间戳
print(time.localtime())  # 获取本地时间
print(time.strftime('%Y%m%d%H%M%S', time.localtime()))  # 时间格式化
