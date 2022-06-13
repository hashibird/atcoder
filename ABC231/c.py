
n, q = map(int, input().split())
a_list = list(map(int, input().split()))
x_list = [int(input()) for _ in range(q)]
cnt_list = [0] * q
cnt = 0
a_list.sort(reverse=True)
for x in x_list:
    s = 0
    e = len(a_list) - 1
    while True:
        half = (e + s) // 2
        if a_list[half] == x:
            cnt_list[cnt] += half + 1
            break
        elif a_list[half] > x:
            s = half + 1
        else:
            e = half - 1
        if e < s:
            cnt_list[cnt] += s
            break
    cnt += 1
    
for i in cnt_list:
    print(i)