origin = [2, 8, 9, 48, 8, 22, -12, 2]
print(origin)
i = 0
while i < len(origin):
    if origin[i - 1] <= 5:
        origin.remove(origin[i - 1])
    else:
        origin[i] = origin[i] + 2
        i += 1

print(origin)