# Exceptions
staff = {
    'Austin': {
        'floor managers': 1,
        'sales associates': 5
    },
    'Melbourne': {
        'floor managers': 0,
        'sales associates': 8
    },
    'Beijing': {
        'floor managers': 2,
        'sales associates': 5
    },
}


def print_staff_report(location, staff_dict):
    managers = staff_dict['floor managers']
    sales_people = staff_dict['sales associates']
    ratio = sales_people / managers
    print('Instrument World ' + location + ' has:')
    print(str(sales_people) + ' sales employees')
    print(str(managers) + ' floor managers')
    print('The ratio of sales people to managers is ' + str(ratio))
    print()


for location, staff in staff.items():
    # Write your code below:
    try:
        print_staff_report(location, staff)
    except ZeroDivisionError as e:
        print('Could not print sales report for ' + location)  # Could not print sales report for Melbourne
        print(e)  # division by zero

# ________________________________________________________________________________
instrument_prices = {
    'Banjo': 200,
    'Cello': 1000,
    'Flute': 100,
}


def display_discounted_price(instrument, discount):
    full_price = instrument_prices[instrument]
    discount_percentage = discount / 100
    discounted_price = full_price - (full_price * discount_percentage)
    print("The instrument's discounted price is: " + str(discounted_price))


instrument = 'Banjo'
discount = '20'

# Write your code below:
try:
    display_discounted_price(instrument, discount)
except KeyError:
    print('An invalid instrument was entered!')
except TypeError:
    print('Discount percentage must be a number!')  # Discount percentage must be a number!
except Exception:
    print('Hit an exception other than KeyError or TypeError!')

# _______________________________________________________________
customer_rewards = {
    'Zoltan': 82570,
    'Guadalupe': 29850,
    'Mario': 17849
}


def display_rewards_account(customer):
    # Write your code below:
    try:
        rewards_number = customer_rewards[customer]
    except KeyError:
        print('Customer was not found in rewards program!')  # Customer was not found in rewards program!
    else:
        print('Rewards account number is: ' + str(rewards_number))


customer = 'Fred'
display_rewards_account(customer)

# __________________________________________________________________________
inventory = {
    'Piano': 3,
    'Lute': 1,
    'Sitar': 2
}


# Write your code below (Checkpoint 2):
class InventoryError(Exception):
    def __init__(self, supply):
        self.supply = supply

    def __str__(self):
        return 'Available supply is only ' + str(self.supply)


def submit_order(instrument2, quantity2):
    supply = inventory[instrument2]

    # Write your code below (Checkpoint 3 & 4):
    if quantity2 > supply:
        raise InventoryError(supply)
    else:
        inventory[instrument2] -= quantity2
        print('Successfully placed order! Remaining supply: ' + str(inventory[instrument2]))


instrument2 = 'Piano'
quantity2 = 5
submit_order(instrument2, quantity2)

# Outputs:
# Traceback (most recent call last):
#   File "C:\Users\Rob\PycharmProjects\codecademy_Intermediate_Python\Exceptions.py", line 116, in <module>
#     submit_order(instrument2, quantity2)
#   File "C:\Users\Rob\PycharmProjects\codecademy_Intermediate_Python\Exceptions.py", line 108, in submit_order
#     raise InventoryError(supply)
# InventoryError: Available supply is only 3
