def array_front9(nums):
  if len(nums) >= 4: #If array is at most than 4
    for i in nums[0:4]:
      if i == 9:
        return True #If one of those 4 are equal to 9 then True
  else: #If array is larger than 4
    for i in nums:
      if i == 9: #If any are equal to 9 return True
        return True
  return False #Else False

print(array_front9([1, 2, 9, 3, 4])) #→ True
print(array_front9([1, 2, 3, 4, 9])) #→ False
print(array_front9([1, 2, 3, 4, 5])) #→ False
print(array_front9([9, 2, 3])) #→ True
print(array_front9([1, 9, 9])) #→ True
print(array_front9([1, 2, 3])) #→ False
print(array_front9([1, 9])) #→ True
print(array_front9([5, 5])) #→ False
print(array_front9([2])) #→ False
print(array_front9([9])) #→ True
print(array_front9([])) #→ False
print(array_front9([3, 9, 2, 3, 3])) #→ True
