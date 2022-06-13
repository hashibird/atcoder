N, K = map(int, input().split())

nums = list(map(int, input().split()))
dic = {}

flag = True
remain = K % N

snack = K // N

for num in nums:
    dic[num] = snack

nums.sort()

while flag and remain > 0:
    for num in nums:
        dic[num] += 1
        remain -= 1
        if remain <= 0:
            flag = False
            break


for i in dic:
    print(dic[i])