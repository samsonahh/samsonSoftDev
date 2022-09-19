def not_string(str):
  firstthree = str[0:3]
  if not firstthree == "not":
    return "not " + str
  else:
    return str
