n = int(input("Введите число: "))
for i in range(1, n+1):
    for j in range(1,n+1):
        if i==j:
            print(i, end=" ")
        else:
            print("0 ", end="")
    print("")