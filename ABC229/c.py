n, w = map(int, input().split())
a_b = [list(map(int, input().split())) for _ in range(n)]
# print(n, w)
# print(a_b)
a_b.sort(reverse=True)
# print(a_b)

idx: int = 0
ans: int = 0
while w > 0 and idx < len(a_b):
    # print(idx)
    if w - a_b[idx][1] >= 0:
        ans += a_b[idx][0] * a_b[idx][1]
        w -= a_b[idx][1]
    else:
        ans += w * a_b[idx][0]
        w = 0
    idx += 1
print(ans)