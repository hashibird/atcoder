def minus1(num):
    return num - 1

n, x = map(int, input().split())
a_friends = list(map(int, input().split()))
a_friends = list(map(minus1, a_friends))
friends_know = [False] * n
next_friend = x - 1

ans = 0
while friends_know[next_friend] == False:
    # print(friends_know)
    friends_know[next_friend] = True
    next_friend = a_friends[next_friend]
    ans += 1
    
print(ans)