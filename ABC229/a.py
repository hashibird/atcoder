s = [input().split() for i in range(2)]


# print(s)
if s == [[".#"],
        ["#."]]:
        print('No')
elif s == [["#."],
            [".#"]]:
        print('No')
else:
    print('Yes')
