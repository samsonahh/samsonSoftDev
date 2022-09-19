def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20) and hour >= 0 and hour < 24
