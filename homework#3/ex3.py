e(x):
        i = 2
            f = []
                while  x != 1:
                            cacauntept = 0
                                    for j in range(1, x + 1):
                                                    if x % j == 0:
                                                                        cacauntept += 1
                                                                                if cacauntept == 2:
                                                                                                f.append(x)
                                                                                                            break
                                                                                                                count = 0
                                                                                                                        for j in range(1, i + 1):
                                                                                                                                        if i % j == 0:
                                                                                                                                                            count += 1
                                                                                                                                                                        else:
                                                                                                                                                                                            continue
                                                                                                                                                                                                if count == 2:
                                                                                                                                                                                                                if x % i == 0:
                                                                                                                                                                                                                                    x //= i
                                                                                                                                                                                                                                                    f.append(i) 
                                                                                                                                                                                                                                                                    continue
                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                i += 1
                                                                                                                                                                                                                                                                                                                continue
                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                    i += 1            
                                                                                                                                                                                                                                                                                                                                        return f
                                                                                                                                                                                                                                                                                                                                    k = input().split()
                                                                                                                                                                                                                                                                                                                                    x = k[0] = int(k[0])
                                                                                                                                                                                                                                                                                                                                    y = k[1] = int(k[1]) 
                                                                                                                                                                                                                                                                                                                                    list_chiselx = che(x)
                                                                                                                                                                                                                                                                                                                                    list_chisely = che(y)
                                                                                                                                                                                                                                                                                                                                    k = 1
                                                                                                                                                                                                                                                                                                                                    kruto = []
                                                                                                                                                                                                                                                                                                                                    for i in range(len(list_chiselx)):
                                                                                                                                                                                                                                                                                                                                            if list_chiselx[i] in list_chisely:
                                                                                                                                                                                                                                                                                                                                                        k *= list_chiselx[i]
                                                                                                                                                                                                                                                                                                                                                                f = list_chisely.index(list_chiselx[i])
                                                                                                                                                                                                                                                                                                                                                                        list_chiselx[i], list_chisely[f] = 1, 1
                                                                                                                                                                                                                                                                                                                                                                        for a in range(-10 * k, 10* k):
                                                                                                                                                                                                                                                                                                                                                                                for b in range(-10 * k, 10* k):
                                                                                                                                                                                                                                                                                                                                                                                            if a * x + b * y == k:
                                                                                                                                                                                                                                                                                                                                                                                                            kruto.append(abs(a) + abs(b))
                                                                                                                                                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                                                                                                                                                    for a in range(-10 * k, 10* k):
                                                                                                                                                                                                                                                                                                                                                                                                                            for b in range(-10 * k, 10* k):
                                                                                                                                                                                                                                                                                                                                                                                                                                        if a * x + b * y == k and min(kruto) == abs(a) + abs(b):
                                                                                                                                                                                                                                                                                                                                                                                                                                                        x1 = a
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    x2 = b
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            print(x1, x2, k)
