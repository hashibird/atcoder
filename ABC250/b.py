from pprint import pprint


n, a, b = map(int, input().split())
double = [["." for _ in range(n * b)] for _ in range(n * a)]
flg_i = False

for i in range(n * a):
  skip = 0
  if i % a == 0:
    flg_i = not flg_i
  flg_j = False
  if flg_i:
    skip = b
  for j in range(skip, n * b):
    if j % b == 0:
      flg_j = not flg_j
    if flg_j:
      double[i][j] = "#"

for i in range(n * a):
  for j in range(n * b):
    print(double[i][j], end="")
  print()