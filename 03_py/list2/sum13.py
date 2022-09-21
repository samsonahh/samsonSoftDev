def sum13(nums):
  if len(nums) == 0: #edge cases 
    return 0
  pos = 0
  answer = 0
  while pos < len(nums):
    if(nums[pos] == 13):
      pos+=2 #skip the current and the next
    else:
      answer+= nums[pos]
      pos+=1
  return answer


print(sum13([1, 2, 2, 1])) #→ 6	
print(sum13([1, 1])) #→ 2	
print(sum13([1, 2, 2, 1, 13])) #→ 6	
print(sum13([1, 2, 13, 2, 1, 13])) #→ 4	
print(sum13([13, 1, 2, 13, 2, 1, 13])) #→ 3	
print(sum13([])) #→ 0	
print(sum13([13])) #→ 0	
print(sum13([13, 13])) #→ 0	
print(sum13([13, 0, 13])) #→ 0	
print(sum13([13, 1, 13])) #→ 0	
print(sum13([5, 7, 2])) #→ 14	
print(sum13([5, 13, 2])) #→ 5	
print(sum13([0])) #→ 0	
print(sum13([13, 0])) #→ 0