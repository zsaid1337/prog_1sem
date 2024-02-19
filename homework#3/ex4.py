n = input().split()

def autism(n):
    chislo = int(n[0])
    bukv = n[1]
    for i in range(1, chislo//2 +2):
        print(bukv*i)
                                    
    for j in range(chislo//2, 0, -1):
        print(bukv * j)
autism(n)
