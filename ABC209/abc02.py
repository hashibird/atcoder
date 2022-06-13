n, x = map(int, input().split())

goods = list(map(int, input().split()))



for i in range(1, len(goods), 2):
    goods[i] -= 1

if sum(goods) <= x:
    print('Yes')
else:
    print('No')