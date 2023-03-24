from time import time
import random

def randomList(n):
    a = list(random.sample(range(1, 1_000_000), n))
    b = list(random.sample(range(1000001, 2000000), n))
    c = list(random.sample(range(2000001, 3000000), n))
    return a, b, c


#***v1***
def O2isIntersect(a, b, c):
    for num in a:
        if num in b and num in c:
            return True
        return False

#***v2***
def O3isIntersect(a, b, c):
    for i in range(0, len(a)):    
        for j in range(0, len(b)):
            for k in range(0, len(c)):
                if c[k] == b[j] == a[i]:
                    return True
    
    return False

def analyze_algo(n):
    a,b,c = randomList(n)
    start_time = time()
    O3isIntersect(a, b, c)
    end_time = time() 
    elapsed = end_time - start_time 
    print("execution time:", elapsed)

def main():
    analyze_algo(100) #100 1000 10000 100000

main()