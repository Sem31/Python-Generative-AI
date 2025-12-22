# create table using list comprehension

table = [2 * i for i in range(1, 11)]
print(table)

list = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# make a square of each number in the list using list comprehension
squares = [x**2 for x in list]
print(squares)


menu = ["Masala Chai", "Iced Lemon Tea", "Green Tea", "Iced Peach Tea", "Ginger chai"]

iced_menu = [item for item in menu if "Iced" in item]
print(iced_menu)

# create a list of even numbers from 1 to 20 using list comprehension
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)


# use 2 for loops in list comprehension to create a list of all possible combinations of numbers from two lists
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

convert_dict = [{num: char} for num in list1 for char in list2]
print(convert_dict)
