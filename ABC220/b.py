k = int(input())
a_data, b_data = input().split()
a_num = 0
b_num = 0

for i, a in enumerate(reversed(a_data)):
    a_num += int(a) * (k ** i)

for i, b in enumerate(reversed(b_data)):
    b_num += int(b) * (k ** i)

print(a_num * b_num)