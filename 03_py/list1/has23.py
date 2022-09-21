def has23(nums):
  return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3 #Checks for each case for a list of 2 ints if it has a 2 or a 3

print(has23([2, 5])) # → True
print(has23([4, 3])) # → True
print(has23([4, 5])) # → False
print(has23([2, 2])) # → True
print(has23([3, 2])) # → True
print(has23([3, 3])) # → True
print(has23([7, 7])) # → False
print(has23([3, 9])) # → True
print(has23([9, 5])) # → False
