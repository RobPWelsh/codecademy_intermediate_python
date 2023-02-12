# Print contents of built-in namespace
# print(dir(__builtins__))

# ------------------------------------------------------------

# Global namespace
# print(' -- Globals Namespace with empty script -- \n')
# # Write Checkpoint 1 here:
# print(globals())
#
#
# # Write Checkpoint 2 here:
# global_variable = 'global'
#
#
# # Write Checkpoint 3 here:
# def print_global():
#     global_variable = 'nested global'
#     nested_variable = 'nested value'
#
#
# print(' \n -- Globals Namespace non-empty script -- \n')
# # Write Checkpoint 4 here:
# print(globals())
# ------------------------------------------------------------
#
# Local namespace
global_variable = 'global'
#
#
# print(' -- Local and global Namespaces with empty script -- \n')
# # Write Checkpoint 1 here:
# print(locals())
# print(globals())
#
# # Write Checkpoint 2 here:
# def divide(num1, num2):
#     result = num1 / num2
#     print(locals())

# Write Checkpoint 3 here:
# def multiply(num1, num2):
#     product = num1 * num2
#     print(locals())
#
#
# print(' \n -- Local Namespace for divide -- \n')
# # Write Checkpoint 4 here:
# divide(3, 4)
#
# print(' \n -- Local Namespace for multiply -- \n')
# # Write Checkpoint 5 here:
# multiply(4, 50)
#
#
# print(' \n -- Local Namespace final -- \n')
# # Write Checkpoint 6 here:
# print(locals())
# ------------------------------------------------------------

# Enclosing namespace
# global_variable = 'global'
#
#
# def outer_function():
#     outer_value = "outer"
#
#     def inner_function():
#         inner_value = "inner"
#
#         def inner_nested_function():
#             nested_value = 'nested'
#
#         inner_nested_function()
#         # Add locals() call below
#         print(locals())
#
#     inner_function()
#
#
# outer_function()

# ------------------------------------------------------------

# # Local scope
# def painting(paint_colors, picture):
#     painting_statement = "To paint the " + picture + " we need the following colors: "
#     for color in paint_colors:
#         print(color)
#
# print(painting_statement)
# painting(['Saffron', 'White', 'Green'], 'Indian Flag')

# ------------------------------------------------------------

# Enclosing/Nonlocal scope
# def calc_paint_amount(width, height):
#     square_feet = width * height
#     # Write your code below!
#     def calc_gallons():
#         return square_feet / 400
#
#     return calc_gallons()
#
# print('Number of paint gallons needed: ')
# print(str(calc_paint_amount(30, 20)))

# ------------------------------------------------------------

# # Modifying scope behavior: nonlocal statement
# walls = [(20, 9), (25, 9), (20, 9), (25, 9)]
#
#
# def calc_paint_amount(wall_measurements):
#     square_feet = 0
#
#     def calc_square_feet():
#         for width, height in wall_measurements:
#             nonlocal square_feet  # This was added to fix the error
#             square_feet += width * height
#
#     def calc_gallons():
#         return square_feet / 400
#
#     calc_square_feet()
#
#     return calc_gallons()
#
#
# print('Number of paint gallons needed: ')
# print(str(calc_paint_amount(walls)))
# ------------------------------------------------------------

# Global scope
# paint_gallons_available = {
#     'red': 50,
#     'blue': 72,
#     'green': 99,
#     'yellow': 33
# }
# def print_available(color):
#     print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')
#
# def print_all_colors_available():
#     for color in paint_gallons_available:
#         print(color)
#
#
# print_available('red')
# print_all_colors_available()
# ------------------------------------------------------------

# Modifying Scope Behavior: global Statement

# def print_available(color):
#     global paint_gallons_available
#     paint_gallons_available = {
#         'red': 50,
#         'blue': 72,
#         'green': 99,
#         'yellow': 33
#     }
#     print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')
#
#
# print_available('red')
# for color in paint_gallons_available:
#     print(color)


