def sum2(nums):
  if len(nums) == 0: #Accounts for empty list
    return 0
  if len(nums) == 1: #Accounts for a list with 1 entry
    return nums[0]
  return nums[0]+nums[1] #Just adds first and the next

print(sum2([1, 2, 3])) # → 3
print(sum2([1, 1])) # → 2
print(sum2([1, 1, 1, 1])) # → 2
print(sum2([1, 2])) # → 3
print(sum2([1])) # → 1
print(sum2([])) # → 0
print(sum2([4, 5, 6])) # → 9
print(sum2([4])) # → 4
