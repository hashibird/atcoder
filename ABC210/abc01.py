N, A, X, Y = map(int, input().split())

ans = 0

for i in range(N):
    if i < A:
        ans += X
    else:
        ans += Y
    
print(ans)


