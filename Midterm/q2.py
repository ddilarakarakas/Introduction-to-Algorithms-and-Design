import math

def FindLastNumber(arr, result):
    if len(arr) == 0 or len(arr[0]) == 0:
        return int(result,2)
    leftArray = []
    rightArray = []
    for i in arr:
        if i[-1] == '0':
            leftArray.append(i[:-1])
        else:
            rightArray.append(i[:-1])
    if len(leftArray) > len(rightArray):
        result = '1' + result
        return FindLastNumber(rightArray, result)
    else:
        result = '0' + result
        return FindLastNumber(leftArray, result)

if __name__ == "__main__":
    my_arr = [0,1,2,3,4,5,7,6,8,9,10,11,12,13,14,15]
    binary_arr = []
    bit = '0' + str(32) + 'b'
    for i in my_arr:
        binary_arr.append(format(i,bit))
    print(FindLastNumber(binary_arr,""))