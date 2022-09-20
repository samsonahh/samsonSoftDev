def string_bits(str):
  answer = ""
  counter = 0
  for c in str:
    if counter%2 == 0:
      answer+=c
    counter+=1
  return answer
