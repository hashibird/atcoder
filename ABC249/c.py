import itertools
import pprint

n, k = map(int, input().split())
s_list = [input() for i in range(n)]

alp = [chr(i+32) for i in range(65, 91)]
dp = [[0 for _ in range(26)] for i in range(n)]
print(alp)
pprint.pprint(dp)

a = [i for i in range(1, n)]
all = itertools.combinations(a, k)

for i in all:
  print(i)
print(len(list(all)))