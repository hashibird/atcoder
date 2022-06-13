# import copy

# new_alp = input()
# n = int(input())
# origin_all_s_list = [input() for i in range(n)]
# all_s_list = copy.copy(origin_all_s_list)
# alp_dic = {}
# origin_alp_dic = {}
# nums = [0] * n
# for i, alp in enumerate(new_alp):
#     alp_dic[alp] = chr(i + 65 + 32)
# alist = [''] * n
# for i, s_list in enumerate(all_s_list):
#     chenge_word = ''
#     for s in s_list:
#         chenge_word += alp_dic[s]
#     alist[i] = chenge_word

# copy_alist = copy.copy(alist)
# copy_alist.sort()

# for i in copy_alist:
#     print(origin_all_s_list[alist.index(i)])


def compare(s):
    res = []
    for x in s:
        res.append(order[x])
    print(res)
    return res

ne = [[1,2,3,100], [1, 2, 4], [2, 1, 1, 111], [3, 1, 1], [1, 1, 22]]
ne.sort()
print(ne)
X = input()
N = int(input())
S = [input() for _ in range(N)]

order = {}
for i, x in enumerate(X):
    order[x] = i

S.sort(key=compare)
print(*S, sep="\n")
