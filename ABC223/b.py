s = input()
n = len(s)
s_list = [''] * n
for i in range(n):
    new_s = s[n - 1] + s[:n - 1]
    s = new_s
    s_list[i] = s
s_list.sort()
print(s_list[0], s_list[-1])


