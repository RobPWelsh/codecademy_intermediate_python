from collections import OrderedDict, deque, namedtuple, defaultdict, ChainMap, Counter, UserDict, UserList, UserString
from helper_functions import process_csv_supplies

#
# # Recap: Python Containers
# company_name = 'Boring Clothing'
# company_location = (40.20, -83.00)
# company_products = ['shirts', 'pants', 'socks', 'belts', 'hats']
# company_data = {'name': company_name, 'location': company_location, 'products': company_products}
#
# # ___________________________________________________
# # Intro to Specialized Containers
#
# orders = OrderedDict({'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99},
#                       'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99},
#                       'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}})
#
# orders.move_to_end('order_4829')
# orders.popitem()
# print(orders)  # Prints OrderedDict([('order_6184', {'type': 'pants', 'size': 'medium', 'price': 14.99}), ('order_2905', {'type': 'shoes', 'size': 12, 'price': 22.5})])
#
#
# # ___________________________________________________
# # Deque
#
# The first row is skipped since it only contains labels
# csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

# Append important items to the front of the list
# supplies_deque = deque()
# for supply in csv_data:
#     if supply[2] == 'important':
#         supplies_deque.appendleft(supply)
#     else:
#         supplies_deque.append(supply)
#
# print(supplies_deque)  # Prints deque list of all items in csv file with important items to the left as deque([['silk thread', '5', 'important'], ['denim', '9', 'important'], ...
#
# # Create deque list of 25 important items
# ordered_important_supplies = deque()
# for i in range(25):
#     ordered_important_supplies.append(supplies_deque.popleft())
#
# # Create deque list of 10 unimportant items
# ordered_unimportant_supplies = deque()
# for i in range(10):
#     ordered_unimportant_supplies.append((supplies_deque.pop()))
#
# # ___________________________________________________
# # Named Tuple
clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

new_coat = ClothingItem('coat', 'black', 'small', 14.99)
print(new_coat)  # Prints ClothingItem(type='coat', color='black', size='small', price=14.99)

coat_cost = new_coat.price
print(coat_cost)  # Prints 14.99

updated_clothes_data = []

for item in clothes:
    updated_clothes_data.append(ClothingItem(item[0], item[1], item[2], item[3]))

print(updated_clothes_data)  # Prints [ClothingItem(type='t-shirt', color='green', size='large', price=9.99), ClothingItem(type='jeans', color='blue', size='medium', price=14.99), ClothingItem(type='jacket', color='black', size='x-large', price=19.99), ClothingItem(type='t-shirt', color='grey', size='small', price=8.99), ClothingItem(type='shoes', color='white', size='12', price=24.99), ClothingItem(type='t-shirt', color='grey', size='small', price=8.99)]

