n=int(input())
k = [int(input()) for _ in range(n)]
for i in range(1, n+1):
    if k[i-1] ^ i != 0:
        tochtonado = i
        break
print(tochtonado)
