def print_knapsack(n, W, weight, values):
    dummy = [0] * (W + 1)
    dp = [dummy.copy() for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weight[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weight[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    res = dp[n][W]
    print("Total capacity that can be taken : ", res)
    w = W
    print("Value 4 :  ", weight[i - 2])
    for i in range(n, 0, -1):
        w = W
    if res <= 0:
        return
    if res != dp[i - 1][w]:
        print("Value 10 : " , weight[i - 1], end=" ")
        res = res - values[i - 1]
        w = w - weight[i - 1]

if __name__ == "__main__":
    values = [ 10, 4, 3 ]
    weight = [ 5, 4, 2 ]
    W = 9
    n = len(values)
    print("values : ", values)
    print("weight : ", weight)
    print_knapsack(n, W, weight, values)
    print("")