def maxMoney(M, locations, money, distance) : 
    n = len(location)
    maxMoney = [0] * (M + 1)   
    temp = 0;  
    for i in range(1, M + 1) :  
        if (temp < n) :  
            if(locations[temp] == i) :
                if (i <= distance) : 
                    maxMoney[i] = max(maxMoney[i - 1], money[temp]) 
                else : 
                    maxMoney[i] = max(maxMoney[i - distance - 1] + money[temp],  maxMoney[i - 1]); 
                temp += 1
            else :
                maxMoney[i] = maxMoney[i - 1]   
        else :       
            maxMoney[i] = maxMoney[i - 1]  
    return maxMoney[M] 
      
if __name__ == "__main__" : 
    M = 20
    location = [6, 7, 12, 13, 14] 
    money = [5, 3, 5, 2, 1]  
    distance = len(location)
    print(maxMoney(M, location, money, distance))