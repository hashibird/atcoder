N, K = map(int, input().split())

C_LIST = list(map(int, input().split()))

temp = C_LIST[0:K]
ans = len(set(temp))

cnt = 0
for i in range(K, N):
    if cnt == K:
        cnt = 0
    temp[cnt] = C_LIST[i]
    len_t = len(set(temp))
    cnt += 1
    if len_t > ans:
        ans = len_t

print(ans)



# n, k = map(int,input().split())

# C = list(map(int, input().split()))

# color = {}

# for i in range(n):
#     color.setdefault(C[i], 0)

# tmp = 0
# for i in range(k):
#     if color[C[i]] == 0:
#         tmp += 1
#     color[C[i]] += 1

# ans = tmp
# for i in range(n-k):
#     if color[C[i]] == 1:
#         tmp -= 1
#     color[C[i]] -= 1
#     if color[C[i+k]] == 0:
#         tmp += 1
#     color[C[i+k]] += 1
#     ans = max(ans, tmp)

# print(ans)