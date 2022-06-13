n = int(input())
ans = 0
for a in range(1, n + 1):
    if a * a * n n:
        break
    for b in range(a , n + 1):
        if a * b ** 2 > n:
            break
        for c in range(b, n + 1):
            if a * b * c <= n:
                ans += 1
            if a * b * c > n:
                break
print(ans)