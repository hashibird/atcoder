a, b, c, d = map(int, input().split())

a *= 1000
c *= 1000

b *= 10
d *= 10

if (a+b) <= (c+d):
    print('Takahashi')
else:
    print('Aoki')
