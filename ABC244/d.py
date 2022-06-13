s_list = input().split()
t_list = input().split()
# print(s_list)

cnt = 0
for s, t in zip(s_list, t_list):
    if s == t:
        cnt += 1
if cnt == 3:
    print('Yes')
elif cnt == 0:
    print('Yes')
else :
    print('No')
    
"""
R G B

R G B
R B G

B G R
B R G

G B R
G R B

"""