max=-999
for a in range (1,61):
    for b in range (1,61):
        for c in range (1,61):
            for d in range (1,61):
                e=a*b
                f=b*c
                g=c*d
                i=e+f+g
                if (a+b+c+d==60):
                    while i>max:
                        max=i
                        print(i)
                    
                    
                    
