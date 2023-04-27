def coinExchange(amount, coinList) :
    coins = [10, 5, 2, 1]
    count = [0, 0, 0, 0]
    total = 0
    a = amount
    for i in range(len(coins)) :
        while amount >= coins[i] and coinList[i] > 0 :
            amount -= coins[i]
            coinList[i] -= 1
            count[i] += 1
            total += 1
    if amount > 0 :
        print("Amount:", a)
        print("Coins are not Enough.")
    else :
        print("Amount:", a)
        print("Coin exchange result:", count)
        print("Number of coins:", total)

def main() :
    coinList = [10, 10, 10, 10]
    coinExchange(249, coinList)
    
main()