days_n = int(input())
patients = 0
treated_patients = 0
untreated_patients = 0
count_of_doctors = 7

for i in range(1, days_n + 1):
    patients = int(input())
    if i % 3 == 0 and treated_patients < untreated_patients:
        count_of_doctors += 1
    if patients > count_of_doctors:
        treated_patients += count_of_doctors
        untreated_patients += patients - count_of_doctors
    else:
        treated_patients += patients

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')