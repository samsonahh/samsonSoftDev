def sum67(nums):
  if len(nums) == 0:
    return 0
  answer = 0
  shouldcount = True 
  for i in nums:
    if i == 6 and shouldcount: #stop counting at 6
      shouldcount = not shouldcount
    if shouldcount:
      answer+=i
    if i == 7 and not shouldcount: #start counting at 7
      shouldcount = not shouldcount
  return answer

print(sum67([1, 2, 2]))#  → 5	
print(sum67([1, 2, 2, 6, 99, 99, 7]))#  → 5	
print(sum67([1, 1, 6, 7, 2]))#  → 4	
print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))#  → 2	
print(sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]))#  → 2	
print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))#  → 18	
print(sum67([2, 7, 6, 2, 6, 2, 7]))#  → 9	
print(sum67([1, 6, 7, 7]))#  → 8	
print(sum67([6, 7, 1, 6, 7, 7]))#  → 8	
print(sum67([6, 8, 1, 6, 7]))#  → 0	
print(sum67([]))#  → 0	
print(sum67([6, 7, 11]))#  → 11	
print(sum67([11, 6, 7, 11]))#  → 22	
print(sum67([2, 2, 6, 7, 7]))#  → 11