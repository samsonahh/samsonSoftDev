def rotate_left3(nums):
    return nums[1:] + [nums[0]] #Takes the sublist without the first and adds the first to the end

print(rotate_left3([1, 2, 3]) ) # → [2, 3, 1]
print(rotate_left3([5, 11, 9]) ) # → [11, 9, 5]
print(rotate_left3([7, 0, 0]) ) # → [0, 0, 7]
print(rotate_left3([1, 2, 1]) ) # → [2, 1, 1]
print(rotate_left3([0, 0, 1]) ) # → [0, 1, 0]
