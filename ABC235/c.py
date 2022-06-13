from collections import defaultdict

n, q = map(int, input().split())
a_n = list(map(int, input().split()))
x_k_q = [tuple(map(int, input().split())) for _ in range(q)]
dic = {}

m = defaultdict(list)


for i in range(n):
    m[a_n[i]].append(i + 1)

print(m)
# for i, a in enumerate(a_n):
#     dic[a] = []
    
# for i in range(len(a_n)):
#     a = a_n[i]
#     a_n[i] = (a, dic[a])
#     dic[a] += 1

# for x_k in x_k_q:
#     if x_k in a_n:
#         print(a_n.index(x_k) + 1)
#     else:
#         print(-1)
