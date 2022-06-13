s = input()
if len(set(list(s))) == len(list(s)):
  if s.islower():
    print('No')
  elif s.isupper():
    print('No')
  else:
    print('Yes')
  exit()
print('No')