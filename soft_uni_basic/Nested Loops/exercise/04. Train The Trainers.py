judge = int(input())
line = input()
final_evaluation = 0
t = 0
while line != 'Finish':
    name_of_presentation = line
    t += 1
    final_rating = 0
    for i in range(judge):
        rating = float(input())
        i += 1
        final_rating += rating
        evaluation = final_rating / i
    print(f'{name_of_presentation} - {evaluation:.2f}.')

    final_evaluation += evaluation

    line = input()
print(f"Student's final assessment is {final_evaluation / t:.2f}.")
