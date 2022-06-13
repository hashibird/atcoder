n = int(input())
a_dict = {}
b_dict = {}
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ans1 = 0
ans2 = 0
for i, a in enumerate(a_list):
    a_dict[a] = i

for i, b in enumerate(b_list):
    if b in a_dict.keys():
        ans2 += 1
        if a_dict[b] == i:
            ans1 += 1
            ans2 -= 1
print(ans1)
print(ans2)