def water(heights):
    if len(heights) < 3:
        return 0

    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    trapped_water = 0

    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                trapped_water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                trapped_water += right_max - heights[right]
            right -= 1

    return trapped_water
heights = list(map(int, input("Enter the heights of the brick towers: ").split()))
result = water(heights)
print("The volume of trapped water is:", result)