nt(input())
k = list(input())
for j in range(len(k)//n):
    new = []
    for i in range(n):
        bukv = k.pop(0)
        new.append(bukv)
    k.extend(new[::-1])
print(*k, sep = '')
