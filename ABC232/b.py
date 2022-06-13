s_inp = input()
t_inp = input()

alp = [chr(i+32) for i in range(65, 91)]
alp += alp
values = []
for s, t in zip(s_inp, t_inp):
    values.append(alp[alp.index(s):].index(t))
    if(values[0] != values[-1]):
        print('No')
        exit()
print('Yes')