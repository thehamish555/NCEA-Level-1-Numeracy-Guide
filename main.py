"""
The following program was made for the purpose of a DT Assessment, It should
not be taken seriously and/or used to learn Level 1 Numeracy. Use at your own
risk, but you have been warned.

DEV: Hamish Lester
VERSION: 0.1-Alpha
DATED: July 27 2023
"""

import sys
import os
import random

class Numeracy:
    """
    Used to generate and calculate math equations for NCEA Level 1 Numeracy.
    """
    def __init__(self):
        """
        Creates the class and all required variables.
        """
        self.numbers = []
        self.last_added = None
        self.last_subtracted = None
        self.last_multiplied = None
        self.last_divided = None
    
    def help(self):
        """
        Shows information on the class
        """
        print('This class is used to generate and calculate math equations')

    def last_values(self):
        """
        If a value is required again, this will return all previous values
        """
        return {
                'generate_numbers': self.numbers,
                'addition': self.last_added,
                'subtraction': self.last_subtracted,
                'multiplication': self.last_multiplied,
                'division': self.last_divided
                }

    def generate_numbers(self, amount=1, min=-1*sys.maxsize, max=sys.maxsize):
        """
        Generates a list of numbers based on given arguments
        """
        self.numbers = []
        for i in range(amount):
            self.numbers.append(random.randint(min, max))
        return self.numbers

    def addition(self, *args):
        """
        Adds a list of numbers together, eg ([1, 2, 3], 4) returns 10
        """
        try:
            total = 0
            for arg in list(args):
                try:
                    total += sum(arg)
                except TypeError:
                    total += arg
        except TypeError:
            raise Exception('Invalid Entry, Lists inside Lists do not work!')
        self.last_added = total
        return self.last_added

    def subtraction(self, a, b):
        """
        Subtracts one number from another, eg (10, 3) returns 7
        """
        self.last_subtracted = a - b
        return self.last_subtracted

    def multiplication(self, *args):
        """
        Multplies a list of numbers together, eg ([2, 3], 6) returns 36
        """
        try:
            total = 1
            for arg in list(args):
                try:
                    for num in arg:
                        total = total * num
                except TypeError:
                    total = total * arg
        except TypeError:
            raise Exception('Invalid Entry, Lists inside Lists do not work!')
        self.last_multiplied = total
        return self.last_multiplied

    def division(self, a, b):
        """
        Dividess one number by another, eg (6, 3) returns 2
        """
        self.last_divided = a / b
        return self.last_divided

if len(sys.argv)==2 and sys.argv[1]=='--help':
    print(f'{__doc__.strip()}\n',) if __doc__ else print('No script information\n')
    print('\033[1mContained Classes and Functions\033[0m')
    try:
        print(f'''    \033[1mClass Numeracy:\033[0m
        {Numeracy.__doc__.strip()}''', end='\n\n')
    except AttributeError:
        print(f'''    \033[1mClass Numeracy:\033[0m
        No information provided''', end='\n\n')
    for method in dir(Numeracy):
        if not method.startswith('__'):
            try:
                print(f'''        \033[1m- Method {method}\033[0m
            {getattr(Numeracy, method).__doc__.strip()}''')
            except AttributeError:
                print(f'''        \033[1m- Method {method}\033[0m
            No information provided''')
elif __name__ == '__main__':
    """
    Will only run this code if run for the purpose of this program, that way
    people can use the class and functions without running the code for this
    program.
    """
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
    numeracy = Numeracy()
    numbers = numeracy.generate_numbers(2, 1, 10)
    print(f'Numbers: {numbers}')
    print(f'Addition: {numeracy.addition(numbers)}')
    print(f'Subtraction: {numeracy.subtraction(numbers[0], numbers[1])}')
    print(f'Multiplication: {numeracy.multiplication(numbers)}')
    print(f'Divided: {numeracy.division(numbers[0], numbers[1])}')
    print(f'Last Values {numeracy.last_values()}')