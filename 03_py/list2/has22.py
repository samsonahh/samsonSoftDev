def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2: #check current and next
      return True
  return False

print(has22([1, 2, 2]))#  → True
print(has22([1, 2, 1, 2]))#  → False
print(has22([2, 1, 2]))#  → False
print(has22([2, 2, 1, 2]))#  → True
print(has22([1, 3, 2]))#  → False
print(has22([1, 3, 2, 2]))#  → True
print(has22([2, 3, 2, 2]))#  → True
print(has22([4, 2, 4, 2, 2, 5]))#  → True
print(has22([1, 2]))#  → False
print(has22([2, 2]))#  → True
print(has22([2]))#  → False
print(has22([]))#  → False
print(has22([3, 3, 2, 2]))#  → True
print(has22([5, 2, 5, 2]))#  → False