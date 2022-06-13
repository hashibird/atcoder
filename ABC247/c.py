num = '1'

n = int(input())
for i in range(1, n):
  num = num + "/" + str(i + 1) + "/" +num


print(" ".join(num.split('/')))