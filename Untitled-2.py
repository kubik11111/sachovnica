x=int(input("Zadaj rozmer sachovnice: "))

v=1
for i in range(x):
    for j in range(x):
        if v%2:
            print("X",end="")
            v+=1
        else:
            print(" ",end="")
            v+=1
    print()
    v-=1