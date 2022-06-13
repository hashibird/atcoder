from typing import final


n = int(input())

p_list = list(map(int, input().split()))
print(p_list)
ans = [''] * n
for i, p in enumerate(p_list):
    ans[p - 1] = str(i + 1)

print(' '.join(ans))