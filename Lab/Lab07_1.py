from time import time
#***v1***

def summation(n):
    value = 0
    for i in range(1, n + 1):
        value = value + i
    return value

def analyze_algo(n = 1):
    start_time = time()
    summation(n)
    end_time = time() 
    elapsed = end_time - start_time 
    print("execution time:", elapsed)

#***v2***

#def summation(n):
#    return (n * (n + 1)) / 2
    
#def analyze_algo(n = 1):
#    start_time = time()
#    summation(n)
#    end_time = time() 
#    elapsed = end_time - start_time 
#    print("execution time:", elapsed)

def main():
    analyze_algo(100000) #100 10000 1000000 100000000 1000000000

main()
