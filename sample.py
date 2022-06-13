# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# N, M, L = map(int, input().split())

# orders = [list(map(int, input().split())) for i in range(N)]
# p_data = [list(map(int, input().split())) for i in range(L)]



# for i in range(1, len(p_data)):
#     temp_list = []
#     for data1, data2 in zip(p_data[i - 1],p_data[i]):
#         temp_list.append(data2 - data1)
#     print(orders.index(temp_list) + 1)

# import pandas as pd
# select = []
# for week in ['monday', 'tuesday', 'wednesday', 'thursday', 'fryday', 'saturday', 'sunday']:
#     for data in range(0, 100, 5):
#         select.append({week: data})
# df = pd.DataFrame(select)
# print(df)

# import datetime
# print(datetime.date.today() + datetime.timedelta(days=10) > datetime.date.today())

import numpy as np

array = np.array([[1, 2]])

print(np.mod(array, [1, 1]))

def add(a):
    a += 10
    return a
print(list(map(add, [10, 20, 30])))

# 7 5         
# 1 2 3 4 5
# 8 9 10 11 12
# 15 16 17 18 19
# 22 23 24 25 26
# 29 30 31 32 33
# 36 37 38 39 40
# 43 44 45 46 47 48