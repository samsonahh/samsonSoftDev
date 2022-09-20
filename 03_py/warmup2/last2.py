def last2(str):
  last2 = str[-2:]
  counter = 0
  for c in range(len(str)-2):
    if str[c:c+2] == last2:
      counter+=1
  return counter
