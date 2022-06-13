import copy
n, m = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_c = sorted(list_a + list_b)
list_d = [abs(list_a[0] - list_b[0])] * (n + m)

if min(list_a) > max(list_b):
    print(min(list_a) - max(list_b))
elif min(list_b) > max(list_a):
    print(max(list_b) - max(list_a))
else:
    for i in range(1, n + m):
        list_d[i - 1] = list_c[i] - list_c[i - 1]
    copy_d = copy.copy(list_d)
    
    for i in range(len(list_d)):
        mini = copy_d.index(min(copy_d))
        id_1 = list_c[mini]
        id_2 = list_c[mini + 1]
        if id_1 in list_a and id_2 in list_b or id_2 in list_a and id_1 in list_b:
            print(min(copy_d))
            exit()
        else:
            copy_d[mini] = max(list_d)