def insertion_sort(arr, low, n): 
    for i in range(low + 1, n + 1): 
		val = arr[i] 
		j = i 
		while j>low and arr[j-1]>val: 
			arr[j]= arr[j-1] 
			j-= 1
		arr[j]= val 

def partition(arr, low, high): 
	pivot = arr[high] 
	i = j = low 
	for i in range(low, high): 
		if arr[i]<pivot: 
			a[i], a[j]= a[j], a[i] 
			j+= 1
	a[j], a[high]= a[high], a[j] 
	return j 

def quick_sort(arr, low, high): 
	if low<high: 
		pivot = partition(arr, low, high) 
		quick_sort(arr, low, pivot-1) 
		quick_sort(arr, pivot + 1, high) 
		return arr 

def hybrid_sort(arr, low, high): 
	while low<high: 
		if high - low < 9: 
			insertion_sort(arr, low, high) 
			break
		else: 
			pivot = partition(arr, low, high) 
			if pivot-low < high-pivot: 
				hybrid_sort(arr, low, pivot-1) 
				low = pivot + 1
			else: 
				hybrid_sort(arr, pivot + 1, high) 
				high = pivot-1

if __name__ == "__main__":
    a = [43,56,23,78,90,54,12,435,75,32,6,8,0,23,567,9,54,32,688,4,2,456,7,34,23] 
    hybrid_sort(a, 0, len(a)-1) 
    print(a) 