import numpy as np

x, y = map(int, input().split())

a=np.array([0,0])
b=np.array([x,y])
distance=np.linalg.norm(b-a)
print(x / distance, y / distance)