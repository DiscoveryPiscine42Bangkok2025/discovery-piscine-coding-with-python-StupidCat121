def find_the_redheads(dict) :
    list = []
    for name, color in dict.items() :
        if color == "red" :
            list.append(name)

    return list

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))