
import sys
def coin_change(coins, target):
    T = [0] * (target + 1)
    for i in range(1, target + 1):
        # initialize the minimum number of coins needed to infinity
        T[i] = sys.maxsize
        # for each coin
        for c in range(len(coins)):
            if i >= coins[c] :
                result = T[i - coins[c]]
                if result != sys.maxsize:
                    T[i] = min(T[i], result + 1)
    return T[target]
coins = [1, 2, 5, 10] 
target = int(input("Please enter the target: \n"))
result = coin_change(coins, target)
if result != sys.maxsize:
    print('The minimum number of coins required to get the desired change is: ',result)
