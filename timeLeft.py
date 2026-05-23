from datetime import datetime

year_of_birth = int(input('\nWhat is the year you were born?: '))
estimated_death_age = int(input('\nAt what age you believe you will die?: '))

current_year = datetime.now().year

your_age = current_year - year_of_birth

years_left = estimated_death_age - your_age
days_left = years_left * 365

print(f'\n\n You are left with only {days_left} days!\n')