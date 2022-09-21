def max_end3(nums):
  if nums[0] > nums[-1]: #If first > last
    return [nums[0]]*3 #Can multiply lists!
  return [nums[-1]]*3

print(max_end3([1, 2, 3])) #→ [3, 3, 3]
print(max_end3([11, 5, 9])) #→ [11, 11, 11]
print(max_end3([2, 11, 3])) #→ [3, 3, 3]
print(max_end3([11, 3, 3])) #→ [11, 11, 11]
print(max_end3([3, 11, 11])) #→ [11, 11, 11]
print(max_end3([2, 2, 2])) #→ [2, 2, 2]
print(max_end3([2, 11, 2])) #→ [2, 2, 2]
print(max_end3([0, 0, 1])) #→ [1, 1, 1]
