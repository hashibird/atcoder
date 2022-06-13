N, P = map(int, input().split())

a_list = list(map(int, input().split()))
ans = 0
for a in a_list:
    if(a < P):
        ans += 1

print(ans)