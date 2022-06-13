l, q = map(int, input().split())
q_list = [tuple(map(int, input().split())) for i in range(q)]
str_l = []

for i in range(1, l + 1):
    str_l += [str(i)]

ans_list = [['']]
ans_list[0] = list(str_l)
for c, x in q_list:
    if c ==  1:
        for item in ans_list:
            if str(x) in item:
                break
        ans_list.append(item[item.index(str(x)) + 1:])
        ans_list[ans_list.index(item)] = item[:item.index(str(x)) + 1]
    else:
        for item in ans_list:
            if str(x) in item:
                print(len(item))