
nums = [9,2,3,1,4,5,6,1,7]

def get_up(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups
    
print(get_up(nums))
