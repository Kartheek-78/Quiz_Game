try:
    import random

    class PythonQuizGame:
        def __init__(self, questions):
            self.questions = questions
            self.score = 0

        def ask_question(self, question, options):
            print(question)
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            user_answer = input("Your answer (1, 2, 3, or 4): ")
            return int(user_answer) - 1

        def run_quiz(self):
            for question, options, correct_answer in self.questions:
                user_choice = self.ask_question(question, options)
                if options[user_choice] == correct_answer:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Incorrect! The correct answer is: {correct_answer}\n")

            print(f"Quiz completed. Your final score is: {self.score}/{len(self.questions)}")

    # Python-related questions with four options
    python_questions = [
        ("What is Python?", ["A snake", "A programming language", "A type of lizard", "An operating system"], "A programming language"),
        ("Which keyword is used to define a function in Python?", ["func", "define", "def", "function"], "def"),
        ("What is the purpose of the 'if' statement?", ["To declare a variable", "To perform a loop", "To make decisions in code", "To import modules"], "To make decisions in code"),
        ("Which data type is used to store a sequence of characters in Python?", ["int", "str", "float", "char"], "str"),
        ("What does the 'len()' function do?", ["Returns the length of a list or string", "Calculates logarithm", "Converts to lowercase", "Finds maximum value"], "Returns the length of a list or string"),
        ("In Python, how do you comment a single line of code?", ["// This is a comment", "# This is a comment", "/* This is a comment */", "// This is not a comment"], "# This is a comment"),
        ("Which module is used for working with dates and times in Python?", ["datetime", "time", "date", "calendar"], "datetime"),
        ("What is the purpose of the 'else' statement?", ["To handle exceptions", "To define a block of code to be executed if the condition is false", "To create a loop", "To break out of a loop"], "To define a block of code to be executed if the condition is false"),
        ("How do you open a file in Python?", ["open(file_name)", "read(file_name)", "file_open(file_name)", "load(file_name)"], "open(file_name)"),
        ("What is a Python list?", ["A collection of ordered elements", "A way to write comments", "A mathematical operator", "A type of loop"], "A collection of ordered elements"),
    ]

    # Shuffle Python questions to randomize quiz order
    random.shuffle(python_questions)

    # Create and run the Python quiz
    python_quiz = PythonQuizGame(python_questions)
    python_quiz.run_quiz()
except ValueError:
    print(f"Please enter only valid numeric options")
except IndexError:
    print(f"Please enter only options given 1/2/3/4")
