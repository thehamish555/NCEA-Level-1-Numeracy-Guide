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
VERSION: 1.0
DATED: September 10, 2023
"""

# Imports - System
import sys
import os
import random
import json
import re
import time

# Imports - PyQt
import PyQt6.QtWidgets as PyQt
import PyQt6.QtGui as PyQtGui
import PyQt6.QtCore as PyQtCore

# Imports - Other
from threading import Thread
from deep_translator import GoogleTranslator


class Numeracy:
    """Used to generate and calculate math equations for NCEA Level 1 Numeracy.

    Called with Numeracy()
    Returns a Numeracy Class
    """

    def __init__(self):
        """Create the class and all required variables.

        Called with Numeracy()
        """
        self.numbers = []  # Used to store the list of generated numbers
        self.last_added = None  # Stores the last added value
        self.last_subtracted = None  # Stores the last subtracted value
        self.last_multiplied = None  # Stores the last multiplied value
        self.last_divided = None  # Stores the last divided value

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
        Returns Last Values calculated by the class in dictionary format
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
        self.numbers = []  # Deletes previous numbers
        for i in range(amount):  # Generates the amount of numbers asked for
            # Generates a random number based on the given range
            self.numbers.append(random.randint(min, max))
        return self.numbers

    @name('+')
    def addition(self, *args):
        """Add a list of numbers together, Eg ([1, 2, 3], 4) returns 10.

        Called with Numeracy.addition(a, b, c...)
        Returns the sum of all numbers provided
        """
        try:
            total = 0   # Will return 0 if no numbers are added together
            for arg in list(args):  # Sets all values as a list
                try:
                    total += sum(arg)  # If Arg is a list, add the sum to total
                except TypeError:
                    total += arg  # If Arg is a number, add the number to total
        except TypeError:
            # Will only accept (1, 2, 3) or ([1, 2, 3]) not ([[1, 2], [3, 4]])
            raise Exception('Invalid Entry, Lists inside Lists do not work!')
        self.last_added = total  # Sets the last added value to be the total
        return self.last_added

    @name('-')
    def subtraction(self, a, b):
        """Subtract one number from another, Eg (10, 3) returns 7.

        Called with Numeracy.subtraction(a, b)
        Returns a - b
        """
        self.last_subtracted = a - b  # Subtracts b from a and sets last value
        return self.last_subtracted

    @name('×')
    def multiplication(self, *args):
        """Multiply a list of numbers together, Eg ([2, 3], 6) returns 36.

        Called with Numeracy.multiplication(a, b, c...)
        Returns the multiple of all numbers provided
        """
        try:
            total = 1  # Will return 1 if no numbers are multiplied together
            for arg in list(args):  # Sets all values as a list
                try:
                    for num in arg:  # Multiplies all values in a list together
                        total = total * num
                except TypeError:
                    # If Arg is a number, multiply number by current total
                    total = total * arg
        except TypeError:
            # Will only accept (1, 2, 3) or ([1, 2, 3]) not ([[1, 2], [3, 4]])
            raise Exception('Invalid Entry, Lists inside Lists do not work!')
        # Sets the last multiplied value to be the total
        self.last_multiplied = total
        return self.last_multiplied

    @name('÷')
    def division(self, a, b):
        """Divide one number by another, Eg (6, 3) returns 2.

        Called with Numeracy.division(a, b)
        Returns a / b
        """
        self.last_divided = a / b  # Divides a by b and sets last value
        return self.last_divided


# Checks for --help as an argument when script is run
if len(sys.argv) == 2 and sys.argv[1] == '--help':
    """Prints the class Numeracy methods and their equivalent docstrings.

    Run with python3 main.py --help
    or equivalent
    """
    n = '\n'  # Sets n to be \n as it cant be used in .replace()
    # The \n is used to ensure formatting between doc-strings and newlines

    # Prints the script doc-string or states no information if not found
    print(f'{__doc__.strip()}\n',) if __doc__ else \
        print('No script information\n')
    print('\033[1mContained Classes and Functions\033[0m')
    try:  # Prints the class doc-string if it exists
        print(f'''    \033[1mClass Numeracy:\033[0m
        {Numeracy.__doc__.replace(n, n + '    ')}''')
    except AttributeError:  # Otherwise states there is no doc-string
        print('''    \033[1mClass Numeracy:\033[0m
        No information provided''')
    for method in dir(Numeracy):  # Goes through all the methods in the class
        if not method.startswith('__'):  # Won't accept inbuilt methods
            try:  # Prints the method doc-string if it exists
                print(f'''        \033[1m- Method {method}\033[0m
            {getattr(Numeracy, method).__doc__.replace(n, n + '    ')}''')
            except AttributeError:  # Otherwise states there is no doc-string
                print(f'''        \033[1m- Method {method}\033[0m
            No information provided''')
elif __name__ == '__main__':
    """Will only run this code if run by main.py, that way
    People can use the class and functions without running the code for this
    program.
    """
    class PageWindow(PyQt.QMainWindow):
        """Used as an object to generate a new page for the PyQt GUI.
        Do not directly call this class, as its used as an object for GUI
        classes. For use of this class, when creating a new GUI page, set the
        object to be PageWindow, Eg class MainWindow(PageWindow):
        """
        gotoSignal = PyQtCore.pyqtSignal(str)  # Creates a signal for the pages

        def goto(self, name):  # When goto is called, go to the selected page
            self.gotoSignal.emit(name)  # States what page to go to

    class MainWindow(PageWindow):
        """Used to create the Home Screen that is displayed when the GUI opens.
        Do not directly call this class outside of the root window class, as it
        is used as a sub-page of the window. For use of this class, inside the
        root window, call the class and assign to a variable.
        Eg self.MainWindow = MainWindow()
        after calling the class, register the class to the list GUI of pages
        """
        def __init__(self):
            super().__init__()  # Loads the class into the page list
            self.initUI()  # Loads the UI

        def initUI(self):
            self.UiComponents()  # Loads the components of the UI

        def make_handleButton(self, button):  # Checks what button was pressed
            def handleButton():  # Callback to load selected page
                if button == 'quizButton':  # If button is quizButton
                    self.goto('quiz')  # Show quiz page
                if button == 'settingsButton':  # If button is settingsButton
                    self.goto('settings')  # Show settings page
            return handleButton

        def UiComponents(self):  # Stores the widgets that need to be displayed
            image = PyQtGui.QPixmap('./data/media/NZQA_Logo.png')\
                .scaledToHeight(150).scaledToHeight(150)  # NZQA Logo
            self.imageLabel = PyQt.QLabel(self)  # Create a label for the image
            # Define location and size on the UI (x, y, w, h)
            self.imageLabel.setGeometry(PyQtCore.QRect(100, 50, image.width(),
                                                       image.height()))
            self.imageLabel.setPixmap(image)  # Show image on label
            self.imageLabel.setObjectName('normalLabel')  # Removes the CSS

            self.quizButton = PyQt.QPushButton(self)  # Button for quiz
            # Define location and size on the UI (x, y, w, h)
            self.quizButton.setGeometry(PyQtCore.QRect(260, 225, 100, 30))
            self.quizButton.clicked.connect(
                self.make_handleButton('quizButton'))  # On press callback

            self.settingsButton = PyQt.QPushButton(self)  # Button for settings
            # Define location and size on the UI (x, y, w, h)
            self.settingsButton.setGeometry(PyQtCore.QRect(140, 225, 100, 30))
            self.settingsButton.clicked.connect(
                self.make_handleButton('settingsButton'))  # On press callback

    class QuizWindow(PageWindow):
        """Used to create the Quiz Screen that is displayed when the user
        clicks the quiz button. Do not directly call this class outside of the
        root window class, as it is used as a sub-page of the window. For use
        of this class, inside the root window, call the class and assign to a
        variable Eg self.QuizWindow = QuizWindow() after calling the class,
        register the class to the list GUI of pages
        """
        def __init__(self):
            super().__init__()  # Loads the class into the page list
            self.initUI()  # Loads the UI

        def initUI(self):
            self.UiComponents()  # Loads the components of the UI

        def make_handleButton(self, button):  # Checks what button was pressed
            def handleButton():  # Callback to load selected page
                if button == 'menuButton':  # If button is menuButton
                    self.goto('menu')  # Show menu page
                if button == 'nextButton':  # If button is nextButton
                    # Set the current question to next question
                    self.question = self.nextQuestion
                    self.string_answers = self.nextString_ansers
                    self.float_answer = self.nextFloat_answer
                    self.working = self.nextWorking
                    # Generate next question in background
                    Thread(target=self.get_next_question, daemon=True).start()
                    self.questionLabel.setText(self.question)  # New Question
                    self.workingButton.hide()  # Re-hide the working button
                    self.nextButton.hide()  # Re-hide next button
                    self.answerLabel.hide()  # Re-hide the answer label
                    self.lineEdit.setReadOnly(False)  # Enable the text entry
                    self.lineEdit.clear()  # Delete text in text entry
                    self.lineEdit.setFocus()  # Set focus on text entry
                    self.answerButton.setEnabled(True)  # Enable answer button
                    # Change the answer button CSS to show its enabled
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
                elif button == 'workingButton':  # If button us workingButton
                    self.messageBox = PyQt.QMessageBox()  # Create a messageBox
                    self.messageBox.setText(self.working)  # Show the working
                    # Load the CSS for the messageBox from the CSS file
                    with open('./data/nzqa.css', 'r') as fh:
                        self.messageBox.setStyleSheet(fh.read())
                    # Set window title to show its the working window
                    self.setWindowTitle(
                                        'NCEA Level 1 Numeracy Guide | Working'
                                        )
                    # Display the messageBox
                    self.messageBox.exec()
                elif button == 'answerButton':  # If button is answerButton
                    self.lineEdit.setReadOnly(True)  # Disable the text entry
                    self.answerButton.setEnabled(False)  # Answer button off
                    # Change the answer button CSS to show its disabled
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
                    self.workingButton.show()  # Show the working button
                    self.nextButton.show()  # Show the next button
                    self.answerLabel.show()  # Show the answer label
                    # Get the answer the user entered from the text entry
                    self.user_answer = self.lineEdit.text().replace(',', '.')
                    try:  # Check if just a number was entered
                        # If user answer and answer match
                        if float(self.user_answer) == self.float_answer:
                            # Display a tick and set color to green
                            self.answerLabel.setText('✓')
                            self.answerLabel.setStyleSheet('''
                                                           color: #21CC62;
                                                           font-size: 18pt;
                                                           ''')
                        else:  # If user answer doesn't match answer
                            # Display a cross and set color to red
                            self.answerLabel.setText('x')
                            self.answerLabel.setStyleSheet('''
                                                           color: #CC2A21;
                                                           font-size: 18pt;
                                                           ''')
                    except ValueError:  # Otherwise check if string is allowed
                        # Get the user answer as a string and split
                        string = self.user_answer.lower().strip().split()
                        for word in string:  # loop through string
                            try:
                                float(word)  # If word is a number
                                # Remove excess zeros at the end after the
                                # decimal to pretend the string is a number
                                # Eg 1.0000000000 = 1 or 1.500000 = 1.5
                                string[string.index(word)] = word.strip('0')\
                                                                 .rstrip('.')
                            except ValueError:  # If word isn't a number ignore
                                pass
                        # Turn split/modified string back to a normal string
                        string = ' '.join(string)
                        # Loop through valid answers
                        for string_answer in self.string_answers:
                            # If user answer matches a string answer
                            if string.strip('0').rstrip('.') ==\
                              string_answer.strip('0').rstrip('.'):
                                # Display a tick and set color to green
                                self.answerLabel.setText('✓')
                                self.answerLabel.setStyleSheet('''
                                                               color: #21CC62;
                                                               font-size: 18pt;
                                                               ''')
                                return handleButton
                            else:  # If user answer doesn't match a answer
                                # Display a cross and set color to reds
                                self.answerLabel.setText('x')
                                self.answerLabel.setStyleSheet('''
                                                               color: #CC2A21;
                                                               font-size: 18pt;
                                                               ''')
            return handleButton

        def loop_next_button(self):
            """Constantly checks if a new question has been generated.

            A thread is used to constantly loop and check if a new question has
            been generated by checking if the current question matches the next
            question. It is possible for this to stop working, but the
            likelihood of this happening is statistically impossible due to
            random nature of the generated questions. If the next question has
            not been generated, the user can not go to the next question until
            its generated.
            """
            try:
                while True:
                    time.sleep(0.5)  # Prevents hanging and makes script faster
                    # If next question is not the same as current question
                    if self.nextQuestion != self.question:
                        self.nextButton.setEnabled(True)  # Enable next button
                        # Changes color of button back to original colors
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
                    else:  # If current question is the same as next question
                        self.nextButton.setEnabled(False)  # Disable button
                        # Changes color of button to a lighter (disabled) color
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
            except RuntimeError:  # When script closes mid loop ignore crash
                pass

        def get_next_question(self):
            """Gets next question and answer ready in the background.

            Using a thread, the program can generate the next question so that
            if a translation is needed, the next question will translate while
            the user is entering their answer. This allows the user to go to
            the next question without it feeling slow and freezing.
            """
            while True:  # Loop through until a valid question is generated
                try:  # Catch invalid questions
                    # Generate and assign values to their next equivalent
                    self.nextQuestion, self.nextString_ansers, \
                        self.nextFloat_answer, self.nextWorking = \
                        generate_question_and_answer()
                    break  # If question is valid stop loop
                except ZeroDivisionError:  # If question is invalid try again
                    pass

        def UiComponents(self):
            """Load all the widgets for the page.

            This will only run once on the creation of the PageWindow, because
            of this, we generate the first and next question so that when the
            window is shown, it has the first two questions ready. This is
            because the window wont show until all PageWindow classes have
            finished loading. Other than generating questions, all the widgets
            are loaded and placed in their correct spots
            """
            while True:  # Loop through until a valid question is generated
                try:  # Catch invalid questions
                    # Generate the starter question and assign to variables
                    self.question, self.string_answers, self.float_answer, \
                        self.working = generate_question_and_answer()
                    break  # If question is valid stop loop
                except ZeroDivisionError:  # If question is invalid try again
                    pass
            # Get the next question ready so that the next loop can start
            self.get_next_question()
            # Create the question label and show the first question
            self.questionLabel = PyQt.QLabel(self.question, self)
            # Define location and size on the UI (x, y, w, h)
            self.questionLabel.setGeometry(PyQtCore.QRect(15, 5, 470, 200))
            # Change the CSS border-radius to a more rounded border
            self.questionLabel.setStyleSheet('border-radius: 15px;')
            # Align the text at the top and center
            self.questionLabel.setAlignment(PyQtCore.Qt.AlignmentFlag
                                            .AlignHCenter
                                            | PyQtCore.Qt.AlignmentFlag.
                                            AlignTop)
            # Make the text drop a line at the edge of the border
            self.questionLabel.setWordWrap(True)

            # Create the answer button that the user presses to check answer
            self.answerButton = PyQt.QPushButton(self)
            # Define location and size on the UI (x, y, w, h)
            self.answerButton.setGeometry(PyQtCore.QRect(380, 210, 100, 30))
            # On press callback
            self.answerButton.clicked.connect(self.make_handleButton(
                                              'answerButton'))

            # Create the text entry for the user to enter their answer
            # Have an x button at the end to remove all text if needed
            self.lineEdit = PyQt.QLineEdit(self, clearButtonEnabled=True)
            # Define location and size on the UI (x, y, w, h)
            self.lineEdit.setGeometry(PyQtCore.QRect(20, 210, 350, 30))
            # On key press return (enter) act like answer button was pressed
            self.lineEdit.returnPressed.connect(self.answerButton.click)
            # Set focus so user can type straight away
            self.lineEdit.setFocus()

            # Create the answer label that tells the user if they got it or not
            self.answerLabel = PyQt.QLabel('', self)
            # Define location and size on the UI (x, y, w, h)
            self.answerLabel.setGeometry(PyQtCore.QRect(348, 213, 20, 20))
            # Removes normal CSS and adds custom CSS for the answer label
            self.answerLabel.setObjectName('answerLabel')
            # Hides by default because it covers the x button in the text entry
            self.answerLabel.hide()

            # Create the menu button so the user can go back to the menu
            self.menuButton = PyQt.QPushButton(self)
            # Define location and size on the UI (x, y, w, h)
            self.menuButton.setGeometry(PyQtCore.QRect(5, 265, 100, 30))
            # On press callback
            self.menuButton.clicked.connect(self.make_handleButton(
                                            'menuButton'))

            # Create the working button so the user can see the worked answer
            self.workingButton = PyQt.QPushButton(self)
            # Define location and size on the UI (x, y, w, h)
            self.workingButton.setGeometry(PyQtCore.QRect(285, 265, 100, 30))
            # On press callback
            self.workingButton.clicked.connect(self.make_handleButton(
                                               'workingButton'))
            # Hides by default since the current question hasn't been answered
            self.workingButton.hide()

            # Create the next button so the user can go to the next question
            self.nextButton = PyQt.QPushButton(self)
            # Define location and size on the UI (x, y, w, h)
            self.nextButton.setGeometry(PyQtCore.QRect(395, 265, 100, 30))
            # On press callback
            self.nextButton.clicked.connect(self.make_handleButton(
                                               'nextButton'))
            # Hides by default since the current question hasn't been answered
            self.nextButton.hide()

            # Start the loop checking for new question in the background
            Thread(target=self.loop_next_button, daemon=True).start()

    class SettingsWindow(PageWindow):
        """Used to create the Settings Screen that is displayed when the user
        clicks the settings button. Do not directly call this class outside of
        the root window class, as it is used as a sub-page of the window. For
        use of this class, inside the root window, call the class and assign to
        a variable Eg self.SettingsWindow = SettingsWindow() after calling the
        class, register the class to the list GUI of pages
        """
        def __init__(self):
            super().__init__()  # Loads the class into the page list
            self.initUI()  # Loads the UI

        def initUI(self):
            self.UiComponents()  # Loads the components of the UI

        def make_handleButton(self, button):  # Checks what button was pressed
            def handleButton():  # Callback to load selected page
                if button == 'menuButton':  # If button is menuButton
                    self.goto('menu')  # Show menu/home page
                elif button == 'languageBox':  # If button is languageBox
                    language = self.languageBox.currentData()  # Get box value
                    # Save the language as the selected language for reloads
                    data['Data']['language'] = language
                    json.dump(data, open('./data/data.json', 'w'), indent=4)
                    # Delete the current translation of widgets
                    PyQt.QApplication.instance().removeTranslator(translator)
                    translate()  # Re-translate the program with the language
            return handleButton

        def UiComponents(self):  # Stores the widgets that need to be displayed
            self.menuButton = PyQt.QPushButton(self)  # Button for menu
            # Define location and size on the UI (x, y, w, h)
            self.menuButton.setGeometry(PyQtCore.QRect(5, 265, 100, 30))
            self.menuButton.clicked.connect(self.make_handleButton(
                                            'menuButton'))  # On press callback

            self.languageLabel = PyQt.QLabel(self)  # Label for language select
            # Define location and size on the UI (x, y, w, h)
            self.languageLabel.setGeometry(PyQtCore.QRect(5, 5, 150, 30))
            self.languageLabel.setObjectName('normalLabel')  # Removes the CSS

            self.languageBox = PyQt.QComboBox(self)  # ComboBox for languages
            # Define location and size on the UI (x, y, w, h)
            self.languageBox.setGeometry(PyQtCore.QRect(5, 35, 150, 30))
            # List of languages that can be used, and their translations
            options = ([
                        ('English', ''),
                        ('Māori', 'data/languages/mi')
                      ])
            # Go through all the languages and add them to the comboBox
            for i, (text, lang) in enumerate(options):
                self.languageBox.addItem(text)  # Add the language name
                self.languageBox.setItemData(i, lang)  # Add the data location
                # If selected language matches a language in the loop
                if data['Data']['language'] == lang:
                    self.languageBox.setCurrentIndex(i)  # Display on load
            self.languageBox.currentIndexChanged.connect(
                self.make_handleButton('languageBox'))  # On change callback

    class Window(PyQt.QMainWindow):
        """Create the main window for pages to be added to.

        This class is called by the user to create and display the main window.
        It loads the pages and all their objects, then displays the menu. This
        is done by registering each page to a slot, and then calling and
        displaying the slot when the goto function is called. For use of this,
        create all page classes elsewhere and use the register function, the
        rest is handled through automation and callbacks.

        Example
        self.MainWindow = MainWindow()  # Menu page class
        self.register(self.MainWindow, 'menu')  # Register the page as 'menu'
        """
        def __init__(self, parent=None):
            super().__init__(parent)  # Create a window with QMainWindow Object
            self.setGeometry(100, 100, 500, 300)  # Set the page
            self.setFixedSize(500, 300)  # Set fixed window size

            # Allow multiple widgets to be layered and display only one
            self.stacked_widget = PyQt.QStackedWidget()
            # Display page with the stacked widgets so they can render
            self.setCentralWidget(self.stacked_widget)

            self.m_pages = {}  # A list of pages
            self.MainWindow = MainWindow()  # Generate Menu page
            self.QuizWindow = QuizWindow()  # Generate Quiz page
            self.SettingsWindow = SettingsWindow()  # Generate Settings page
            self.register(self.MainWindow, 'menu')  # Register Menu page
            self.register(self.QuizWindow, 'quiz')  # Register Quiz page
            self.register(self.SettingsWindow, 'settings')  # Register settings

            self.goto('menu')  # Display menu first

        def register(self, widget, name):  # Register a page to the Window
            self.m_pages[name] = widget  # Add the page to list of pages
            self.stacked_widget.addWidget(widget)  # Add the page to the UI
            if isinstance(widget, PageWindow):  # If it uses PageWindow object
                widget.gotoSignal.connect(self.goto)  # Allow changing to page

        @PyQtCore.pyqtSlot(str)  # Go to page given string
        def goto(self, name):  # Takes string name of page
            if name in self.m_pages:  # If page is in list of pages
                widget = self.m_pages[name]  # Get the widgets of the page
                self.stacked_widget.setCurrentWidget(widget)  # Display page
                self.setWindowTitle(widget.windowTitle())  # Change page title

    def generate_question_and_answer():
        """Create a question and an answer.

        Called with generate_question_and_answer()
        Returns question, string_answers, float_answer and working
        """
        question = random.choice(list(data['Questions']))  # Picks a question
        question_data = data['Questions'][question]  # Gets the question data
        question = question.split()  # Splits the question into a list
        equation = question_data['equation']  # Gets the equation used to solve
        string_formats = question_data['string_formats']  # Gets string answers
        working = question_data['working']  # Gets the worked answer
        num_of_names = 0  # Sets number of names in question as 0
        num_of_nums = 0  # Sets number of numbers in question as 0
        names = []  # Used to store names
        for word in question:  # Go through each word in the question
            if word.__contains__('#name'):  # If word has #name in it
                temp = int(re.sub(r'\D', '', word))  # Get the numbers only
                # If the number is greater than the current number of names
                if temp > num_of_names:
                    num_of_names = temp  # Set the number of names to number
            elif word.__contains__('#num'):  # If word has #num in it
                temp = int(re.sub(r'\D', '', word))  # Get the numbers only
                # If the number is greater than the current number of numbers
                if temp > num_of_nums:
                    num_of_nums = temp  # Set the number of numbers to number
        for i in range(num_of_names):  # Loop based on how many names there are
            while True:  # Loop until list of names are all unique
                temp = random.choice(data['Names'])  # Get a random name
                if not names.__contains__(temp):  # Check if name is unique
                    names.append(temp)  # Add name to list of names
                    break  # Break loop
            for word in question:  # Go through each word in the question
                question[question.index(word)] = word.replace(f'#name{i+1}',
                                                              temp)  # Set name
            # Set names in the equation and working
            equation = ''.join(equation).replace(f'#name{i+1}', temp)
            working = ''.join(working).replace(f'#name{i+1}', temp)
        # Join the question together as a string again
        question = ' '.join(question)
        # Generate numbers given how many and mix/max range
        numbers = numeracy.generate_numbers(num_of_nums,
                                            question_data['range_min'],
                                            question_data['range_max'])
        for i in range(num_of_nums):  # Loop based on how many numbers needed
            # Set numbers in the question, equation and working
            question = ''.join(question).replace(f'#num{i+1}', str(numbers[i]))
            equation = ''.join(equation).replace(f'#num{i+1}', str(numbers[i]))
            working = ''.join(working).replace(f'#num{i+1}', str(numbers[i]))
        equation_storage = []  # Store all calculations
        if len(equation.split()) > 1:  # If equation is longer than one word
            numbers = []  # List for storing numbers
            functions = []  # List for storing functions
            for word in equation.split():  # Go through each word in equation
                """
                This section here loops through all the words in the equation.
                It gets all the numbers and functions and calculates a value.
                It does this by reading the equation left to right, and doing
                the required math function, taking the outcome and using that
                in the next calculation. An example of this is below

                1 addition 2 multiplication 3 -> 3 multiplicaction 3 -> 9

                1 and 2 are added to make 3, than multiplied by 3.
                """
                try:  # Check for errors
                    int(word)  # Check if word is a number
                    numbers.append(float(word))  # Add float of number to list
                except ValueError:  # If not a number
                    functions.append(word)  # Add word as function
                # Check to make sure lists have at least two numbers and a
                # function otherwise continue getting words
                if len(functions) > 0 and len(numbers) > 1:
                    try:  # Check for errors
                        # Run the Numeracy function in the function list with
                        # all the given numbers in the number list
                        total = getattr(numeracy, functions[0])(numbers)
                    except TypeError:  # If function only takes two numbers
                        # Run the Numeracy function in the function list with
                        # two of the given numbers in the number list
                        total = getattr(numeracy, functions[0])(
                                              numbers[0], numbers[1])
                    equation_storage.append(total)  # Store number for later
                    numbers = [total]  # Set numbers list to only be new number
                    functions = []  # Clear functions list
            answer = round(total, 2)  # Round answer to 2dp using final total
        else:  # If equation is one word
            """
            This section does the same as above, but instead of running through
            the equation left to right, it just do the math given one function.
            An example of this is below

            Question: what is 5 x 3?
            Equation: multiplication -> 15

            Code multiplies 5 and 3 without being told to use those numbers in
            the equation
            """
            function = equation.strip()  # Strip all spaces in the equation
            try:  # Check for errors
                # Run the Numeracy function from the equation and round to 2dp
                answer = round(getattr(numeracy, function)(numbers), 2)
            except TypeError:  # If function only takes two numbers
                # Run the Numeracy function from the equation and round to 2dp
                answer = round(getattr(numeracy, function)(numbers[0],
                                                           numbers[1]), 2)
        # Convert answer to string and remove .00000000 etc from the end
        string_answer = str(round(answer, 2)).strip('0').rstrip('.').strip()
        string_answers = []  # A list to store string answers
        for string_format in string_formats:  # Go through string formats
            # Replace answer in the string format with the actual answer and
            # append to list of strings answers
            string_answers.append(string_format.replace('#answer',
                                                        string_answer))
        for i in range(len(equation_storage)):  # Go through equation storage
            # Replace all numbers in the working that show previously
            # calculated numbers, Eg add 5 and 3 (5+3) and add 10 (8+10) = 18
            working = working.replace(f'#{i}', str(round(equation_storage[i],
                                      2)).strip('0').rstrip('.'))
        if answer < 0:  # If answer is negative
            # Get the absolute (positive) number of the answer and set that as
            # the string answer. Then add a negative symbol to the front of
            # the string answer. Done so $-5 turns into -$5
            string_answer = '-' + question_data['#answer']\
                .replace('#answer', str(abs(float(string_answer))))\
                .strip('0').rstrip('.')
        else:  # If answer is positive
            # Set string answer to be answer format, done so the displayed
            # Answer uses the appropriate units, Eg $5 instead of 5
            string_answer = question_data['#answer'].replace('#answer',
                                                             string_answer)
        # Add answer with proper units to worked answer
        working = working.replace('#answer', string_answer)
        if answer < 0:  # If answer is negative
            temp_string_answers = []  # A list of temp string answers
            # Go through each string answer and attach a negative symbol
            # To the front and remove the others
            for string_answer in string_answers:
                temp_string_answers.append('-'+string_answer.replace('-', ''))
            # Set string answers to modified answers
            string_answers = temp_string_answers

        float_answer = round(float(answer), 2)  # Float and round answer to 2dp
        try:  # Check for errors
            # Go through each string answer
            for i in range(len(string_answers)):
                # Translate the string answer and replace it in the list
                string_answers[i] = google_translator\
                    .translate(string_answers[i])
        except IndexError:  # If no string answers for question
            pass  # Ignore
        question = google_translator.translate(question)  # Translate question
        working = google_translator.translate(working)  # Translate working

        return question, string_answers, float_answer, working

    def translate():
        """Translate the widgets, questions and answers.

        This function will run when the program loads, and when the language is
        changed. You should not need to call this function as it will change
        all text based on the language stored in the data file. If you do call
        this function, nothing will change unless you changed the language
        manually. If there is no .qm file for the given language, then the
        widgets will not change/be blank but the google translator might still
        work.

        Called with translate()
        """
        # If swapping between two non-English languages, detect the language
        google_translator.source = 'auto'
        if data['Data']['language']:  # If a language besides English is used
            translator.load(data['Data']['language'])  # Load the .qm file
            # Install the language data to the application instance
            PyQt.QApplication.instance().installTranslator(translator)
            google_translator.target = data['Data']['language']\
                .lstrip('data/languages/')  # Set target to selected language
        else:  # If English is being used
            google_translator.target = 'english'  # Set target to English
        try:  # Check for errors
            # Go through each string answer
            for i in range(len(window.QuizWindow.string_answers)):
                # Translate the string answer and replace it in the list
                window.QuizWindow.string_answers[i] = google_translator\
                    .translate(window.QuizWindow.string_answers[i])
        except IndexError:  # If no string answers for question
            pass  # Ignore
        # Translate the current question and working into new language
        window.QuizWindow.question, \
            window.QuizWindow.working \
            = google_translator.translate(window.QuizWindow.question), \
            google_translator.translate(window.QuizWindow.working)
        # Loop through the string answers and translate them
        for i in range(len(window.QuizWindow.string_answers)):
            window.QuizWindow.string_answers[i] = google_translator\
                .translate(window.QuizWindow.string_answers[i])
        # Remove the next question and load a new one with translation
        window.QuizWindow.nextQuestion = window.QuizWindow.question
        # Once translation is over, translate from English as the questions are
        # in English and will also be faster than detecting the language
        google_translator.source = 'english'
        # Since next question was removed, get a new question with translations
        Thread(target=window.QuizWindow.get_next_question, daemon=True).start()
        """The code below updates every widget in the program to show either
        the default string (English) or the translated equivalent if a
        language is loaded into the program.
        """
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

    # Clears the console on whatever device is used
    if os.name == 'posix':  # Linux/Mac
        os.system('clear')
    else:  # Windows/Other
        os.system('cls')

    # Disables any QT warnings that may appear on some devices
    os.environ['QT_LOGGING_RULES'] = 'qt.qpa.*=false'
    # Loads the data file containing names, questions and user data
    data = json.load(open('./data/data.json', 'r'))

    translator = PyQtCore.QTranslator()  # Creates a translation tool for PyQt
    if data['Data']['language']:  # Checks if user has set a different language
        # Creates a google translator of the selected language for questions
        google_translator = GoogleTranslator(source='english', target=data
                                             ['Data']['language']
                                             .lstrip('data/languages/'))
    else:  # If user has no language selected
        # Create a google translator that does English to English for questions
        google_translator = GoogleTranslator(source='english',
                                             target='english')
    numeracy = Numeracy()  # Loads the Numeracy class so math can be done

    app = PyQt.QApplication(sys.argv)  # Creates a Qt Application

    window = Window()  # Creates the root window with the Window class
    with open('./data/nzqa.css', 'r') as fh:  # Opens the custom style sheets
        window.setStyleSheet(fh.read())  # Sets the window to have the CSS
    translate()  # Translates all widgets in the application

    # Starts a thread for the root window so that other functions can be run as
    # threads. This is done to prevent freezing as run in the background
    Thread(target=window.show(), daemon=True).start()

    sys.exit(app.exec())  # Cleanly exit the program and clear all resources
