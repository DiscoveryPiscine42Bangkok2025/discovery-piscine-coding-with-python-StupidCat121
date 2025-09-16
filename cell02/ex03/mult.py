fisrt_num = int(input("Enter the first number: ")) 
second_num = int(input("Enter the second number: "))
mult = fisrt_num * second_num

print(f"{fisrt_num} x {second_num} = {mult}")
if mult < 0:
    print("The result is negative")
elif mult == 0:
    print("The result is positive and negative")
else:
    print("The result is positive")
