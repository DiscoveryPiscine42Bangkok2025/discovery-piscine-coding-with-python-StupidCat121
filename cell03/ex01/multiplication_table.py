print("Enter a number")
num = int(input(""))    
print(num)
for i in range(0, 10):
    mult = num * (i)
    print(f"{i} x {num} = {mult}")