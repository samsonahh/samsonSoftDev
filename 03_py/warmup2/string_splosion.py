def string_splosion(str):
  answer = ""
  for index in range(len(str)+1):
    answer+=str[0:index]
  return answer
