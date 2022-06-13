n = int(input())

ans_dict = set()
point = 0
ans = 0
for i in range(n):
  s, t = input().split()
  if s in ans_dict:
    continue
  ans_dict.add(s)
  temp = int(t)
  if temp > point:
    point = temp
    ans = i + 1
print(ans)