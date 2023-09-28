k = list(map(int, input().split()))
for i in range(1, k[0]):
    if k[i] ^ i != 0:
        tochtonado = i
        break
print(tochtonado)
