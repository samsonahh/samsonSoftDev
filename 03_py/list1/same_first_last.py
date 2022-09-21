def same_first_last(nums):
  #Logical one liner. Does check for empty lists
  return len(nums) >= 1 and nums[0] == nums[-1]

print(same_first_last([1, 2, 3])) # → False
print(same_first_last([1, 2, 3, 1])) # → True
print(same_first_last([1, 2, 1])) # → True
print(same_first_last([7])) # → True
print(same_first_last([])) # → False
print(same_first_last([1, 2, 3, 4, 5, 1])) # → True
print(same_first_last([1, 2, 3, 4, 5, 13])) # → False
print(same_first_last([13, 2, 3, 4, 5, 13])) # → True
print(same_first_last([7, 7])) # → True
