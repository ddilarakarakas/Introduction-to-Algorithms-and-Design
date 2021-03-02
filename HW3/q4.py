import random

swap_quicksort=0
swap_insertion=0

def quick_sort(array, low, high):
    if low<high:
        pivot = rearrange(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)

def rearrange(array,low,high):
    global swap_quicksort
    p = array[high]
    left = low-1
    for i in range(low,high):
        if array[i]<p:
            left+=1
            array[i], array[left] = array[left], array[i]
            swap_quicksort += 1
    array[left+1], array[high] = array[high], array[left+1]
    swap_quicksort += 1
    return left+1

def insertionSort(arr):
    global swap_insertion
    for i in range(2,len(arr)):
        current=arr[i]
        position=i-1
        while position>=1 and current < arr[position]:
            swap_insertion+=1
            arr[position+1] = arr[position]
            position=position-1
        arr[position+1]=current

if __name__ == "__main__":
    arr1=[]
    for i in range(0,1000):
        arr1=[]
        for i in range(0,1000):
            arr1.append(random.randint(0,10000))
        arr2=arr1[:]
        quick_sort(arr1,0,len(arr1)-1)
        insertionSort(arr2)
        
    print("Average count for quicksort = " + str(swap_quicksort/1000))
    print("Average count for insertionsort = " + str(swap_insertion/1000))


#It is a bit slow because it works with 1000 sizes.

