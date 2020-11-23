def palindrome_integer(this_list):
    for i in this_list:
        reversed_element = i[:: -1]
        if i == reversed_element:
            print(True)
        else:
            print(False)


line = input().split(", ")

palindrome_integer(line)
