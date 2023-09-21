n = list(map(int, input().split()))
for i in range(len(n)):
    if n.count(n[i]) == 1:
        print(n[i])
