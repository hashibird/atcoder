h, w = map(int, input().split())
double = [[(i, j) for j in range(1, w+1)] for i in range(1, h+1)]
y, x = map(int, input().split())


ans = 0

query = double[y-1][x-1]

if query[1] + 1 <= w:
  ans += 1
if query[0] + 1 <= h:
  ans += 1
if query[1] - 1 >= 1:
  ans += 1
if query[0] -1 >= 1:
  ans += 1

print(ans)