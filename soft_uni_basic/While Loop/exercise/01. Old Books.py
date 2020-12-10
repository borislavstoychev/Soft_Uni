surching_book = input()
book = input()
b = 0
book_found = False
while book != 'No More Books':
    if book == surching_book:
        book_found = True
        print(f'You checked {b} books and found it.')
        break
    b += 1
    book = input()
if not book_found:
    print('The book you search is not here!')
    print(f'You checked {b} books.')
