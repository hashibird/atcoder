n, k, a = map(int, input().split())

temp = a
lis = [0] * k
for i in range(k):
    lis[i] = temp
    temp += 1
    if temp > n:
        temp = 1
print(lis[k - 1])
