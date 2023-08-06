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
import json


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

    def name(self):
        """Rename the method to a placeholder string.

        Called with @Numeracy.name()
        Returns a placeholder name for the class method
        """
        def decorator(function):
            function.__name__ = self
            return function
        return decorator

    @name('Last Values')
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

    @name('Generate Numbers')
    def generate_numbers(self, amount=1, min=-1*sys.maxsize, max=sys.maxsize):
        """Generate a list of numbers based on given arguments.

        Called with Numeracy.generate_numbers(amount, min, max)
        Returns a list of randomly generated numbers in the given range
        """
        self.numbers = []
        for i in range(amount):
            self.numbers.append(random.randint(min, max))
        return self.numbers

    @name('+')
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

    @name('-')
    def subtraction(self, a, b):
        """Subtract one number from another, eg (10, 3) returns 7.

        Called with Numeracy.subtraction(a, b)
        Returns a - b
        """
        self.last_subtracted = a - b
        return self.last_subtracted

    @name('×')
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

    @name('÷')
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
    """Will only run this code if run by main.py, that way
    people can use the class and functions without running the code for this
    program.
    """
    def generate_question_and_answer():
        """Create a question and an answer.

        Called with generate_question_and_answer()
        Returns are question and answer
        """
        global cont

        def dict_walk(d):
            global cont
            if cont is True:
                for k, v in d.items():
                    r = random.choice(list(d.keys()))
                    question.append(r)
                    if v == '#end':
                        cont = False
                        break
                    else:
                        dict_walk(d[r])

        cont = True
        question = []
        num_of_names = 0
        num_of_nums = 0
        names = []

        dict_walk(data['Words'])
        for word in question:
            if word.strip().startswith('#name'):
                temp = int(word[-1:])
                if temp > num_of_names:
                    num_of_names = temp
            elif word.strip().startswith('#num'):
                temp = int(word[-1:])
                if temp > num_of_nums:
                    num_of_nums = temp
        for i in range(num_of_names):
            while True:
                temp = random.choice(data['Names'])
                if not names.__contains__(temp):
                    names.append(temp)
                    break
            question = ''.join(question).replace(f'#name{i+1}', temp)
        num_range = question.split(';')[1]
        numbers = numeracy.generate_numbers(num_of_nums,
                                            float(num_range.split()[0]),
                                            float(num_range.split()[1]))
        for i in range(num_of_nums):
            question = ''.join(question).replace(f'#num{i+1}', str(numbers[i]))
        question = question.split('@')
        equation = question.pop(1)
        question = question.pop(0)
        if len(equation.split()) > 1:
            numbers = []
            functions = []
            for word in equation.split():
                try:
                    int(word)
                    numbers.append(float(word))
                except ValueError:
                    functions.append(word)
                if len(functions) > 0 and len(numbers) > 1:
                    try:
                        total = getattr(numeracy, functions[0])(numbers)
                    except TypeError:
                        total = getattr(numeracy, functions[0])(numbers[0],
                                                                numbers[1])
                    numbers = [total]
                    functions = []
            answer = total
        else:
            function = equation.strip()
            try:
                answer = getattr(numeracy, function)(numbers)
            except TypeError:
                answer = getattr(numeracy, function)(numbers[0],
                                                     numbers[1])

        return question, answer

    numeracy = Numeracy()
    data = json.load(open('./data/keywords.json', 'r'))
    while True:
        try:
            question, answer = generate_question_and_answer()
            answer = float(answer)
            break
        except ZeroDivisionError:
            pass
    while True:
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
        print(question)
        try:
            user_answer = round(float(input('-> ')), 2)
            break
        except ValueError:
            pass
    if user_answer == answer:
        print('True')
    else:
        print('False')
