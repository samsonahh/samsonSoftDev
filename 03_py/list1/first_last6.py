def first_last6(nums):
  #nums[-1] returns the number in the last index
  return nums[0] == 6 or nums[-1] == 6

print(first_last6([1, 2, 6])) #→  True
print(first_last6([6, 1, 2, 3])) #→  True
print(first_last6([13, 6, 1, 2, 3])) #→  False
print(first_last6([13, 6, 1, 2, 6])) #→  True
print(first_last6([3, 2, 1])) #→  False
print(first_last6([3, 6, 1])) #→  False
print(first_last6([3, 6])) #→  True
print(first_last6([6])) #→  True
print(first_last6([3])) #→  False
print(first_last6([5, 6])) #→  True
print(first_last6([5, 5])) #→  False
print(first_last6([1, 2, 3, 4, 6])) #→  True
print(first_last6([1, 2, 3, 4])) #→  False
