a, b = input().split()
a = list(reversed(a))
b = list(reversed(b))

for i in range(min(len(a), len(b))):
    temp = int(a[i]) + int(b[i])
    if temp >= 10:
        print('Hard')
        exit()

print('Easy')