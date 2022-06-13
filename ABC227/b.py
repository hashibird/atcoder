n = int(input())
s = list(map(int, input().split()))
ans = 0
flg = 0
for s_ in s:
    for i in range(1, 1000):
        for j in range(1, 1000):
            calc = 4 * i * j + 3 * i + 3 * j
            if calc == s_:
                flg = 1
                break
            if calc >= s_:
                break
        if flg == 1:
            break
    if flg == 0:
        ans += 1
    flg = 0
# print(4 * i * j + 3 * i + 3 * j)
print(ans)