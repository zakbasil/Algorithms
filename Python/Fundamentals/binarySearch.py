def binarySearchWithLoops(arr, searchElement): #[1 2 3 4 5] x = 4
	start = 0 
	end = len(arr) - 1 
	count = 0
	while start <= end:
		count += 1
		mid = (start + end) // 2 
		if arr[mid] == searchElement:
			break
		elif arr[mid] < searchElement:
			start = mid + 1
		else:
			end = mid - 1
	if start > end:
		return(-1)
	return(count)

result = binarySearchWithLoops(range(101), 67)
print(result)
result = binarySearchWithLoops(range(101), 32)
print(result)
result = binarySearchWithLoops(range(101), 37)
print(result)
result = binarySearchWithLoops(range(101), 47)
print(result)
