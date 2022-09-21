def centered_average(nums):
  total = 0
  for i in nums:
    total+=i
  return (total - min(nums) - max(nums))/(len(nums)-2)

print(centered_average([1, 2, 3, 4, 100])) #→ 3	
print(centered_average([1, 1, 5, 5, 10, 8, 7])) #→ 5	
print(centered_average([-10, -4, -2, -4, -2, 0])) #→ -3	
print(centered_average([5, 3, 4, 6, 2])) #→ 4	
print(centered_average([5, 3, 4, 0, 100])) #→ 4	
print(centered_average([100, 0, 5, 3, 4])) #→ 4	
print(centered_average([4, 0, 100])) #→ 4	
print(centered_average([0, 2, 3, 4, 100])) #→ 3	
print(centered_average([1, 1, 100])) #→ 1	
print(centered_average([7, 7, 7])) #→ 7	
print(centered_average([1, 7, 8])) #→ 7	
print(centered_average([1, 1, 99, 99])) #→ 50	
print(centered_average([1000, 0, 1, 99])) #→ 50	
print(centered_average([4, 4, 4, 4, 5])) #→ 4	
print(centered_average([4, 4, 4, 1, 5])) #→ 4	
print(centered_average([6, 4, 8, 12, 3])) #→ 6