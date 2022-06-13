n, k, x = map(int, input().split())

a_list = list(map(int,input().split()))
a_list.sort(reverse=True)
for i in range(n):
  if a_list[i] // x <= k:
    k -= a_list[i] // x
    a_list[i] = max(a_list[i] - (a_list[i] // x) * x, 0)

a_list.sort(reverse=True)


if a_list[0] > x and k >= 1:
  a_list[0] -= k * x
  k = 0

for i in range(n):
  if k == 0:
    break
  a_list[i] = max(a_list[i] - x, 0)
  k -= 1
  

print(sum(a_list))