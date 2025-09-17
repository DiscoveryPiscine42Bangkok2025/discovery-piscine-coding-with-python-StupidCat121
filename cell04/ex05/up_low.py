str = input("")
list = list(str)

for i in list:
    if i.islower():
        print(i.upper(), end = '')
    else:
        print(i.lower(), end = '')