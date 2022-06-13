n = int(input())
h_i = list(map(int, input().split()))
ans = h_i[0]

for h in h_i[1:]:
    if ans < h:
        ans = h
    else:
        break
print(ans)