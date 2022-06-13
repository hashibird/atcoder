import bisect
n = int(input())
int_list = [i for i in range(1, 2 * n + 2)]

cnt = 0
for _ in range(2 * n + 1):
    print(int_list[cnt])
    cnt += 1
    inp = int(input())
    if inp == 0:
        break
    a = bisect.bisect_left(int_list, inp)
    int_list.pop(a)
