def factors(n): # your code here 
    for x in range(1, n + 1):
        if n % x == 0:
            print("%d divides %d" % (x, n))
        else:
            x=x+1
            

factors(40) 

factors(5)  
