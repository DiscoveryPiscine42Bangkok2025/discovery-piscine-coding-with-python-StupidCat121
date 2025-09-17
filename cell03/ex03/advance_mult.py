i = 0 
j = 0

while(i <= 10):
    j = 0
    print(f"Talbe de {i}:", end = ' ')
    while(j <= 10):
        print(f"{i * j}", end = ' ')
        j = j + 1
    print()
    i = i + 1