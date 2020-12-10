input_text = input()

sum = 0

for i in range(0,len(input_text)):
    if input_text[i] == 'a':
        sum += 1
    elif input_text[i] == 'e':
        sum += 2
    elif input_text[i] == 'i':
        sum += 3
    elif input_text[i] == 'o':
        sum += 4
    elif input_text[i] == 'u':
        sum += 5
print(sum)
