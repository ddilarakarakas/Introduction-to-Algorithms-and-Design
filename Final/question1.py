def pol_sub_arr(str) :
    strLength = len(str) 
    sub_table = [[0 for x in range(strLength)] for y in range(strLength)] 
    currentLength = 1
    i = 0
    for i in range(strLength) :
        sub_table[i][i] = True
    index = 0
    i = 0
    for i in range(strLength-1) :
        if (str[i] == str[i + 1]) :
            sub_table[i][i + 1] = True
            index = i
            currentLength = 2
    k = 3
    while k <= strLength :
        i = 0
        for i in range(strLength - k + 1 ) : 
            j = i + k - 1
            if (sub_table[i + 1][j - 1] and str[i] == str[j]) :
                sub_table[i][j] = True
                if (k > currentLength) :
                    index = i
                    currentLength = k
        k = k + 1
    print(str[index : index + currentLength])
    return currentLength

my_string = "karakas"
l = pol_sub_arr(my_string)
print ("Length is:", l)

my_string = "xxyyyyyxyyx"
l = pol_sub_arr(my_string)
print ("Length is:", l)

my_string = "karaarak"
l = pol_sub_arr(my_string)
print ("Length is:", l)

my_string = "aabbaaere"
l = pol_sub_arr(my_string)
print ("Length is:", l)
