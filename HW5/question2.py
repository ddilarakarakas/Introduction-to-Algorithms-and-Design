def minPath(arr):
    depth = [None] * len(arr)
    n = len(arr) - 1
    for i in range(len(arr[n])):
        depth[i] = arr[n][i]
    for i in range(len(arr) - 2, -1,-1):
        for j in range( len(arr[i])):
            depth[j] = arr[i][j] + min(depth[j], depth[j + 1])
    return depth[0]

if __name__ == '__main__':
    arr = [[ 2 ],[5, 4 ],[1, 4, 7 ],[8,6,9,6]]
    print(minPath(arr))