#
# # ___________________________________________________
# # DefaultDict
#
# site_locations = {'t-shirt': 'Shirts',
#                   'dress shirt': 'Shirts',
#                   'flannel shirt': 'Shirts',
#                   'sweatshirt': 'Shirts',
#                   'jeans': 'Pants',
#                   'dress pants': 'Pants',
#                   'cropped pants': 'Pants',
#                   'leggings': 'Pants'
#                   }
# updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']
#
# validated_locations = defaultdict(lambda: 'TODO: Add to website')
#
# validated_locations.update(site_locations)
# print(validated_locations)  # Prints defaultdict(<function <lambda> at 0x000001C4D7BD9760>, {'t-shirt': 'Shirts', 'dress shirt': 'Shirts', 'flannel shirt': 'Shirts', 'sweatshirt': 'Shirts', 'jeans': 'Pants', 'dress pants': 'Pants', 'cropped pants': 'Pants', 'leggings': 'Pants'})
#
# for item in updated_products:
#     if validated_locations[item] == 'TODO: Add to website':
#         site_locations[item] = validated_locations[item]
# print(site_locations)  # Prints {'t-shirt': 'Shirts', 'dress shirt': 'Shirts', 'flannel shirt': 'Shirts', 'sweatshirt': 'Shirts', 'jeans': 'Pants', 'dress pants': 'Pants', 'cropped pants': 'Pants', 'leggings': 'Pants', 'draped blouse': 'TODO: Add to website', 'undershirt': 'TODO: Add to website', 'sun dress': 'TODO: Add to website', 'camisole top': 'TODO: Add to website'}
#
#
# # ___________________________________________________
# # OrderedDict
# # The first 15 orders are provided
# order_data = [['Order: 1', 'purchased'],
#               ['Order: 2', 'purchased'],
#               ['Order: 3', 'purchased'],
#               ['Order: 4', 'returned'],
#               ['Order: 5', 'purchased'],
#               ['Order: 6', 'canceled'],
#               ['Order: 7', 'returned'],
#               ['Order: 8', 'purchased'],
#               ['Order: 9', 'returned'],
#               ['Order: 10', 'canceled'],
#               ['Order: 11', 'purchased'],
#               ['Order: 12', 'returned'],
#               ['Order: 13', 'purchased'],
#               ['Order: 14', 'canceled'],
#               ['Order: 15', 'purchased']]
#
# orders = OrderedDict(order_data)
# print(orders)  # Prints OrderedDict([('Order: 1', 'purchased'), ('Order: 2', 'purchased'), ('Order: 3', 'purchased'), ('Order: 4', 'returned'), ('Order: 5', 'purchased'), ('Order: 6', 'canceled'), ('Order: 7', 'returned'), ('Order: 8', 'purchased'), ('Order: 9', 'returned'), ('Order: 10', 'canceled'), ('Order: 11', 'purchased'), ('Order: 12', 'returned'), ('Order: 13', 'purchased'), ('Order: 14', 'canceled'), ('Order: 15', 'purchased')])
#
# to_move = []
# to_remove = []
#
# for order in orders:
#     if (orders[order]) == 'returned':
#         to_move.append(order)
#     elif (orders[order]) == 'canceled':
#         to_remove.append(order)
#
# print(to_move)  # Prints ['Order: 4', 'Order: 7', 'Order: 9', 'Order: 12']
# print(to_remove)  # Prints ['Order: 6', 'Order: 10', 'Order: 14']
#
# for order in to_remove:
#     orders.pop(order)
#
# for order in to_move:
#     orders.move_to_end(order)
#
# print(orders)  # Prints OrderedDict([('Order: 1', 'purchased'), ('Order: 2', 'purchased'), ('Order: 3', 'purchased'), ('Order: 5', 'purchased'), ('Order: 8', 'purchased'), ('Order: 11', 'purchased'), ('Order: 13', 'purchased'), ('Order: 15', 'purchased'), ('Order: 4', 'returned'), ('Order: 7', 'returned'), ('Order: 9', 'returned'), ('Order: 12', 'returned')])
#
#
# # ___________________________________________________
# # ChainMap
# year_profit_data = [
#     {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
#     {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
#     {'mar_profit': 11849.13},
#     {'apr_profit': 9870.68},
#     {'may_profit': 13662.34},
#     {'jun_profit': 12903.54},
#     {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
#     {'aug_profit': 17685.69},
#     {'sep_profit': 9815.57},
#     {'oct_profit': 10318.28},
#     {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
#     {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
# ]
#
# new_months_data = [
#     {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
#     {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
#     {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
# ]
#
# profit_map = ChainMap(*year_profit_data)
# print(profit_map)  # Prints ChainMap({'jan_profit': 15492.3, 'jan_holiday_profit': 2589.12}, {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88}, {'mar_profit': 11849.13}, {'apr_profit': 9870.68}, {'may_profit': 13662.34}, {'jun_profit': 12903.54}, {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21}, {'aug_profit': 17685.69}, {'sep_profit': 9815.57}, {'oct_profit': 10318.28}, {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55}, {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79})
#
#
# # Function to return sum of standard profits and sum of holiday profits contained in profit_map
# def get_profits(profit_map):
#     standard_profit = 0
#     holiday_profit = 0
#
#     for data in profit_map:
#         if data.find('holiday') == -1:
#             standard_profit += profit_map[data]
#         else:
#             holiday_profit += profit_map[data]
#
#     return standard_profit, holiday_profit
#
#
# last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)
#
# for item in new_months_data:
#     profit_map = profit_map.new_child(item)
#
# current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)
#
# year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
# year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit
#
# print(year_diff_standard_profit)
# print(year_diff_holiday_profit)
#
#
# # ___________________________________________________
# # Counter
#
# opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse',
#                      'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress',
#                      'dress', 'dress', 'jeans', 'dress', 'blouse']
#
# closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress',
#                      'jeans', 'dress', 'blouse']
#
# test = Counter(opening_inventory)
# print(test['shoes'])
# def find_amount_sold(opening, closing, item):
#     opening_count = Counter(opening)
#     print(opening_count)  # Prints Counter({'dress': 7, 'jeans': 4, 'blouse': 4, 'shoes': 3, 'skirt': 3, 't-shirt': 3, 'shorts': 1})
#     closing_count = Counter(closing)
#     print(closing_count)  # Prints Counter({'dress': 4, 'jeans': 3, 'skirt': 2, 'blouse': 2, 'shoes': 1, 'shorts': 1})
#     opening_count.subtract(closing_count)
#
#     return opening_count[item]
#
#
# tshirts_sold = find_amount_sold(opening_inventory, closing_inventory, 't-shirt')
# print(tshirts_sold)  # Prints 3
#
#
# # ___________________________________________________
# # Example of wrapping classes
# class Customer:
#
#     def __init__(self, name, age, address, phone_number):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.phone_number = phone_number
#
#
# class CustomerWrap(Customer):
#
#     def __init__(self, name, age, address, phone_number):
#         self.customer = Customer(name, age, address, phone_number)
#
#     def display_customer_info(self):
#         print('Name: ' + self.customer.name)
#         print('Age: ' + str(self.customer.age))
#         print('Address: ' + self.customer.address)
#         print('Phone Number: ' + self.customer.phone_number)
#
#
# customer = CustomerWrap('Dmitri Buyer', 38, '123 Python Avenue', '5557098603')
# customer.display_customer_info()
#
#
# # ___________________________________________________
# # Container Wrappers - UserDict
# data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
#         'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
#         'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
#         'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}
#
#
# class OrderProcessingDict(UserDict):
#
#     def clean_orders(self):
#         items_to_remove = []
#
#         for key, value in self.data.items():
#             if value['order_status'] == 'complete':
#                 items_to_remove.append(key)
#
#         for item in items_to_remove:
#             del self.data[item]
#
#
# process_dict = OrderProcessingDict(data)
#
# process_dict.clean_orders()
#
# print(data)

