a, b, c, d, e, f, x = map(int, input().split())
ans_ax, ans_bx = x, x
ans_a,ans_b = 0, 0

while ans_ax > 0:
  for i in range(1, a+1):
    ans_ax -= 1
    ans_a += b
    if  ans_ax <= 0:
      break
  ans_ax -= c
  

while ans_bx > 0:
  for i in range(1, d+1):
    ans_bx -= 1
    ans_b += e
    if  ans_bx <= 0:
      break
  ans_bx -= f


if ans_a > ans_b:
  print('Takahashi')
elif ans_a == ans_b:
  print('Draw')
else:
  print('Aoki')
