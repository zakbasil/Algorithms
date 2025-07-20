def MergeSortedArrays(arr, left, mid, right):
	numberOfElementsArr1 = mid - left + 1
	numberOfElementsArr2 = right - mid
	L = [0] * (numberOfElementsArr1)
	R = [0] * (numberOfElementsArr2)

	for i in range(0, numberOfElementsArr1):
		L[i] = arr[left + i]
 
	for j in range(0, numberOfElementsArr2):
		R[j] = arr[mid + 1 + j]
		
	i = 0
	j = 0
	k = left
	while i < numberOfElementsArr1 and j < numberOfElementsArr2: 
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < numberOfElementsArr1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < numberOfElementsArr2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr, l, r):
	if l < r:
		m = (l+r)//2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		MergeSortedArrays(arr, l, m, r)


inputList = list(map(int, input("Enter the list: ").rstrip().split(' ')))
print("Array before sort: ",inputList)
mergeSort(inputList, 0, len(inputList)-1)
print("Array after sort: ",inputList)