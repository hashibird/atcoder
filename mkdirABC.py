import os

abc = ['a.py', 'b.py', 'c.py']
numdir = '/Users/hashi000/projects/py_ts_pj/atcode/pythonABC/abc_num.txt'

with open(numdir, 'r') as fr:
    num = int(fr.readline())

makedir = f'/Users/hashi000/projects/py_ts_pj/atcode/pythonABC/ABC{num}'
print(makedir)
os.mkdir(makedir)

for alp in abc:
    makefile = f'{makedir}/{alp}'
    with open(makefile, 'w'):
        pass

with open(numdir, 'w') as fw:
    fw.write(str(num + 1))