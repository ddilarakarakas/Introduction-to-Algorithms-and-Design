import math 

def interval(index1, index2):  
    j = int(math.log2(index2 - index1 + 1))  
    if tempArr[index1][j] <= tempArr[index2 - (1 << j) + 1][j]:  
        return tempArr[index1][j]  
    else: 
        return tempArr[index2 - (1 << j) + 1][j] 

def fillTable(arr):
    lenArr = len(arr)   
    for i in range(0, lenArr):  
        tempArr[i][0] = arr[i]  
    j = 1 
    while (1 << j) <= lenArr:  
        i = 0
        while (i + (1 << j) - 1) < lenArr:   
            if (tempArr[i][j - 1] <  tempArr[i + (1 << (j - 1))][j - 1]):  
                tempArr[i][j] = tempArr[i][j - 1]  
            else: 
                tempArr[i][j] = tempArr[i + (1 << (j - 1))][j - 1]  
              
            i += 1
        j += 1

def print_min(intervals, arr):
    fillTable(arr)
    lenInterval = len(intervals)
    for i in range(0,lenInterval) :
        l = intervals[i][0]
        r = intervals[i][1]
        print("Min of [%d,%d] : %d " %(l,r,interval(l, r)))
  
if __name__ == "__main__": 
    arr = [71, 23, 334, 20, 56, 10, 36, 128, 1]   
    maxSize = 400
    intervals = [[1,5],[1,2],[4,8]]
    tempArr = [[0 for i in range(maxSize)] for j in range(maxSize)] 
    print("Array : ", arr)
    print_min(intervals, arr)