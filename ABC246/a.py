x_list = []
y_list = []
for i in range(3):
  x, y = map(int, input().split())
  x_list.append(x)
  y_list.append(y)

ansx = 0
ansy = 0

for x, y in zip(x_list, y_list):
  if x_list.count(x) == 1:
    ansx = x
  elif y_list.count(y) == 1:
    ansy = y
print(ansx, ansy)