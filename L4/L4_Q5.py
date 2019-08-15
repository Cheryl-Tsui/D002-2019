def printer(secret, opened):
    i = 0
    while i < len(secret):
        if opened==[]:
            a=len(secret)
            for b in range (a):
                print("", end="_")
                i=i+1
        for n in opened:
            if i!=n:
                print("", end="_")
                i=i+1
                if i==n:
                    p=secret[n]
                    print(p, end="")
                    i=i+1
                    
            elif i==n:
                p=secret[n]
                print(p, end="")
                i=i+1
                
            else:
                k=len(secret)
                for m in range (k):
                    print("", end="_")
                    i=i+1

    print("\n")

        
# Note: you might use print(x, end="") to print x without changing line

printer("apple", [1, 2]) # _pp__
printer("orange", [0, 5]) # o____e
printer("cat", []) # ___
