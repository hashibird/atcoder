x = input()
check = 0

if len(set(x)) == 1:
    print('Weak')
    exit()

else:
    for i in range(1, 4):
        if str(int(x[i - 1]) + 1) == x[i]:
            check += 1
        elif x[i - 1] == '9' and x[i] == '0':
            check += 1

if check == 3:
    print('Weak')
else:
    print('Strong')