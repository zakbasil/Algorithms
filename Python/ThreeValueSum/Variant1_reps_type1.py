nums = list(map(int, input().split()))
target = int(input())
nums.sort()
for i in range(len(nums)):
    left, right = i, len(nums) - 1 
    while (left <= right):
        sum = nums[i] + nums[left] + nums[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            print("true")
            exit(0)
print("False")