
n = int(input())
queries = [list(map(int, input().split())) for _ in range(n)]

ball = []
start = 0

for query in queries:
  if query[0] == 1:
    ball += [[query[1], query[2]]]
  else:
    ans = 0
    for i in range(start, len(ball)):
      if ball[i][1] > query[1]:
        ans += query[1] * ball[i][0]
        ball[i][1] -= query[1]
        break
      elif ball[i][1] <= query[1]:
        ans += ball[i][1] * ball[i][0]
        query[1] -= ball[i][1]
        start += 1
    print(ans)
# print(ball)
