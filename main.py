print('hello print')
# hi 
def add_numbers(a, b):
    sum = a + b
    return sum  # Return the sum

# Call the function and print the result
result = add_numbers(1, 2)
print(f'The sum is {result}.')

def greet(name):
    print(f'hello {name}')

greet("alice")

a=(int(input('Enter an integer:')))
b=(float(input('enter a float:')))
print(a + b)

import calendar 
year= int(input('enter the year:'))
month= int(input('enter the month(1-12):'))
print(calendar.month(year, month))

import datetime

def greet_user():
    # Get the current time using this code
    now = datetime.datetime.now()
    current_hour = now.hour

    # Determine the greeting based on the current hour
    if 5 <= current_hour < 12:
        greeting = "Good Morning!"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon!"
    elif 17 <= current_hour < 21:
        greeting = "Good Evening!"
    else:
        greeting = "Good Night!"

    return greeting

if __name__ == "__main__":
    print(greet_user())

print(12345)

n = 7  # Height of D

for i in range(n):
    for j in range(n):
        if j == 0 or (j == n - 1 and i != 0 and i != n - 1) or (i == 0 or i == n - 1) and j < n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()