import numpy as np

y, x, n = map(int, input().split())

lists = [list(map(int, input().split())) for i in range(n)]

# print(y, x, n)

# print(lists)

cards = [[0 for i in range(x)] for i in range(y)]
cards_cp = []
dele_y = []
dele_x = []

for i, t_list in enumerate(lists):
    cards[t_list[0] - 1][t_list[1] - 1] = i + 1

for i, card in enumerate(cards):
    if sum(card) == 0:
        dele_y.append(i)

for i, card in enumerate(cards):
    if i in dele_y:
        continue
    cards_cp.append(card)

arrays = np.sum(cards_cp, axis=0)

# print(cards_cp)
# print(arrays)
dele = []
for i, arr in enumerate(arrays):
    if arr == 0:
        dele.append(i)

cards_cp = np.delete(cards_cp, dele, 1)

for i in range(1, n + 1):
    for id in np.argwhere(cards_cp==i):
        print(id[0] + 1, id[1] + 1)