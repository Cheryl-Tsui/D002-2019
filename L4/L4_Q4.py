def checker(sentence, letter):
    n=0
    result = []
    while n<=len(sentence)-1:
        if sentence[n]==letter:
            result=result + [n]
            n=n+1
        else:
            n=n+1
    return result   
   
a = checker("Apple", "p") # a = [1, 2]
b = checker("Banana", "p") # b = []
c = checker("Cat", "a") # c = [1]
print(a,b,c)
