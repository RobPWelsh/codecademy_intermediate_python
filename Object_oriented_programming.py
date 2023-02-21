# class Employee:
#     new_id = 1
#
#     def __init__(self):
#         self.id = Employee.new_id
#         Employee.new_id += 1
#
#     def say_id(self):
#         print('My id is {}.'.format(self.id))
#
#
# class Admin(Employee):
#     def say_id(self):
#         super().say_id()
#         print('I am an Admin.')
#
#
# class Manager(Admin):
#     def say_id(self):
#         super().say_id()
#         print('I am in charge.')
#
# e1 = Employee()
# e2 = Employee()
# e1.say_id()  # outputs My id is 1.
# e2.say_id()  # outputs My id is 2.
#
# e3 = Admin()
# e3.say_id()  # outputs My id is 3. I am an Admin.
#
# e4 = Manager()
# e4.say_id()  # outputs My id is 4. I am an Admin. I am in charge.

# _____________________________________________________________________
#  Inheritance
# class Employee:
#     new_id = 1
#
#     def __init__(self):
#         self.id = Employee.new_id
#         Employee.new_id += 1
#
#     def say_id(self):
#         print("My id is {}.".format(self.id))
#
#
# class User:
#     def __init__(self, username, role="Customer"):
#         self.username = username
#         self.role = role
#
#     def say_user_info(self):
#         print("My username is {}.".format(self.username))
#         print("My role is {}.".format(self.role))
#
#
# # Write your code below
# class Admin(Employee, User):
#     def __init__(self):
#         super().__init__()
#         User.__init__(self, self.id, 'Admin')
#
#
#     def say_id(self):
#         super().say_id()
#         print("I am an admin.")
#
#
# e1 = Employee()
# e2 = Employee()
# e3 = Admin()
#
# e3.say_user_info()  # outputs My username is 3. My role is Admin.

# ________________________________________________________________
# Polymorphism
# class Employee:
#     new_id = 1
#
#     def __init__(self):
#         self.id = Employee.new_id
#         Employee.new_id += 1
#
#     def say_id(self):
#         print("My id is {}.".format(self.id))
#
#
# class Admin(Employee):
#     def say_id(self):
#         super().say_id()
#         print("I am an admin.")
#
#
# class Manager(Admin):
#     def say_id(self):
#         super().say_id()
#         print("I am in charge!")
#
#
# meeting = [Employee(), Admin(), Manager()]
# for role in meeting:
#     role.say_id()
# Outputs:
# My id is 1.
# My id is 2.
# I am an admin.
# My id is 3.
# I am an admin.
# I am in charge!
# _____________________________________________________
# Dunder Methods (another form of polymorphism)
# class Employee():
#     new_id = 1
#
#     def __init__(self):
#         self.id = Employee.new_id
#         Employee.new_id += 1
#
#
# class Meeting:
#     def __init__(self):
#         self.attendees = []
#
#     def __add__(self, employee):
#         print("ID {} added.".format(employee.id))
#         self.attendees.append(employee)
#
#     # Write your code
#     def __len__(self):
#         return len(self.attendees)
#
#
# e1 = Employee()
# e2 = Employee()
# e3 = Employee()
# m1 = Meeting()
#
# m1 + e1  # outputs ID 1 added.
# m1 + e2  # outputs ID 2 added.
# m1 + e3  # outputs ID 3 added.
#
# print(len(m1))  # outputs 3

# __________________________________________________
# Abstraction
# from abc import ABC, abstractmethod
#
#
# class AbstractEmployee(ABC):
#     new_id = 1
#
#     def __init__(self):
#         self.id = AbstractEmployee.new_id
#         AbstractEmployee.new_id += 1
#
#     @abstractmethod
#     def say_id(self):
#         pass
#
#
# # Write your code below
# class Employee(AbstractEmployee):
#
#     def say_id(self):
#         print('I am employee number {}'.format(self.id))
#
#
# e1 = Employee()
# e1.say_id()

# _______________________________________________________
# Encapsulation
# class Employee():
#     def __init__(self):
#         self.id = None
#         # Write your code below
#         self._id = 'Me'
#         self.__id = 'You'
#
#
# e = Employee()
# print(dir(e))


# ____________________________________________________
# Getters, Setters and Deleters
# class Employee():
#     new_id = 1
#
#     def __init__(self, name=None):
#         self.id = Employee.new_id
#         Employee.new_id += 1
#         self._name = name
#
#     # Write your code below
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         self._name = name
#
#     def del_name(self):
#         del self._name
#
#
# e1 = Employee("Maisy")
# e2 = Employee()
#
# print(e1.get_name())  # Maisy
#
# e2.set_name("Fluffy")
# print(e2.get_name())  # Fluffy
#
# e2.del_name()
# print(e2.get_name())  # Raises AttributeError since this attribute was deleted

# ________________________________________________________
# Project - School Catalogue
class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    def set_numberOfStudents(self, numberOfStudents):
        self.numberOfStudents = numberOfStudents

    def __repr__(self):
        return 'A {} school named {} with {} students.'.format(self.level, self.name, self.numberOfStudents)


my_high_school = School('Bloom Carroll', 'High', 125)

print(my_high_school.get_name())
print(my_high_school.get_level())
my_high_school.set_numberOfStudents(138)
print(my_high_school.get_numberOfStudents())


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, 'Primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        return super().__repr__() + ' The pickup policy is {}'.format(self.pickupPolicy)


my_primary_school = PrimarySchool('Carroll', 66, 'Early')
print(my_primary_school.get_name())
print(my_primary_school.get_pickupPolicy())
print(my_primary_school)


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, 'High', numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sportsTeams(self):
        return self.sportsTeams

    def __repr__(self):
        return super().__repr__() + ' The sports teams we have are {}'.format(self.sportsTeams)


my_high_school = HighSchool('Bloom Carroll', 125, ['Football', 'Baseball', 'Basketball'])
print(my_high_school.get_sportsTeams())
print(my_high_school)
