from random import gauss
current = [x/10 for x in range(0, 200, 5)]
voltage = [c* 72.7326+ gauss(0.0, 0.5) for c in current]

with open("exp.txt", "w") as fout:
    fout.write("I_A U_V\n")
    for i in range(len(current)):
        fout.write(f"{current[i]} {voltage[i]}\n
        

        
