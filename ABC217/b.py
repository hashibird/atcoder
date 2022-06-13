s = ['ABC' , 'ARC' , 'AGC' , 'AHC']
inp_s = [input() for _ in range(3)]
for i in inp_s:
    s.remove(i)

print(s[0])