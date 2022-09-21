def array_count9(nums):
  counter = 0
  for i in nums:
    if i == 9: #If the number is 9 then increase the counter
      counter+=1
  return counter

print(array_count9([1, 2, 9])) # → 1
print(array_count9([1, 9, 9])) # → 2
print(array_count9([1, 9, 9, 3, 9])) # → 3
print(array_count9([1, 2, 3])) # → 0
print(array_count9([])) # → 0
print(array_count9([4, 2, 4, 3, 1])) # → 0
print(array_count9([9, 2, 4, 3, 1])) # → 1
