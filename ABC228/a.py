s, t, x = map(int, input().split())
x += 0.5
if s <= t:
    if s <= x and x <= t:
        print('Yes')
    else:
        print('No')
else:
    if s <= x and x <= 24 or 0 <= x and x <= t:
        print('Yes')
    else:
        print('No')