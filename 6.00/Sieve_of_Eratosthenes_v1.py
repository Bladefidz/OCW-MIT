#Print print number between 2 - 1000
#This source code for http://www.scriptol.com/programming/sieve.php
#Use python 3 to compile

def eratosthenes(n):
    all = []         
    prime = 1  
    print("1, 2,")
    i = 3 
    while (i <= n):
        if  i not in all:
            print(i, ",")
            prime += 1
            j = i
            while (j <= (n / i)): 
                all.append(i * j)
                j += 1
        i += 2                        
    print("\n")

eratosthenes(1000)
