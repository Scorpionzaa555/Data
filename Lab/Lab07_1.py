from time import time

#***v1***
def summation(n):
    value = 0
    for i in range(1, n + 1):
        value = value + i
    return value

#***v2***
# def summation(n):
#    return (n * (n + 1)) / 2

def analyze_algo(n = 1):
    start_time = time()
    summation(n)
    end_time = time() 
    elapsed = end_time - start_time 
    print("execution time:", elapsed)

def main():
    analyze_algo(1000000)
    analyze_algo(10000000) #100 10_000 1_000_000 100_000_000 1_000_000_000
    analyze_algo(100000000)

main()