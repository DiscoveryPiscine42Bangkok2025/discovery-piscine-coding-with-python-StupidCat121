import numpy as np

num = float(input("Give me a number: "))

if num == np.floor(num):
    print(f"This is an integer")
else:
    print(f"This is a decimal")