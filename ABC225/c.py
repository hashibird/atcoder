n, m = map(int, input().split())
b_list = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    for j in range(m - 1):
        temp = (b_list[i][j] - 1) % 7
        if temp > (b_list[i][j + 1] - 1) % 7:
            print('No')
            exit()
        if b_list[i][j] + 1 != b_list[i][j + 1]:
            print('No')
            exit()
        
    if i < n - 1 and b_list[i][0] + 7 != b_list[i + 1][0]:
        print('No')
        exit()
print('Yes')
