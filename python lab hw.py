# Step 1: Create a list
my_list = [1, 2, 3, 4, 5]
print("Initial list:", my_list)

# Step 2: Use insert() to add an element at a specific index
my_list.insert(2, 10)  # Insert 10 at index 2
print("After insertion:", my_list)

# Step 3: Use remove() to remove a specific element
my_list.remove(3)  # Remove the first occurrence of 3
print("After removal:", my_list)

# Step 4: Use append() to add an element to the end of the list
my_list.append(6)  # Append 6 to the end of the list
print("After append:", my_list)

# Step 5: Use pop() to remove an element at a specific index
popped_element = my_list.pop(1)  # Pop the element at index 1
print("After pop:", my_list)
print("Popped element:", popped_element)

# Step 6: Use clear() to remove all elements from the list
my_list.clear()  # Clear the list
print("After clear():", my_list)

# Step 7: Attempt to remove an element from the cleared list
# This will raise a ValueError since the list is empty
try:
    my_list.remove(10)  # Attempt to remove 10
except ValueError as e:
    print("Error:", e)

# Input two numbers
num1 = int(input('write your number: '))
num2 = int(input('write your second number: '))

# Using if-else to find the largest number
if num1 > num2:
    largest_number = num1
else:
    largest_number = num2

print("The largest number is:", largest_number)



# Input a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")