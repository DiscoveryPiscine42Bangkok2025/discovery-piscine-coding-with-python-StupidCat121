def param(i):
    if len(i) >= 2:
        for j in range(len(i)):
            print(i[len(i) - 1 - j])
    else:
        print("none")

list = input("Enter parameters: ").split()
param(list)

