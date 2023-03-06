# Iterator Objects: __iter__() and iter()
sku_list = [7046538, 8289407, 9056375, 2308597]

print(dir(sku_list))

sku_iterator_object_one = sku_list.__iter__()  # call object using method
print(sku_iterator_object_one)  # <list_iterator object at 0x0000022E11809FF0>

sku_iterator_object_two = iter(sku_list)  # call object using function
print(sku_iterator_object_two)  # <list_iterator object at 0x0000022E1180A050>

# _________________________________________________________
# Iterator Objects:__next__() and next()
dog_foods = {
    "Great Dane Foods": 4,
    "Min Pip Pup Foods": 10,
    "Pawsome Pup Foods": 8
}

dog_food_iterator = iter(dog_foods)
next_dog_food1 = next(dog_food_iterator)
print(next_dog_food1)  # Great Dane Foods
next_dog_food2 = next(dog_food_iterator)
next_dog_food3 = next(dog_food_iterator)
print(next_dog_food2)  # Min Pip Pup Foods
print(next_dog_food3)  # Pawsome Pup Foods


#  next(dog_food_iterator)  # Traceback - StopIteration
# _________________________________________________________
# Custom Iterators
class CustomerCounter:
    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        if self.count > 100:
            raise StopIteration
        else:
            return self.count


customer_counter = CustomerCounter()

for num in customer_counter:
    print(num)  # prints 1 - 100
# _________________________________________________________
# Infinite Iterator: Count
import itertools

max_capacity = 1000
num_bags = 0

for i in itertools.count(13.5, 13.5):
    if i > max_capacity:
        break
    num_bags += 1
print(num_bags)  # 74

# _________________________________________________________
# Input-Dependent Iterator: Chain
great_dane_foods = [2439176, 3174521, 3560031]
min_pin_pup_foods = [6821904, 3302083]
pawsome_pup_foods = [9664865]

# Write your code below:
all_skus_iterator = itertools.chain(great_dane_foods, min_pin_pup_foods, pawsome_pup_foods)

for sku in all_skus_iterator:
    print(sku)  # prints each sku on a separate line

# _________________________________________________________
# Combinatoric Iterator: Combinations
collars = ["Red-S", "Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

collar_combo_iterator = itertools.combinations(collars, 3)

for collar_combo in collar_combo_iterator:
    print(collar_combo)  # prints 20 3-member tuples on separate lines

# _________________________________________________________
# Review
cat_toys = [('laser', 1.99), ('fountain', 5.99), ('scratcher', 10.99), ('catnip', 15.99)]

cat_toy_iterator = iter(cat_toys)

print(next(cat_toy_iterator))  # ('laser', 1.99)
print(next(cat_toy_iterator))  # ('fountain', 5.99)
print(next(cat_toy_iterator))  # ('scratcher', 10.99)
print(next(cat_toy_iterator))  # ('catnip', 15.99)

max_money = 15
options = []

toy_combos = itertools.combinations(cat_toys, 2)

for combo in toy_combos:
    toy1 = combo[0]
    cost_of_toy1 = toy1[1]
    toy2 = combo[1]
    cost_of_toy2 = toy2[1]
    if cost_of_toy1 + cost_of_toy2 <= max_money:
        options.append(combo)

print(options)  # [(('laser', 1.99), ('fountain', 5.99)), (('laser', 1.99), ('scratcher', 10.99))]

# _________________________________________________________
# New Teacher in Town project
from roster import student_roster
from classroom_organizer import ClassroomOrganizer

# Create ClassroomOrganizer object
students = ClassroomOrganizer()

# Step 1 - Create iterator for the student roster and print out each student
student_iterator = iter(student_roster)

for i in range(10):
    print(next(student_iterator))

# Step 2 & 3 - Make the ClassroomOrganizer class iterable and print the first name of each student
for student in students:
    print(student)
# ------ or ---------
# student_iterator = iter(students)
# for i in range(10):
#     print(next(student_iterator))

# Step 4 - Add a method to ClassroomOrganizer to return option pairs for all students
print(students.seating_options())

# Step 5 - Get 4-pair combos of math and science students
stem_students = itertools.chain(students.get_students_with_subject('Math'),
                                students.get_students_with_subject('Science'))

stem_student_combos = itertools.combinations(stem_students, 4)

for stem_combo in stem_student_combos:
    print(stem_combo)
