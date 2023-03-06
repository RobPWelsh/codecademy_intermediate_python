# yield vs return

# def class_standing_generator():
#     yield 'Freshman'
#     yield 'Sophomore'
#     yield 'Junior'
#     yield 'Senior'
#
#
# class_standings = class_standing_generator()
#
# for standing in class_standings:
#     print(standing) # prints Freshman, Sophomore, Junior, Senior on separate lines

# ___________________________________________________________
# next() and StopIteration
# def student_standing_generator():
#     student_standings = ['Freshman', 'Senior', 'Junior', 'Freshman']
#     for standing in student_standings:
#         if standing == 'Freshman':
#             yield 500
#
#
# standing_values = student_standing_generator()
#
# print(next(standing_values))  # prints 500
# print(next(standing_values))  # prints 500


# print(next(standing_values))  # Traceback - StopIteration

# ______________________________________________________________
# Generator Expressions
# def cs_generator():
#     for i in range(1, 5):
#         yield "Computer Science " + str(i)
#
#
# cs_courses = cs_generator()
# for course in cs_courses:
#     print(course)  # prints Computer Science 1 through 4 on separate lines
#
# cs_generator_exp = ('Computer Science ' + str(i) for i in range(1, 5))
# for course in cs_generator_exp:
#     print(course)  # prints Computer Science 1 through 4 on separate lines

# ______________________________________________________________
# Generator Methods: send()
# MAX_STUDENTS = 30
#
#
# def get_student_ids():
#     student_id = 1
#     while student_id <= MAX_STUDENTS:
#         # Write your code below
#         n = yield student_id
#         if n is not None:
#             student_id = n
#             continue
#
#         student_id += 1
#
#
# student_id_generator = get_student_ids()
# for i in student_id_generator:
#     # Write your code below
#     if i == 6:
#         i = student_id_generator.send(25)
#     print(i)


# ______________________________________________________________
# Generator Methods: throw()
# def student_counter():
#     for i in range(1, 5001):
#         yield i
#
#
# student_generator = student_counter()
# for student_id in student_generator:
#     # Write your code below:
#     if student_id > 100:
#         student_generator.throw(ValueError, "Invalid student ID")
#     print(student_id)

# ______________________________________________________________
# Generator Methods: close()
# def student_counter():
#     for i in range(1, 5001):
#         yield i
#
#
# student_generator = student_counter()
# for student_id in student_generator:
#     print(student_id)
#     # Write your code below:
#     if student_id > 99:
#         student_generator.close()

# ______________________________________________________________
# Connecting generators
# def science_students(x):
#     for i in range(1, x + 1):
#         yield i
#
#
# def non_science_students(x, y):
#     for i in range(x, y + 1):
#         yield i
#
#
# def combined_students():
#     yield from science_students(5)
#     yield from non_science_students(10, 15)
#     yield from non_science_students(25, 30)
#
#
# student_generator = combined_students()
# for student in student_generator:
#     print(student)


# ______________________________________________________________
# Generator Pipelines
# def course_generator():
#     yield ("Computer Science", 5)
#     yield ("Art", 10)
#     yield ("Business", 15)
#
#
# def add_five_students(courses):
#     for course, num_students in courses:
#         yield course, num_students + 5
#
#
# increased_courses = add_five_students(course_generator())
#
# for increased_course in increased_courses:
#     print(increased_course)


# ______________________________________________________________
# Review
# def summa():
#     yield 'Summa Cum Laude'
#
#
# def magna():
#     yield 'Magna Cum Laude'
#
#
# def cum_laude():
#     yield 'Cum Laude'
#
#
# # Write your code below:
# def graduation_countdown(days):
#     while days >= 0:
#         days_left = yield days
#         if days_left is not None:
#             days = days_left
#         else:
#             days -= 1
#
#
# days = 25
# countdown_generator = (days for days in range(days, -1, -1))
#
# grad_days = graduation_countdown(days)
# for day in grad_days:
#     if day == 15:
#         grad_days.send(10)
#     elif day == 3:
#         grad_days.close()
#     print("Days Left: {}".format(day))
#
# gpas = [3.2, 4.0, 3.6, 2.9]
#
# def honors_generator(gpas):
#     for gpa in gpas:
#         if gpa > 3.9:
#             yield from summa()
#         elif gpa > 3.7:
#             yield from magna()
#         elif gpa > 3.5:
#             yield from cum_laude()
#
# honors = honors_generator(gpas)
# for honor in honors:
#     print(honor)

# ______________________________________________________________
# Event Coordinator Project
guests = {}


def read_guestlist(file_name):
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline().strip().split(",")
        if len(line_data) < 2:
            # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        n = yield name
        if n is not None:
            name = n[0]
            age = int(n[1])
            guests[name] = age
            yield name


guest_names = read_guestlist('guest_list.txt')

for i in range(10):
    print(next(guest_names))

print(guest_names.send(['Jane', '35']))

for name in guest_names:
    print(name)

over_21 = (guest + ' ' + str(guests[guest]) for guest in guests if guests[guest] >= 21)

for name_age in over_21:
    print(name_age)


def table_1_generator():
    for i in range(5):
        yield 'Chicken', 'Table 1', 'Seat ' + str(i + 1)


def table_2_generator():
    for i in range(5):
        yield 'Beef', 'Table 2', 'Seat ' + str(i + 1)


def table_3_generator():
    for i in range(5):
        yield 'Fish', 'Table 3', 'Seat ' + str(i + 1)


def all_tables():
    yield from table_1_generator()
    yield from table_2_generator()
    yield from table_3_generator()


def assignments(guests, table):
    for guest in guests:
        table_list = list(next(table))
        table_list.insert(0, guest)
        table_list = tuple(table_list)
        yield table_list


test = assignments(guests, all_tables())

for assignment in test:
    print(assignment)


