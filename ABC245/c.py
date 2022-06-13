


n, k = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# for i in range(n - 1):
#     a_list[i] = a_list[i + 1] - a_list[i]
#     b_list[i] = b_list[i + 1] - b_list[i]

one_list = [False for i in range(n)]
two_list = [False for i in range(n)]
one_list[0] = True
two_list[0] = True

for i in range(n - 1):
    if abs(a_list[i + 1] - a_list[i]) <= k and one_list[i] or abs(a_list[i + 1] - b_list[i]) <= k and two_list[i]:
        one_list[i + 1] = True
    if abs(b_list[i + 1] - a_list[i]) <= k and one_list[i] or abs(b_list[i + 1] - b_list[i]) <= k and two_list[i]:
        two_list[i + 1] = True
        
if one_list[-1] == True or two_list[-1] == True:
    print('Yes')
else:
    print('No')