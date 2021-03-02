def mergeSort(arr):
    if len(arr) > 1:
        r = len(arr)//2
        leftArr = arr[:r]
        rightArr = arr[r:]
        mergeSort(leftArr)
        mergeSort(rightArr)
        merge(leftArr,rightArr,arr)
def merge(leftArr, rightArr, arr):
    i = j = k = 0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1
    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1
    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1

def findPairs(arr,number):
    mergeSort(arr)
    left = 0
    right = len(arr) - 1
    while left < right:
        sum = arr[left] * arr[right]
        if sum < number:
            left = left + 1
        elif sum > number:
            right = right - 1
        else:
            print("Numbers: " + str(arr[left]) + " "+ str(arr[right]))
            left = left + 1
            right = right - 1

if __name__ == '__main__':
    arr = [1,2,3,6,5,4]
    print(arr)
    print("Desired number: " + str(6))
    findPairs(arr,6)
