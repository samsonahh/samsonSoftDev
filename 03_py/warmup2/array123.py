def array123(nums):
  for i in range(len(nums)-2): # -2 in case of the i+3 in line 3 causing an overflow
    if nums[i:i+3] == [1,2,3]: #If [1, 2, 3] shows up return True
      return True
  return False #Else return False

print(array123([1, 1, 2, 3, 1])) #→ True
print(array123([1, 1, 2, 4, 1])) #→ False
print(array123([1, 1, 2, 1, 2, 3])) #→ True
print(array123([1, 1, 2, 1, 2, 1])) #→ False
print(array123([1, 2, 3, 1, 2, 3])) #→ True
print(array123([1, 2, 3])) #→ True
print(array123([1, 1, 1])) #→ False
print(array123([1, 2])) #→ False
print(array123([1])) #→ False
print(array123([])) #→ False
