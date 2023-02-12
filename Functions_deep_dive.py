from functools import reduce

# Using Map and Lambda
x = lambda a, b: a - b if a > b else None

print(x(25, 4))  # returns 21


# ___________________________________________


def double(x):
    return x * 2


int_list = [2, 4, 7]

doubled = map(double, int_list)

print(list(doubled))  # returns [4, 8, 14]

# ______________________________________

y = map(lambda values: values * 2, int_list)
print(list(y))  # returns [4, 8, 14]

# ______________________________________
grade_list = [3.5, 3.7, 2.6, 95, 87]

grades_100scale = map(lambda grade: grade * 25 if type(grade) is float else grade, grade_list)

updated_grade_list = list(grades_100scale)
print(updated_grade_list)

# ______________________________________
# Using Filter
books = [["Burgess", 1985],
         ["Orwell", "Nineteen Eighty-four"],
         ["Murakami", "1Q85"],
         ["Orwell", 1984],
         ["Burgess", "Nineteen Eighty-five"],
         ["Murakami", 1985]]

string_titles = filter(lambda title: type(title[1]) is str, books)

string_titles_list = list(string_titles)
print(
    string_titles_list)  # returns [['Orwell', 'Nineteen Eighty-four'], ['Murakami', '1Q85'], ['Burgess', 'Nineteen Eighty-five']]


# ______________________________________
# Using Reduce


def double(x, y):
    return x * y


test = reduce(double, [5, 6, 2, 3])
print(test)  # returns 180

letters = ['r', 'e', 'd', 'u', 'c', 'e']

word = reduce(lambda letter1, letter2: letter1 + letter2, letters)
print(word)  # returns reduce


# ______________________________________
# Decorators

# def title_decorator(print_name_function):
#     def wrapper():
#         print('Sir')
#         print_name_function()
#     return wrapper
#
# def print_my_name():
#     print('Rob')
#
# decorated_function = title_decorator(print_my_name)
#
# decorated_function()

# simplify the above by using @title_decorator
# def title_decorator(print_name_function):
#     def wrapper():
#         print('Sir')
#         print_name_function()
#
#     return wrapper
#
#
# @title_decorator
# def print_my_name():
#     print('Rob')
#
#
# print_my_name()

# Decorators with parameters
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print('Sir')
        print_name_function(*args, **kwargs)
    return wrapper


@title_decorator
def print_my_name(name, age):
    print('{} you are age {}'.format(name, str(age)))


print_my_name('Rob', 59)
