n = int(input())

lists = list(map(int, input().split()))


print(lists.index(sorted(lists)[-2]) + 1)