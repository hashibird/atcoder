x1, y1, x2, y2 = map(int, input().split())

absx = abs(x2 - x1)
absy = abs(y2 - y1)
if(absx >= 5):
    print('No')
elif(absx == 0 and (absy == 0 or absy == 2 or absy == 4)):
    print('Yes')
elif(absx == 1 and (absy == 1 or absy == 3)):
    print('Yes')
elif(absx == 2 and (absy == 0 or absy == 4)):
    print('Yes')
elif(absx == 3 and (absy == 1 or absy == 3)):
    print('Yes')
elif(absx == 4 and (absy == 0 or absy == 2)):
    print('Yes')
else:
    print('No')