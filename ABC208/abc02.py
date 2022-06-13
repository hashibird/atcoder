import math
P = int(input())

ans = 0
temp = 0
for i in range(10, 0, -1):
    if math.factorial(i) <= P:
        while temp + math.factorial(i) <= P:
            temp += math.factorial(i)
            ans += 1

print(ans)

