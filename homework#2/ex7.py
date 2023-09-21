n = list(map(int, input().split()))
max = 0
for i in range(len(n)):
    if n.count(n[i]) >= max:
        max = n.count(n[i])
        chislo = n[i]
print(chislo)
