# Class Based Context Managers
# class PoemFiles:
#     def __init__(self):
#         print('Creating Poems!')
#
#     def __enter__(self):
#         print('Opening poem file')
#
#     def __exit__(self, *exc):
#         print('Closing poem file')
#
#
# with PoemFiles() as manager:
#     print('Hope is the thing with feather')
#
#     """
#     Prints:
#     Creating Poems!
#     Opening poem file
#     Hope is the thing with feather
#     Closing poem file
#     """
# _______________________________________________________
# Class Based Context Managers II
# class PoemFiles:
#     def __init__(self, poem_file, mode):
#         print('Starting up a poem context manager')
#         self.file = poem_file
#         self.mode = mode
#
#     def __enter__(self):
#         print('Opening poem file')
#         self.opened_poem_file = open(self.file, self.mode)
#         return self.opened_poem_file
#
#     def __exit__(self, *exc):
#         print('Closing poem file')
#         self.opened_poem_file.close()
#
#
# with PoemFiles('poem.txt', 'w') as open_poem_file:
#     open_poem_file.write('Hope is the thing with feathers')

# _______________________________________________________
# Handling Exceptions I
# class PoemFiles:
#
#     def __init__(self, poem_file, mode):
#         print(' \n -- Starting up a poem context manager -- \n ')
#         self.file = poem_file
#         self.mode = mode
#
#     def __enter__(self):
#         print('Opening poem file')
#         self.opened_poem_file = open(self.file, self.mode)
#         return self.opened_poem_file
#
#     # Create your __exit__ method here:
#     def __exit__(self, exc_type, exc_value, traceback):
#         print(exc_type)
#         print(exc_value)
#         print(traceback)
#         self.opened_poem_file.close()
#
#
# # First
# # with PoemFiles('poem.txt', 'r') as file:
# #     print("---- Exception data below ----")
# #     print(file.uppercasewords())
#
# # Second
# # with PoemFiles('poem.txt', 'r') as file2:
# #     print(file2.read())
# #     print("---- Exception data below ----")

# _______________________________________________________
# Handling Exceptions II
# class PoemFiles:
#
#     def __init__(self, poem_file, mode):
#         print(' \n -- Starting up a poem context manager -- \n')
#         self.file = poem_file
#         self.mode = mode
#
#     def __enter__(self):
#         print(' \n --  Opening poem file -- \n')
#         self.opened_poem_file = open(self.file, self.mode)
#         return self.opened_poem_file
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print(exc_type, exc_value, traceback, '\n')
#         # Write your code below:
#         if isinstance(exc_value, AttributeError):
#             self.opened_poem_file.close()
#             return True
#
#
# with PoemFiles('poem.txt', 'r') as file:
#     print("---- Exception data below ---- \n ")
#     print(file.uppercasewords())
#
# with PoemFiles('poem.txt', 'r') as file2:
#     print(file2.read())
#     print(" \n ---- Exception data below ---- \n ")

# _______________________________________________________
# Intro to Contextlib
# from contextlib import contextmanager


# @contextmanager
# def poem_files(file, mode):
#     print('Opening file')
#     open_poem_file = open(file, mode)
#
#     try:
#         yield open_poem_file
#     finally:
#         print('Closing File')
#         open_poem_file.close()
#
#
# with poem_files('poem.txt', 'a') as opened_file:
#     print('Inside yield')
#     opened_file.write('Rose is beautiful, Just like you.')

# _______________________________________________________
# Contextlib Error Handling

# @contextmanager
# def poem_files(file, mode):
#     print('Opening File')
#     open_poem_file = open(file, mode)
#     try:
#         yield open_poem_file
#     # Write your code below:
#     except AttributeError as e:
#         print(e)
#
#     finally:
#         print('Closing File')
#         open_poem_file.close()
#
#
# with poem_files('poem.txt', 'a') as opened_file:
#     print('Inside yield')
#     opened_file.sign('Buzz is big city. big city is buzz.')
# _______________________________________________________
# Nested Context Managers
# @contextmanager
# def poem_files(file, mode):
#     print('Opening File')
#     open_poem_file = open(file, mode)
#     try:
#         yield open_poem_file
#     finally:
#         print('Closing File')
#         open_poem_file.close()
#
#
# @contextmanager
# def card_files(file, mode):
#     print('Opening File')
#     open_card_file = open(file, mode)
#     try:
#         yield open_card_file
#     finally:
#         print('Closing File')
#         open_card_file.close()
#
#
# with poem_files('poem.txt', 'r') as poem:
#     with card_files('card.txt', 'w') as card:
#         print(poem)
#         print(card)
#         card.write(poem.read())
# _______________________________________________________
# Project - Aisha's Greetings
from contextlib import contextmanager


@contextmanager
def generic(card_type, sender, receiver):
    card_file = open(card_type, 'r')
    order = open(f'{sender}_generic.txt', 'w')

    try:
        order.write(f'Dear {receiver}, \n')
        order.write(card_file.read())
        order.write(f'\nSincerely, {sender} \n')
        yield order

    finally:
        card_file.close()
        order.close()


with generic('thankyou_card.txt', 'Mwenda', 'Amanda'):
    print('Card Generated!')

with open('Mwenda_generic.txt') as first_order:
    print(first_order.read())


class personalized:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.file = open(f'{sender}_personalized.txt', 'w')

    def __enter__(self):
        self.file.write(f'Dear {self.receiver} \n \n')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.write(f'\n \n Sincerely, \n {self.sender}')
        self.file.close()


with personalized('John', 'Michael') as order2:
    order2.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I "
                 "don't say it often but I just wanted to let you know that you inspire me an I love you! All the "
                 "best. Always.")

with generic('happy_bday.txt', 'Josiah', 'Remy') as order3, personalized('Josiah', 'Esther') as order4:
    order4.write("Happy Birthday!! I love you to the moon and back. Even though you're a pain sometimes, you're a "
                 "pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. "
                 "Cheers to 25!! You're getting old!")
