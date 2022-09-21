def string_match(a, b):
  counter = 0 #Counter will be slowly added to and will be returned as final answer
  length = 0 #Length of the shorter string we will be working with
  short = "" #the short string
  long = "" #the long string
  if len(a) > len(b): #Lines 6-13 check and fill length, short, and long
    length = len(b)
    short = b
    long = a
  else:
    length = len(a)
    short = a
    long = b
  if length < 2: #No strings can match if the longest string has a length of 1 or 0
    return 0
  for i in range(length - 1): #We use the shortest string to avoid extra characters that the longer string will have
    if short[i:i+2] == long[i:i+2]: #Checks the frequency of equal pairs in both the strings
      counter+=1
  return counter

print(string_match('xxcaazz', 'xxbaaz')) #→ 3
print(string_match('abc', 'abc')) #→ 2
print(string_match('abc', 'axc')) #→ 0
print(string_match('hello', 'he')) #→ 1
print(string_match('he', 'hello')) #→ 1
print(string_match('h', 'hello')) #→ 0
print(string_match('', 'hello')) #→ 0
print(string_match('aabbccdd', 'abbbxxd')) #→ 1
print(string_match('aaxxaaxx', 'iaxxai')) #→ 3
print(string_match('iaxxai', 'aaxxaaxx')) #→ 3
