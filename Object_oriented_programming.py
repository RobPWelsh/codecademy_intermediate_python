class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print('My id is {}.'.format(self.id))


class Admin(Employee):
    pass


e1 = Employee()
e2 = Employee()
e1.say_id()  # outputs My id is 1.
e2.say_id()  # outputs My id is 2.

e3 = Admin()
e3.say_id()  # outputs My id is 3.
