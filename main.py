"""NCEA Level 1 Numeracy Guide (Questions and Answers).

The following program was made for a DT Assessment, It should
not be taken seriously and/or used to learn Level 1 Numeracy. Use at your own
risk, but you have been warned.

DEV: Hamish Lester
VERSION: 0.2-Alpha
DATED: July 31, 2023
"""

import sys
import os
import random


class Numeracy:
    """Used to generate and calculate math equations for NCEA Level 1 Numeracy.

    Called with Numeracy()
    Returns a Numeracy Class
    """

    def __init__(self):
        """Create the class and all required variables.

        Called with Numeracy()
        """
        self.numbers = []
        self.last_added = None
        self.last_subtracted = None
        self.last_multiplied = None
        self.last_divided = None

    def help(self):
        """Show information on the class.

        Called with Numeracy.help()
        """
        print('This class is used to generate and calculate math equations')

    def name(self, name):
        """Rename the method to a placeholder string.

        Called with @Numeracy.name()
        Returns a placeholder name for the class method
        """
        def decorator(function):
            function.__name__ = name
            return function
        return decorator

    @name(1, 'Last Values')
    def last_values(self):
        """Return all previous values.

        Called with Numeracy.last_values()
        Returns Last Values calculated by the class
        """
        return {
                'generate_numbers': self.numbers,
                'addition': self.last_added,
                'subtraction': self.last_subtracted,
                'multiplication': self.last_multiplied,
                'division': self.last_divided
                }

    @name(1, 'Generate Numbers')
    def generate_numbers(self, amount=1, min=-1*sys.maxsize, max=sys.maxsize):
        """Generate a list of numbers based on given arguments.

        Called with Numeracy.generate_numbers(amount, min, max)
        Returns a list of randomly generated numbers in the given range
        """
        self.numbers = []
        for i in range(amount):
            self.numbers.append(random.randint(min, max))
        return self.numbers

    @name(1, '+')
    def addition(self, *args):
        """Add a list of numbers together, eg ([1, 2, 3], 4) returns 10.

        Called with Numeracy.addition(a, b, c...)
        Returns the sum of all numbers provided
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

    @name(1, '-')
    def subtraction(self, a, b):
        """Subtract one number from another, eg (10, 3) returns 7.

        Called with Numeracy.subtraction(a, b)
        Returns a - b
        """
        self.last_subtracted = a - b
        return self.last_subtracted

    @name(1, '×')
    def multiplication(self, *args):
        """Multiply a list of numbers together, eg ([2, 3], 6) returns 36.

        Called with Numeracy.multiplication(a, b, c...)
        Returns the multiple of all numbers provided
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

    @name(1, '÷')
    def division(self, a, b):
        """Divide one number by another, eg (6, 3) returns 2.

        Called with Numeracy.division(a, b)
        Returns a / b
        """
        self.last_divided = a / b
        return self.last_divided


if len(sys.argv) == 2 and sys.argv[1] == '--help':
    n = '\n'
    print(f'{__doc__.strip()}\n',) if __doc__ else \
        print('No script information\n')
    print('\033[1mContained Classes and Functions\033[0m')
    try:
        print(f'''    \033[1mClass Numeracy:\033[0m
        {Numeracy.__doc__.replace(n, n + "    ")}''')
    except AttributeError:
        print('''    \033[1mClass Numeracy:\033[0m
        No information provided''')
    for method in dir(Numeracy):
        if not method.startswith('__'):
            try:
                print(f'''        \033[1m- Method {method}\033[0m
            {getattr(Numeracy, method).__doc__.replace(n, n + "    ")}''')
            except AttributeError:
                print(f'''        \033[1m- Method {method}\033[0m
            No information provided''')
elif __name__ == '__main__':
    """
    Will only run this code if run by main.py, that way
    people can use the class and functions without running the code for this
    program.
    """

    while True:
        try:
            numeracy = Numeracy()
            numbers = numeracy.generate_numbers(2, -10, 10)
            function = random.choice((numeracy.addition, numeracy.subtraction,
                                      numeracy.multiplication,
                                      numeracy.division))
            answer = round(float(function(numbers[0], numbers[1])), 2)
            break
        except ZeroDivisionError:
            pass
    while True:
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
        print(f'Calculate What {numbers[0]}{function.__name__}{numbers[1]} Is')
        try:
            user_answer = round(float(input('= ')), 2)
            break
        except ValueError:
            pass
    if user_answer == answer:
        print('True')
    else:
        print('False')
        