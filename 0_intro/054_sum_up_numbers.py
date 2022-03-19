def solution(inputString):
    nums = ''
    for char in inputString:
        if char.isdigit():
            nums += char
        elif nums and nums[-1] != '-':
            nums += '-'
    if nums and nums[-1] == '-':
        nums = nums[:-1]
    if not nums: return 0
    return sum(map(int, nums.split('-')))