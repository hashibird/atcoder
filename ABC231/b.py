import collections
n = int(input())
s = [input() for _ in range(n)]

s = dict(collections.Counter(s))

cnt = 0
name = ""
for i in s:
    if cnt < s[i]:
        name = i
        cnt = s[i]
print(name)