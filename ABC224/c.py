import itertools
import numpy as np
import warnings
warnings.simplefilter('ignore', category=RuntimeWarning)

def mid_point(pos):
    s_l = sorted(pos, key=sum)
    a = [pos.index(s_l[0]), pos.index(s_l[1]), pos.index(s_l[2])]
    return a

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
# xy = [[0 ,1],
# [0, -1],
# [0,2]]
all = itertools.combinations(xy, 3)
cnt = 0
for xy_list in all:
    top_mid_bottom = mid_point(xy_list)
    array1 = np.abs(np.array(xy_list[top_mid_bottom[0]]) - xy_list[top_mid_bottom[1]])
    array2 = np.abs(np.array(xy_list[top_mid_bottom[2]]) - xy_list[top_mid_bottom[1]])
    temp = (array1) / (array2)
    if not (temp[0] == temp[1]) and not (array1[0] == 0 and array2[0] == 0) and not(array1[1] == 0 and array2[1] == 0):
        # print(xy_list)
        cnt += 1
    else:
        # print('NOOOOO    ', xy_list)
        pass
print(cnt)

