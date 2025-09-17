# def scan(search_char, text_string):
#     count = 0
#     words = text_string.split() 
#     for word in words:
#         if search_char == word: 
#             count += 1
#     print(count)

# user_input_str = input()
# user_input_char = input()
# scan(user_input_char, user_input_str)


#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    text = sys.argv[2]

    count = text.count(keyword)

    if count > 0:
        print(count)
    else:
        print("none")

if __name__ == "__main__":
    main()

# python3 scan_it.py "the" "the cat thedog the bee" | cat -e