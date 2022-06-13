s_list = input()
t_list = input()
if s_list == t_list:
    print('Yes')
    exit()
else:
    for i in range(len(s_list) - 1):
        if s_list[:i] + s_list[i + 1] + s_list[i] + s_list[i + 2:] == t_list:
            
            print('Yes')
            exit()
print('No')