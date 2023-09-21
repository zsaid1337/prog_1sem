n = int(input())
spsok = list(map(int, input().split()))
sum = 0
for j in range(max(spsok)):
    for i in range(n):
        if min(spsok) + j == spsok[i]:
            sum += 1
            break
    if sum == n//2+1:
        k = j
        break
print(min(spsok) + k)
