n, k = map(int, input().split())
k = k -1
p_list_sum = [None]*n
p_list_300 = [None]*n
checked = [0] * n
rank = n - k
for i in range(n):
    summ = sum(map(int, input().split()))
    p_list_sum[i] = summ
    p_list_300[i] = summ + 300

p_list_sum.sort(reverse=True)
# print(p_list_sum)
# print([p_list_300])

for p in p_list_300:
    if p_list_sum[k] <= p:
        print('Yes')
    else:
        print('No')
# print(p_list)

# for i in range(len(p_list)):
#     for j in range(i + 1, len(p_list)):
#         # if checked[i] >= rank:
#         #     break
#         if p_list[i][1] >= p_list[j][0]:
#             checked[i] += 1
#         if p_list[i][0] <= p_list[j][1]:
#             checked[j] += 1
#     if checked[i] >= rank:
#         print('Yes')
#     else:
#         print('No')
# print(checked)

