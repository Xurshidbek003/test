import bisect
nums = [i for i in range(1, 100001)]
target = int(input())
print(bisect.bisect_left(nums, target))

# left = 0
# right = len(nums)-1
# while left<right:
#     mid = (left+right)//2
#     if nums[mid]>target:
#         right = mid - 1
#     else: left = mid
#
# print(left)