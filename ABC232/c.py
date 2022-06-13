n, m = map(int, input().split())
a_b = [list(map(int, input().split())) for _ in range(m)]
c_d = [list(map(int, input().split())) for _ in range(m)]

a_b_cnt = [0] * (n)
c_d_cnt = [0] * (n)

for a, b in a_b:
    a_b_cnt[a-1] += 1
    a_b_cnt[b-1] += 1

for c, d in c_d:
    c_d_cnt[c-1] += 1
    c_d_cnt[d-1] += 1

print(a_b_cnt)
print(c_d_cnt)

if a_b_cnt == c_d_cnt:
    print('Yes')
    exit()
print('No')