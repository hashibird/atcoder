import numpy as np

n_int = int(input())
t_str = input()
ans = np.array([0, 0])
cnt = 0
muki = [[1, 0], [0, -1], [-1, 0], [0, 1]]
for t in t_str:
    if t == "S":
        ans += np.array(muki[cnt%4])
    else:
        cnt += 1
print(ans[0], ans[1])
