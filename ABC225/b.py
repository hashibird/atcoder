n = int(input())
num_list = [0] * (n+1)
for i in range(n-1):
    a, b = map(int, input().split())
    num_list[a] += 1
    num_list[b] += 1
for num in num_list:
    if num == n - 1:
        print('Yes')
        exit()
print('No')
