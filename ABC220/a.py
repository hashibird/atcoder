a, b, c = map(int, input().split())
num = 0
while num <= b:
    
    if num >= a:
        print(num)
        exit()
    num += c
print(-1)