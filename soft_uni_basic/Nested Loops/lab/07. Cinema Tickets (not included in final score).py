comand = input()
total_celled_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
while comand != "Finish":
    free_sits = int(input())
    type_of_ticket = input()
    ticket_sold = 0
    while type_of_ticket != "End":
        total_celled_tickets += 1
        ticket_sold += 1
        if type_of_ticket == 'student':
            student_tickets += 1
        elif type_of_ticket == 'standard':
            standard_tickets += 1
        elif type_of_ticket == 'kid':
            kids_tickets += 1

        if ticket_sold == free_sits:
            break
        type_of_ticket = input()
    print(f'{comand} - {ticket_sold / free_sits * 100:.2f}% full.')
    comand = input()

print(f'Total tickets: {total_celled_tickets}')
print(f'{student_tickets / total_celled_tickets * 100:.2f}% student tickets.')
print(f'{standard_tickets / total_celled_tickets * 100:.2f}% standard tickets.')
print(f'{kids_tickets / total_celled_tickets * 100:.2f}% kids tickets.')
