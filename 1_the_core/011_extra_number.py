def solution(a, b, c):
    nums = [a, b, c]
    for i in range(3):
        if nums[i] not in nums[:i] + nums[i+1:]:
            return nums[i]