def array_of_name(dict) :
    list = []
    for first, last in dict.items() :
        list.append(f"{first.capitalize()} {last.capitalize()}")
    return list

person = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_name(person))