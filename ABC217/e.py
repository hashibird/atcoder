import sys
input = sys.stdin.readline

Q = int(input())
query_list = [input().split() for _ in range(Q)]
ans = []
for query in query_list:
    if query[0] == '1':
        ans += [query[1]]
    elif query[0] == '2':
        print(ans[0])
        ans = ans[1:]
    else:
        ans.sort()