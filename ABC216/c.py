n = int(input())
ans = ''
while n >= 1:
    if n % 2 == 1:
        n -= 1
        ans += 'A'
    else:
        n //= 2
        ans += 'B'
    # print(n)
print(ans[::-1])

# num = 0
# for a in ans[::-1]:
#     if a == 'A':
#         num += 1
#     else:
#         num *= 2
# print(num)