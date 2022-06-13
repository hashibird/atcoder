
import itertools

s = input()


all = itertools.permutations(s, 3)
print(len(set(all)))