v, a, b, c = map(int, input().split())
family_name = ['F', 'M', 'T']
family_use = [a, b, c]
i = 0
while True:
    minus = family_use[i % 3]
    v -= minus
    # print(v)
    if(v < 0):
        break
    i += 1

print(family_name[i % 3])