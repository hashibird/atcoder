n = int(input())
a_list = list(map(int, input().split()))
x = int(input())

if sum(a_list) > x:
    temp = 0
    for i, a in enumerate(a_list, start=1):
        temp += a
        if x < temp:
            print(i)
            exit()
else:
    cnt = x // sum(a_list) * n
    temp = sum(a_list) * (x // sum(a_list))
    for a in a_list:
        temp += a
        cnt += 1
        if temp > x:
            print(cnt)
            exit()
