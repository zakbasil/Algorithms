def merge(arr, l, m, r):#[56,32,145,13,13], l=0, r=0, m=1
	n1 = m - l + 1 #[56]
	n2 = r - m     #[32]
	L = [0] * (n1) #[0]
	R = [0] * (n2) #[0]

	for i in range(0, n1):
		L[i] = arr[l + i] #L = [56]
 
	for j in range(0, n2):
		R[j] = arr[m + 1 + j] #R = [32]
		
	i = 0 #1
	j = 0 #1
	k = l #2
	while i < n1 and j < n2: 
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr, l, r): #[56,32,145,63,13], l=0, r=1
	if l < r:
		m = (l+r)//2 #0
		mergeSort(arr, l, m) #arr, 0, 0
		mergeSort(arr, m+1, r) #arr, 1, 1
		merge(arr, l, m, r) #arr, 0, 0, 1


arr = [56,32,145,63,13]
n = len(arr)

print(arr)
mergeSort(arr, 0, n-1)
print(arr)