def returnPositives(arr):
    sum_p = 0
    for i in range(0,len(arr)):
        if arr[i] > 0:
            sum_p += arr[i]
    return sum_p

def returnNegatives(arr):
    sum_n = 0
    for i in range(0,len(arr)):
        if arr[i] < 0:
            sum_n += arr[i]
    return sum_n     

def getSubset(booleanArr, arr, sum_x):
    subset = []
    min_x = returnNegatives(arr)
    max_x = returnPositives(arr)

    if(sum_x < min_x or sum_x > max_x or (not booleanArr[len(arr) - 1][sum_x - min_x])):
        return subset
    
    for i in range(len(arr)-1,-1,-1):
        if (arr[i] == sum_x):
            subset.append(arr[i])
            return subset
        elif (not booleanArr[i-1][sum_x - min_x]):
            subset.append(arr[i])
            sum_x = sum_x - arr[i]

    return subset

def solve(booleanArr, arr):
    min_x = returnNegatives(arr)
    max_x = returnPositives(arr)
    for i in range(0, len(arr)):
        for j in range(min_x, max_x):
            if i == 0:
                booleanArr[i][j - min_x] = (arr[i] == j)
            
            elif(min_x <= j - arr[i] and j - arr[i] <= max_x):
                booleanArr[i][j - min_x] = (arr[i] == j) or (booleanArr[i-1][j-min_x]) or (booleanArr[i-1][j - min_x - arr[i]])
            
            else:
                booleanArr[i][j - min_x] = arr[i] == j or booleanArr[i-1][j - min_x]

    return booleanArr

if __name__ == '__main__':
    arr = [-1,6,4,2,3,-7,-5]
    _min = returnNegatives(arr)
    _max = returnPositives(arr)
    booleanArr = [[False] * (_max - _min + 1)] * len(arr)
    booleanArr = solve(booleanArr, arr)
    subSetArr = []
    subSetArr = getSubset(booleanArr,arr,0)
    print("Array is {}".format(arr))
    if(booleanArr[0][0] == True):
        print("Result is : True")
    else:
        print("Result is : False")