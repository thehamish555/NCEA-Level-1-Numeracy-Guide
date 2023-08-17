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
import PyQt6.QtWidgets as PyQt
import PyQt6.QtGui as PyQtGui
import PyQt6.QtCore as PyQtCore


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
        {Numeracy.__doc__.replace(n, n + '    ')}''')
    except AttributeError:
        print('''    \033[1mClass Numeracy:\033[0m
        No information provided''')
    for method in dir(Numeracy):
        if not method.startswith('__'):
            try:
                print(f'''        \033[1m- Method {method}\033[0m
            {getattr(Numeracy, method).__doc__.replace(n, n + '    ')}''')
            except AttributeError:
                print(f'''        \033[1m- Method {method}\033[0m
            No information provided''')
elif __name__ == '__main__':
    """Will only run this code if run by main.py, that way
    people can use the class and functions without running the code for this
    program.
    """
    class PageWindow(PyQt.QMainWindow):
        gotoSignal = PyQtCore.pyqtSignal(str)

        def goto(self, name):
            self.gotoSignal.emit(name)

    class MainWindow(PageWindow):
        def __init__(self):
            super().__init__()
            self.initUI()
            self.setWindowTitle('NCEA Level 1 Numeracy Guide | Home')

        def initUI(self):
            self.UiComponets()

        def UiComponets(self):
            self.quizButton = PyQt.QPushButton("Start Quiz", self)
            self.quizButton.setGeometry(PyQtCore.QRect(285, 265, 100, 30))
            self.quizButton.setStyleSheet('''
                                            QPushButton {
                                                background-color: #8DCCD2;
                                                border-radius: 7px;
                                                border: 1px solid #232B2D;
                                                color: #232B2D;
                                            }
                                            QPushButton:hover {
                                                background-color: #005A69;
                                            }
                                            QPushButton:pressed {
                                                background-color: #005A69;
                                            }
                                            ''')
            self.quizButton.clicked.connect(
                self.make_handleButton('quizButton')
            )

        def make_handleButton(self, button):
            def handleButton():
                if button == 'quizButton':
                    self.goto('quiz')
            return handleButton

    class QuizWindow(PageWindow):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle('NCEA Level 1 Numeracy Guide | Quiz')
            self.UiComponents()

        def make_handleButton(self, button):
            def handleButton():
                if button == 'menuButton':
                    self.goto('menu')
                if button == 'nextButton':
                    self.get_question()
                    self.questionLabel.setText(self.question)
                    self.workingButton.hide()
                    self.nextButton.hide()
                    self.answerLabel.hide()
                    self.lineEdit.setReadOnly(False)
                    self.lineEdit.clear()
                elif button == 'workingButton':
                    self.messageBox = PyQt.QMessageBox()
                    self.messageBox.setText(self.working)
                    self.messageBox.setStyleSheet('''
                                                  QMessageBox {
                                                      background-color:
                                                          #FFFFFF;
                                                  }
                                                  QMessageBox QLabel {
                                                      background-color:
                                                          #FFFFFF;
                                                      border: 1px solid
                                                          #232B2D;
                                                      border-radius: 7px;
                                                      margin-right: 20px;
                                                      color: #232B2D;
                                                      padding-left: 5px;
                                                      padding-right: 5px;
                                                      padding-top: 5px;
                                                      padding-bottom: 5px;
                                                  }
                                                  QMessageBox QPushButton {
                                                      background-color:
                                                          #8DCCD2;
                                                      border-radius: 7px;
                                                      border: 1px solid
                                                          #232B2D;
                                                      margin-right: 20px;
                                                      color: #232B2D;
                                                  }
                                                  QMessageBox QPushButton:
                                                      hover {
                                                          background-color:
                                                              #005A69;
                                                  }
                                                  QMessageBox QPushButton:
                                                      pressed {
                                                          background-color:
                                                              #005A69;
                                                  }
                                                  ''')
                    self.setWindowTitle(
                                        'NCEA Level 1 Numeracy Guide | Working'
                                        )
                    self.messageBox.exec()
                elif button == 'answerButton':
                    self.lineEdit.setReadOnly(True)
                    self.workingButton.show()
                    self.nextButton.show()
                    self.answerLabel.show()
                    try:
                        if float(self.lineEdit.text()) == self.float_answer:
                            self.answerLabel.setText('✓')
                            self.answerLabel.setStyleSheet('''
                                                           color: #21CC62;
                                                           background-color:
                                                               #FFFFFF;
                                                           font-size: 18pt;
                                                           ''')
                        else:
                            self.answerLabel.setText('x')
                            self.answerLabel.setStyleSheet('''
                                                           color: #CC2A21;
                                                           background-color:
                                                               #FFFFFF;
                                                           font-size: 18pt;
                                                           ''')
                    except ValueError:
                        if self.lineEdit.text().rstrip('0').rstrip('.') == \
                          self.string_answer.rstrip('0').rstrip('.'):
                            self.answerLabel.setText('✓')
                            self.answerLabel.setStyleSheet('''
                                                           color: #21CC62;
                                                           background-color:
                                                               #FFFFFF;
                                                           font-size: 18pt;
                                                           ''')
                        else:
                            self.answerLabel.setText('x')
                            self.answerLabel.setStyleSheet('''
                                                           color: #CC2A21;
                                                           background-color:
                                                               #FFFFFF;
                                                           font-size: 18pt;
                                                           ''')
            return handleButton

        def get_question(self):
            while True:
                try:
                    self.question, self.string_answer, self.float_answer, \
                        self.working = generate_question_and_answer()
                    break
                except ZeroDivisionError:
                    pass

        def UiComponents(self):
            self.get_question()
            self.questionLabel = PyQt.QLabel(self.question, self)
            self.questionLabel.setGeometry(PyQtCore.QRect(15, 5, 470, 200))
            self.questionLabel.setStyleSheet('''
                                         background-color: #FFFFFF;
                                         border: 1px solid #232B2D;
                                         border-radius: 15px;
                                         padding-left: 5px;
                                         padding-right: 5px;
                                         color: #232B2D;
                                         ''')
            self.questionLabel.setAlignment(PyQtCore.Qt.AlignmentFlag
                                            .AlignHCenter
                                            | PyQtCore.Qt.AlignmentFlag.
                                            AlignTop)
            self.questionLabel.setWordWrap(True)

            self.lineEdit = PyQt.QLineEdit(self, clearButtonEnabled=True,
                                           placeholderText='Enter Answer...',)
            self.lineEdit.setGeometry(PyQtCore.QRect(20, 210, 350, 30))
            self.lineEdit.setStyleSheet('''
                                         background-color: #FFFFFF;
                                         border: 1px solid #232B2D;
                                         border-radius: 7px;
                                         padding-left: 2px;
                                         color: #232B2D;
                                         ''')

            self.answerButton = PyQt.QPushButton('Check Answer', self)
            self.answerButton.setGeometry(PyQtCore.QRect(380, 210, 100, 30))
            self.answerButton.setStyleSheet('''
                                            QPushButton {
                                                background-color: #8DCCD2;
                                                border-radius: 7px;
                                                border: 1px solid #232B2D;
                                                color: #232B2D;
                                            }
                                            QPushButton:hover {
                                                background-color: #005A69;
                                            }
                                            QPushButton:pressed {
                                                background-color: #005A69;
                                            }
                                            ''')
            self.answerButton.clicked.connect(self.make_handleButton(
                                              'answerButton'))

            self.answerLabel = PyQt.QLabel('', self)
            self.answerLabel.setGeometry(PyQtCore.QRect(348, 213, 20, 20))
            self.answerLabel.hide()

            self.menuButton = PyQt.QPushButton("Main Menu", self)
            self.menuButton.setGeometry(PyQtCore.QRect(5, 265, 100, 30))
            self.menuButton.setStyleSheet('''
                                          QPushButton {
                                              background-color: #8DCCD2;
                                              border-radius: 7px;
                                              border: 1px solid #232B2D;
                                              color: #232B2D;
                                          }
                                          QPushButton:hover {
                                              background-color: #005A69;
                                          }
                                          QPushButton:pressed {
                                              background-color: #005A69;
                                          }
                                          ''')
            self.menuButton.clicked.connect(self.make_handleButton(
                                            'menuButton'))

            self.workingButton = PyQt.QPushButton('Show Working', self)
            self.workingButton.setGeometry(PyQtCore.QRect(285, 265, 100, 30))
            self.workingButton.setStyleSheet('''
                                             QPushButton {
                                                 background-color:
                                                     #8DCCD2;
                                                 border-radius: 7px;
                                                 border: 1px solid
                                                     #232B2D;
                                                 color: #232B2D;
                                            }
                                            QPushButton:hover {
                                                background-color:
                                                    #005A69;
                                            }
                                            QPushButton:pressed {
                                                background-color:
                                                    #005A69;
                                            }
                                            ''')
            self.workingButton.hide()
            self.workingButton.clicked.connect(self.make_handleButton(
                                               'workingButton'))

            self.nextButton = PyQt.QPushButton('Next Question', self)
            self.nextButton.setGeometry(PyQtCore.QRect(395, 265, 100, 30))
            self.nextButton.setStyleSheet('''
                                          QPushButton {
                                              background-color:
                                                  #8DCCD2;
                                              border-radius: 7px;
                                              border: 1px solid
                                                  #232B2D;
                                              color: #232B2D;
                                          }
                                          QPushButton:hover {
                                              background-color:
                                                  #005A69;
                                          }
                                          QPushButton:pressed {
                                              background-color:
                                                  #005A69;
                                          }
                                          ''')
            self.nextButton.hide()
            self.nextButton.clicked.connect(self.make_handleButton(
                                               'nextButton'))

    class Window(PyQt.QMainWindow):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setGeometry(100, 100, 500, 300)
            self.setFixedSize(500, 300)
            self.setStyleSheet('''
                              background-color: #FFFFFF;
                              ''')

            self.stacked_widget = PyQt.QStackedWidget()
            self.setCentralWidget(self.stacked_widget)

            self.m_pages = {}

            self.register(MainWindow(), 'menu')
            self.register(QuizWindow(), 'quiz')

            self.goto('menu')

        def register(self, widget, name):
            self.m_pages[name] = widget
            self.stacked_widget.addWidget(widget)
            if isinstance(widget, PageWindow):
                widget.gotoSignal.connect(self.goto)

        @PyQtCore.pyqtSlot(str)
        def goto(self, name):
            if name in self.m_pages:
                widget = self.m_pages[name]
                self.stacked_widget.setCurrentWidget(widget)
                self.setWindowTitle(widget.windowTitle())

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
        answer_format = question.split("'")[1]
        question = question.split('@')
        working = question.pop(2)
        equation = question.pop(1)
        question = question.pop(0)
        equation_storage = []
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
                    equation_storage.append(total)
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

        string_answer = answer_format.replace('answer', str(answer)
                                              .rstrip('0').rstrip('.')).strip()
        for i in range(len(equation_storage)):
            working = working.replace(f'#{i}', str(equation_storage[i])
                                      .rstrip('0').rstrip('.'))

        working = working.replace('answer', str(answer).rstrip('0')
                                  .rstrip('.')).strip()
        float_answer = float(answer)

        return question, string_answer, float_answer, working

    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
    os.environ['QT_LOGGING_RULES'] = 'qt.qpa.*=false'

    numeracy = Numeracy()
    data = json.load(open('./data/keywords.json', 'r'))

    app = PyQt.QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec())
