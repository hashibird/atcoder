n = int(input())

names = [input() for i in range(n)]

if len(names) == len(set(names)):
    print('No')
else:
    print('Yes')