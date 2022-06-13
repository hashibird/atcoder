n = int(input())

s_t_list = []
double_list = []

for _ in range(n):
    s_t = input().split()
    s_t_list.append(s_t)
    double_list.append(s_t[0])
    if s_t[0] != s_t[1]:
      double_list.append(s_t[1])

for s, t in s_t_list:
  if double_list.count(s) >= 2 and double_list.count(t) >= 2:
    print('No')
    exit()
print('Yes')