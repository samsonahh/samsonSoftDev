def string_splosion(str):
  answer = "" #Empty answer to be filled
  for index in range(len(str)+1): #Loops through and takes index
    answer+=str[0:index] #Takes substring from the front to an increasing end index
  return answer

print(string_splosion('Code')) #→ 'CCoCodCode'
print(string_splosion('abc')) #→ 'aababc'
print(string_splosion('ab')) #→ 'aab'
print(string_splosion('x')) #→ 'x'
print(string_splosion('fade')) #→ 'ffafadfade'
print(string_splosion('There')) #→ 'TThTheTherThere'
print(string_splosion('Kitten')) #→ 'KKiKitKittKitteKitten'
print(string_splosion('Bye')) #→ 'BByBye'
print(string_splosion('Good')) #→ 'GGoGooGood'
print(string_splosion('Bad')) #→ 'BBaBad'
