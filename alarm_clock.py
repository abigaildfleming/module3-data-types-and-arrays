current_time = int(input('What is the current time in hours: '))
alarm_hours = int(input('How many hours until you want your alarm to go off: '))

time_of_day = (current_time + alarm_hours) % 24

print('Time after', alarm_hours, 'hours:', time_of_day)