# ___________________________________________________
# Container Wrappers - UserList
# data = [4, 6, 8, 9, 5, 7, 3, 1, 0]
#
# class ListSorter(UserList):
#
#     # Overwrite the append method to add sort
#     def append(self, item):
#         self.data.append(item)
#         self.data.sort()
#
#
# sorted_list = ListSorter(data)
#
# sorted_list.append(12)
#
# print(sorted_list)

# ___________________________________________________
# Container Wrappers - UserString

# str_name = 'python powered patterned products'
# str_word = 'patterned '
#
#
# class SubtractString(UserString):
#     def __sub__(self, other):
#         if other in self.data:
#             self.data = self.data.replace(other, '')
#
#
# subtract_string = SubtractString(str_name)
#
# subtract_string - str_word
#
# print(subtract_string)

# ___________________________________________________
# Review
# overstock_items = [['shirt_103985', 15.99],
#                     ['pants_906841', 19.99],
#                     ['pants_765321', 15.99],
#                     ['shoes_948059', 29.99],
#                     ['shoes_356864', 9.99],
#                     ['shirt_865327', 10.99],
#                     ['shorts_086853', 9.99],
#                     ['pants_267953', 21.99],
#                     ['dress_976264', 32.99],
#                     ['shoes_135786', 17.99],
#                     ['skirt_196543', 12.99],
#                     ['jacket_976535', 26.99],
#                     ['pants_086367', 30.99],
#                     ['dress_357896', 29.99],
#                     ['shoes_157895', 14.99]]
#
# split_prices = deque()
#
# for item in overstock_items:
#     if item[1] > 20.00:
#         split_prices.appendleft(item)
#     else:
#         split_prices.append(item)
#
# print(split_prices)
#
# ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])
#
#
# bundles = []
# while len(split_prices) >= 5:
#     bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(), split_prices.popleft()]
#     calc_price = sum(b[1] for b in bundle_list)
#
#     bundles.append(ClothesBundle(bundle_list, calc_price))
#
# print(bundles)
#
# promoted_bundles = []
#
# for bundle in bundles:
#     if bundle.bundle_price > 100:
#         promoted_bundles.append(bundle)
#
# print(promoted_bundles)

