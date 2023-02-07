# Function arguments recap
# tables = {
#     1: ['Jiho', False],
#     2: [],
#     3: [],
#     4: [],
#     5: [],
#     6: [],
#     7: [],
# }
# print(tables)
#
#
# # Write your code below:
# def assign_table(table_number, name, vip_status=False):
#     tables[table_number] = [name, vip_status]
#
#
# assign_table(6, 'Yoni', False)
# print(tables)
#
# assign_table(name='Martha', vip_status=True, table_number=3)
# print(tables)
#
# assign_table(4, 'Karla')
# print(tables)


# Variable number of arguments: *args
# def print_order(*order_items):
#     print(order_items)
#
#
# print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')
# -------------------------------------------------------------------------------
#
# tables = {
#     1: {
#         'name': 'Jiho',
#         'vip_status': False,
#         'order': 'Orange Juice, Apple Juice'
#     },
#     2: {},
#     3: {},
#     4: {},
#     5: {},
#     6: {},
#     7: {},
# }
# print(tables)
#
#
# def assign_table(table_number, name, vip_status=False):
#     tables[table_number]['name'] = name
#     tables[table_number]['vip_status'] = vip_status
#     tables[table_number]['order'] = ''
#
#
# # Write your code below:
#
# def assign_and_print_order(table_number, *order_items):
#     tables[table_number]['order'] = order_items
#     for item in order_items:
#         print(item)
#
#
# assign_table(2, 'Arwa', True)
# assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')
#
# print(tables)
# -------------------------------------------------------------------------------
# Variable number of arguments: **kwargs

# def assign_food_items(**order_items):
#     print(order_items)
#     food = order_items.get('food')
#     drinks = order_items.get('drinks')
#     print(food)
#     print(drinks)
#
# # Example Call
# assign_food_items(food='Pancakes, Poached Egg', drinks='Water')
# -------------------------------------------------------------------------------
# tables = {
#   1: {
#     'name': 'Chioma',
#     'vip_status': False,
#     'order': {
#       'drinks': 'Orange Juice, Apple Juice',
#       'food_items': 'Pancakes'
#     }
#   },
#   2: {},
#   3: {},
#   4: {},
#   5: {},
#   6: {},
#   7: {},
# }
#
#
# def assign_table(table_number, name, vip_status=False):
#     tables[table_number]['name'] = name
#     tables[table_number]['vip_status'] = vip_status
#     tables[table_number]['order'] = {}
#
#
# assign_table(2, 'Douglas', True)
# print('--- tables with Douglas --- \n', tables)
#
#
# def assign_food_items(table_number, **order_items):
#     food = order_items.get('food')
#     drinks = order_items.get('drinks')
#     tables[table_number]['order']['food_items'] = food
#     tables[table_number]['order']['drinks'] = drinks
#
#
# print('\n --- tables after update --- \n')
#
# assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')
# print(tables)

# -------------------------------------------------------------------------------
# All together
# Example:
def print_animals(animal1, animal2, *args, animal4, **kwargs):
    print(animal1, animal2)
    print(args)
    print(animal4)
    print(kwargs)


print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='Cat', animal5='Dog')

# Exercise:

