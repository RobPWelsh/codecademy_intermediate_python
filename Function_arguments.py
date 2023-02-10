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
# def print_animals(animal1, animal2, *args, animal4, **kwargs):
#     print(animal1, animal2)
#     print(args)
#     print(animal4)
#     print(kwargs)
#
#
# print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='Cat', animal5='Dog')
#
#
# # Exercise:
# def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
#     print(appetizer)
#     print(entrees)
#     print(sides)
#     print(dessert_scoops)
#
#
# single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops', sides='Mashed Potatoes', dessert1='Vanilla', dessert2='Cookies and Cream')
#
# # -------------------------------------------------------------------------------
# # Function call unpacking
#
#
# def calculate_price_per_person(total, tip, split):
#     total_tip = total * (tip/100)
#     split_price = (total + total_tip) / split
#     print(split_price)
#
#
# # Write your code below:
# table_7_total = [534.50, 20.0, 5]
# calculate_price_per_person(*table_7_total)

# -------------------------------------------------------------------------------
# Project - The Nile
from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function


# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
    from_lat, from_long = from_coords
    to_lat, to_long = to_coords

    distance = get_distance(from_lat, from_long, to_lat, to_long)
    shipping_rate = SHIPPING_PRICES[shipping_type]
    price = distance * shipping_rate
    return format_price(price)


# Test the function by calling
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
    cheapest_driver = None
    cheapest_driver_price = None
    for driver in drivers:
        driver_time = distance / driver.speed
        price_for_driver = driver_time * driver.salary
        if cheapest_driver is None:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
        elif price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
    return cheapest_driver_price, cheapest_driver


# Test the function by calling
test_function(calculate_driver_cost)

# Define calculate_money_made() here
def calculate_money_made(**trips):
    total_money_made = 0
    for trip_id, trip in trips.items():
        trip_revenue = trip.cost - trip.driver.cost
        total_money_made += trip_revenue
    return total_money_made

# Test the function by calling
test_function(calculate_money_made)

# Add some more text before commit