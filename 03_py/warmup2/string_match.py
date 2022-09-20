def string_match(a, b):
  counter = 0
  length = 0
  short = ""
  long = ""
  if len(a) > len(b):
    length = len(b)
    short = b
    long = a
  else:
    length = len(a)
    short = a
    long = b
  if length < 2:
    return 0
  for i in range(length - 1):
    if short[i:i+2] == long[i:i+2]:
      counter+=1
  return counter
