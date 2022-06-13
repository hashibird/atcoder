from bisect import bisect_left, bisect_right


n = int(input())
a_list = list(map(int, input().split()))
nums = [[] for i in range(n+1)]

for i, a in enumerate(a_list):
  nums[a] += [i + 1]

q = int(input())
for i in range(q):
  l, r, x = map(int, input().split())
  print(max(0, bisect_right(nums[x], r) - bisect_left(nums[x], l)))