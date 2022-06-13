n = int(input())

x_y_list = [list(map(int, input().split())) for i in range(n)]
s_list = list(input())

dict = {}

for i, x_y in enumerate(x_y_list):
    if x_y[1] in dict.keys():
        dict[x_y[1]] += [[x_y[0], s_list[i]]] 
    else:
        dict[x_y[1]] = [[x_y[0], s_list[i]]]

for d in dict.keys():
    if len(dict[d]) >= 2:
        r_list = []
        l_list = []
        for x_s_list in dict[d]:
            if(x_s_list[1] == 'R'):
                r_list += [x_s_list[0]]
            else:
                l_list += [x_s_list[0]]
        if len(r_list) == 0 or len(l_list) == 0:
            continue
        r_list.sort
        l_list.sort
        
        for x_s_list in dict[d]:
            print(dict)
            if(x_s_list[1] == 'R'):
                if l_list[-1] >= x_s_list[0]:
                    print('Yes')
                    exit()
            else:
                if(r_list[0] <= x_s_list[0]):
                    print('Yes')
                    exit()
                    
print('No')