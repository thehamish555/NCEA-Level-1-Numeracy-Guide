"""NCEA Level 1 Numeracy Guide (Questions and Answers).

The following program was made for a DT Assessment, It should
not be taken seriously and/or used to learn Level 1 Numeracy. Use at your own
risk, but you have been warned.

When run as __main__, this program generates questions and calculates the
answers. It asks the user the question through a GUI to which the user can
answer. Once the user submits their answer it shows the user if they were
right or wrong. It can also show you how to solve the question after the user
checks their answer.

DEV: Hamish Lester
VERSION: 0.5-Alpha
DATED: August 18, 2023
"""

import sys
import os
import random
import json
import re
import PyQt6.QtWidgets as PyQt
import PyQt6.QtGui as PyQtGui
import PyQt6.QtCore as PyQtCore
from threading import Thread
from deep_translator import GoogleTranslator
import time


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

        def initUI(self):
            self.UiComponets()

        def UiComponets(self):
            image = PyQtGui.QPixmap('./data/media/NZQA_Logo.png')\
                .scaledToHeight(150).scaledToHeight(150)
            self.imageLabel = PyQt.QLabel(self)
            self.imageLabel.setGeometry(PyQtCore.QRect(100, 50, image.width(),
                                                       image.height()))
            self.imageLabel.setPixmap(image)
            self.imageLabel.setObjectName('imageLabel')

            self.quizButton = PyQt.QPushButton(self)
            self.quizButton.setGeometry(PyQtCore.QRect(260, 225, 100, 30))
            self.quizButton.clicked.connect(
                self.make_handleButton('quizButton'))

            self.settingsButton = PyQt.QPushButton(self)
            self.settingsButton.setGeometry(PyQtCore.QRect(140, 225, 100, 30))
            self.settingsButton.clicked.connect(
                self.make_handleButton('settingsButton'))

        def make_handleButton(self, button):
            def handleButton():
                if button == 'quizButton':
                    self.goto('quiz')
                if button == 'settingsButton':
                    self.goto('settings')
            return handleButton

    class QuizWindow(PageWindow):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.UiComponents()

        def make_handleButton(self, button):
            def handleButton():
                if button == 'menuButton':
                    self.goto('menu')
                if button == 'nextButton':
                    self.question = self.nextQuestion
                    self.string_answers = self.nextString_ansers
                    self.float_answer = self.nextFloat_answer
                    self.working = self.nextWorking
                    Thread(target=self.get_next_question, daemon=True).start()
                    self.questionLabel.setText(self.question)
                    self.workingButton.hide()
                    self.nextButton.hide()
                    self.answerLabel.hide()
                    self.lineEdit.setReadOnly(False)
                    self.lineEdit.clear()
                    self.lineEdit.setFocus()
                    self.answerButton.setEnabled(True)
                    self.answerButton.setStyleSheet('''
                                                    QPushButton {
                                                        background-color:
                                                            #8DCCD2;
                                                    }
                                                    QPushButton:hover {
                                                        background-color:
                                                            #005A69;
                                                    }
                                                    ''')
                elif button == 'workingButton':
                    self.messageBox = PyQt.QMessageBox()
                    self.messageBox.setText(self.working)
                    with open('./data/nzqa.css', 'r') as fh:
                        self.messageBox.setStyleSheet(fh.read())
                    self.setWindowTitle(
                                        'NCEA Level 1 Numeracy Guide | Working'
                                        )
                    self.messageBox.exec()
                elif button == 'answerButton':
                    self.lineEdit.setReadOnly(True)
                    self.answerButton.setEnabled(False)
                    self.answerButton.setStyleSheet('''
                                                    QPushButton {
                                                        background-color:
                                                            #CADCDE;
                                                    }
                                                    QPushButton:hover {
                                                        background-color:
                                                            #005A69;
                                                    }
                                                    ''')
                    self.workingButton.show()
                    self.nextButton.show()
                    self.answerLabel.show()
                    self.user_answer = self.lineEdit.text().replace(',', '.')
                    try:
                        if float(self.user_answer) == self.float_answer:
                            self.answerLabel.setText('✓')
                            self.answerLabel.setStyleSheet('''
                                                           color: #21CC62;
                                                           font-size: 18pt;
                                                           ''')
                        else:
                            self.answerLabel.setText('x')
                            self.answerLabel.setStyleSheet('''
                                                           color: #CC2A21;
                                                           font-size: 18pt;
                                                           ''')
                    except ValueError:
                        string = self.user_answer.lower().strip().split()
                        for word in string:
                            try:
                                float(word)
                                string[string.index(word)] = word.strip('0')\
                                                                 .rstrip('.')
                            except ValueError:
                                pass
                        string = ' '.join(string)
                        for string_answer in self.string_answers:
                            if string.strip('0').rstrip('.') ==\
                              string_answer.strip('0').rstrip('.'):
                                self.answerLabel.setText('✓')
                                self.answerLabel.setStyleSheet('''
                                                               color: #21CC62;
                                                               font-size: 18pt;
                                                               ''')
                                return handleButton
                            else:
                                self.answerLabel.setText('x')
                                self.answerLabel.setStyleSheet('''
                                                               color: #CC2A21;
                                                               font-size: 18pt;
                                                               ''')
            return handleButton

        def loop_next_button(self):
            try:
                while True:
                    time.sleep(0.5)
                    if self.nextQuestion != self.question:
                        self.nextButton.setEnabled(True)
                        self.nextButton.setStyleSheet('''
                                                      QPushButton {
                                                          background-color:
                                                              #8DCCD2;
                                                      }
                                                      QPushButton:hover {
                                                          background-color:
                                                              #005A69;
                                                      }
                                                      ''')
                    else:
                        self.nextButton.setEnabled(False)
                        self.nextButton.setStyleSheet('''
                                                      QPushButton {
                                                          background-color:
                                                              #CADCDE;
                                                      }
                                                      QPushButton:hover {
                                                          background-color:
                                                              #005A69;
                                                      }
                                                      ''')
            except RuntimeError:
                pass

        def get_next_question(self):
            while True:
                try:
                    self.nextQuestion, self.nextString_ansers, \
                        self.nextFloat_answer, self.nextWorking = \
                        generate_question_and_answer()
                    break
                except ZeroDivisionError:
                    pass

        def UiComponents(self):
            while True:
                try:
                    self.question, self.string_answers, self.float_answer, \
                        self.working = generate_question_and_answer()
                    break
                except ZeroDivisionError:
                    pass
            # Thread(target=self.get_next_question, daemon=True).start()
            self.get_next_question()
            self.questionLabel = PyQt.QLabel(self.question, self)
            self.questionLabel.setGeometry(PyQtCore.QRect(15, 5, 470, 200))
            self.questionLabel.setStyleSheet('border-radius: 15px;')
            self.questionLabel.setAlignment(PyQtCore.Qt.AlignmentFlag
                                            .AlignHCenter
                                            | PyQtCore.Qt.AlignmentFlag.
                                            AlignTop)
            self.questionLabel.setWordWrap(True)

            self.answerButton = PyQt.QPushButton(self)
            self.answerButton.setGeometry(PyQtCore.QRect(380, 210, 100, 30))
            self.answerButton.clicked.connect(self.make_handleButton(
                                              'answerButton'))

            self.lineEdit = PyQt.QLineEdit(self, clearButtonEnabled=True)
            self.lineEdit.setGeometry(PyQtCore.QRect(20, 210, 350, 30))
            self.lineEdit.returnPressed.connect(self.answerButton.click)
            self.lineEdit.setFocus()

            self.answerLabel = PyQt.QLabel('', self)
            self.answerLabel.setGeometry(PyQtCore.QRect(348, 213, 20, 20))
            self.answerLabel.setObjectName('answerLabel')
            self.answerLabel.hide()

            self.menuButton = PyQt.QPushButton(self)
            self.menuButton.setGeometry(PyQtCore.QRect(5, 265, 100, 30))
            self.menuButton.clicked.connect(self.make_handleButton(
                                            'menuButton'))

            self.workingButton = PyQt.QPushButton(self)
            self.workingButton.setGeometry(PyQtCore.QRect(285, 265, 100, 30))
            self.workingButton.clicked.connect(self.make_handleButton(
                                               'workingButton'))
            self.workingButton.hide()

            self.nextButton = PyQt.QPushButton(self)
            self.nextButton.setGeometry(PyQtCore.QRect(395, 265, 100, 30))
            self.nextButton.clicked.connect(self.make_handleButton(
                                               'nextButton'))
            self.nextButton.hide()

            Thread(target=self.loop_next_button, daemon=True).start()

    class SettingsWindow(PageWindow):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.UiComponets()

        def UiComponets(self):
            self.menuButton = PyQt.QPushButton(self)
            self.menuButton.setGeometry(PyQtCore.QRect(5, 265, 100, 30))
            self.menuButton.clicked.connect(self.make_handleButton(
                                            'menuButton'))

            self.languageLabel = PyQt.QLabel(self)
            self.languageLabel.setGeometry(PyQtCore.QRect(5, 5, 150, 30))
            self.languageLabel.setStyleSheet('''
                                             border: 0px;
                                             font-size: 11pt;
                                             padding-left: 0px;
                                             ''')

            self.languageBox = PyQt.QComboBox(self)
            self.languageBox.setGeometry(PyQtCore.QRect(5, 35, 150, 30))
            options = ([('English', ''), ('Māori', 'data/languages/mi')])
            for i, (text, lang) in enumerate(options):
                self.languageBox.addItem(text)
                self.languageBox.setItemData(i, lang)
                if data['Data']['language'] == lang:
                    self.languageBox.setCurrentIndex(i)
            self.languageBox.currentIndexChanged.connect(
                self.make_handleButton('languageBox'))

        def make_handleButton(self, button):
            def handleButton():
                if button == 'menuButton':
                    self.goto('menu')
                elif button == 'languageBox':
                    language = self.languageBox.currentData()
                    data['Data']['language'] = language
                    json.dump(data, open('./data/data.json', 'w'), indent=4)
                    PyQt.QApplication.instance().removeTranslator(translator)
                translate()
            return handleButton

    class Window(PyQt.QMainWindow):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setGeometry(100, 100, 500, 300)
            self.setFixedSize(500, 300)

            self.stacked_widget = PyQt.QStackedWidget()
            self.setCentralWidget(self.stacked_widget)

            self.m_pages = {}
            self.MainWindow = MainWindow()
            self.QuizWindow = QuizWindow()
            self.SettingsWindow = SettingsWindow()
            self.register(self.MainWindow, 'menu')
            self.register(self.QuizWindow, 'quiz')
            self.register(self.SettingsWindow, 'settings')

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
        question = random.choice(list(data['Questions']))
        question_data = data['Questions'][question]
        question = question.split()
        equation = question_data['equation']
        string_formats = question_data['string_formats']
        working = question_data['working']
        num_of_names = 0
        num_of_nums = 0
        names = []
        for word in question:
            if word.__contains__('#name'):
                temp = int(re.sub(r'\D', '', word))
                if temp > num_of_names:
                    num_of_names = temp
            elif word.__contains__('#num'):
                temp = int(re.sub(r'\D', '', word))
                if temp > num_of_nums:
                    num_of_nums = temp
        for i in range(num_of_names):
            while True:
                temp = random.choice(data['Names'])
                if not names.__contains__(temp):
                    names.append(temp)
                    break
            for word in question:
                question[question.index(word)] = word.replace(f'#name{i+1}',
                                                              temp)
            equation = ''.join(equation).replace(f'#name{i+1}', temp)
            working = ''.join(working).replace(f'#name{i+1}', temp)
        question = ' '.join(question)
        numbers = numeracy.generate_numbers(num_of_nums,
                                            question_data['range_min'],
                                            question_data['range_max'])
        for i in range(num_of_nums):
            question = ''.join(question).replace(f'#num{i+1}', str(numbers[i]))
            equation = ''.join(equation).replace(f'#num{i+1}', str(numbers[i]))
            working = ''.join(working).replace(f'#num{i+1}', str(numbers[i]))
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
                        total = getattr(numeracy, functions[0])(
                                              numbers[0], numbers[1])
                    equation_storage.append(total)
                    numbers = [total]
                    functions = []
            answer = round(total, 2)
        else:
            function = equation.strip()
            try:
                answer = round(getattr(numeracy, function)(numbers), 2)
            except TypeError:
                answer = round(getattr(numeracy, function)(numbers[0],
                                                           numbers[1]), 2)
        string_answer = str(round(answer, 2)).strip('0').rstrip('.').strip()
        string_answers = []
        for string_format in string_formats:
            string_answers.append(string_format.replace('#answer',
                                                        string_answer))
        for i in range(len(equation_storage)):
            working = working.replace(f'#{i}', str(round(equation_storage[i],
                                      2)).strip('0').rstrip('.'))
        if answer < 0:
            string_answer = '-' + question_data['#answer']\
                .replace('#answer', str(abs(float(string_answer))))\
                .strip('0').rstrip('.')
        else:
            string_answer = question_data['#answer'].replace('#answer',
                                                             string_answer)
        working = working.replace('#answer', string_answer)
        if answer < 0:
            temp_string_answers = []
            for string_answer in string_answers:
                temp_string_answers.append('-'+string_answer.replace('-', ''))
            string_answers = temp_string_answers

        float_answer = round(float(answer), 2)
        try:
            for i in range(len(string_answers)):
                string_answers[i] = google_translator\
                    .translate(string_answers[i])
        except IndexError:
            pass
        question = google_translator.translate(question)
        working = google_translator.translate(working)

        return question, string_answers, float_answer, working

    def translate():
        google_translator.source = 'auto'
        if data['Data']['language']:
            translator.load(data['Data']['language'])
            PyQt.QApplication.instance().installTranslator(translator)
            google_translator.target = data['Data']['language']\
                .lstrip('data/languages/')
        else:
            google_translator.target = 'english'
        window.QuizWindow.question, \
            window.QuizWindow.working \
            = google_translator.translate(window.QuizWindow.question), \
            google_translator.translate(window.QuizWindow.working)
        for i in range(len(window.QuizWindow.string_answers)):
            window.QuizWindow.string_answers[i] = google_translator\
                .translate(window.QuizWindow.string_answers[i])
        window.QuizWindow.nextQuestion = window.QuizWindow.question
        google_translator.source = 'english'
        Thread(target=window.QuizWindow.get_next_question, daemon=True).start()
        window.QuizWindow.questionLabel.setText(window.QuizWindow.question)
        window.MainWindow.setWindowTitle(
            PyQt.QApplication.translate('MainWindow',
                                        'NCEA Level 1 Numeracy Guide | Home'))
        window.MainWindow.quizButton.setText(
            PyQt.QApplication.translate('MainWindow', 'Start Quiz'))
        window.MainWindow.settingsButton.setText(
            PyQt.QApplication.translate('MainWindow', 'Settings'))

        window.SettingsWindow.setWindowTitle(
            PyQt.QApplication.translate(
                'SettingsWindow', 'NCEA Level 1 Numeracy Guide | Settings'))
        window.SettingsWindow.languageLabel.setText(
            PyQt.QApplication.translate('SettingsWindow', 'Select Language'))
        window.SettingsWindow.menuButton.setText(
            PyQt.QApplication.translate('SettingsWindow', 'Main Menu'))

        window.QuizWindow.setWindowTitle(
            PyQt.QApplication.translate('QuizWindow',
                                        'NCEA Level 1 Numeracy Guide | Quiz'))
        window.QuizWindow.menuButton.setText(
            PyQt.QApplication.translate('QuizWindow', 'Main Menu'))
        window.QuizWindow.answerButton.setText(
            PyQt.QApplication.translate('QuizWindow', 'Check Answer'))
        window.QuizWindow.workingButton.setText(
            PyQt.QApplication.translate('QuizWindow', 'Show Working'))
        window.QuizWindow.nextButton.setText(
            PyQt.QApplication.translate('QuizWindow', 'Next Question'))
        window.QuizWindow.lineEdit.setPlaceholderText(
            PyQt.QApplication.translate('QuizWindow', 'Enter Answer...'))

    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

    os.environ['QT_LOGGING_RULES'] = 'qt.qpa.*=false'
    data = json.load(open('./data/data.json', 'r'))

    translator = PyQtCore.QTranslator()
    if data['Data']['language']:
        google_translator = GoogleTranslator(source='english', target=data
                                             ['Data']['language']
                                             .lstrip('data/languages/'))
    else:
        google_translator = GoogleTranslator(source='english',
                                             target='english')
    numeracy = Numeracy()

    app = PyQt.QApplication(sys.argv)

    window = Window()
    with open('./data/nzqa.css', 'r') as fh:
        window.setStyleSheet(fh.read())
    translate()
    Thread(target=window.show(), daemon=True).start()

    sys.exit(app.exec())
