time_record = int(input())
num_of_records = int(input())
time = int(input())

time_decore = time_record * 0.15
time_to_take_record = num_of_records * time
total_time = time_decore + time_to_take_record
final_time = round(time_record - total_time)
if final_time >= 0:
    print(f"You managed to finish the movie on time! You have {final_time} minutes left!")
else:
    print(f'Time is up! To complete the movie you need {abs(final_time)} minutes.')