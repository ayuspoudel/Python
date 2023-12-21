def count_prime(n):
    ar = [0]*(n+1)
    ar[0] = ar[1] = 1
    f = 2
    for i in ar(2, n, f):
        ar[i] = 1
        f = f+1
    count = 0
    for i in ar:
        return ar.count(1)
    
count_prime(5)

    
