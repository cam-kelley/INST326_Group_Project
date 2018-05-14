import random


class Flashcard:
    def __init__(self):
        print("Welcome to flashcards!")
        print("Please input questions and their corresponding answers. When finished, enter 'DONE' into the "
              "'Your question' field.")
        print("You can also upload a CSV file to this program in the format of: questions in the first column"
              "and answers in the second column.")
        self.flashcard = []
        self.correct = 0

    def user_input(self):
        upload = input('Would you like to upload a CSV file? Enter "Yes" or "No": ')
        while True:
            if upload == "No":
                question = str(input("Your question: "))
                if question == 'DONE':
                    break
                answer = str(input("Your answer: "))
                self.flashcard.append([question, answer, -1])
            elif upload == "Yes":  # This part should start a csv upload to the program so that questions and answers
                                    # are loaded into the def test(): function
                pass
                '''upload_csv = input("Enter the file name you would like to use, in the form 'example.csv': ")
                the_file = open(upload_csv, 'r')'''
            else:
                print('Please enter either "Yes" or "No"')

    def test(self):
        answer = 0
        while True:
            q_a_number = random.randint(0, len(self.flashcard) - 1)
            if self.flashcard[q_a_number][2] == -1:
                user_enter = str(input("What is the correct answer for {}? ".format(self.flashcard[q_a_number][0])))
                if user_enter == self.flashcard[q_a_number][1]:
                    self.flashcard[q_a_number][2] = 1
                    self.correct += 1
                    answer += 1
                else:
                    self.flashcard[q_a_number][2] = 0
                    answer += 1
            if answer == len(self.flashcard):
                break

    def print_result(self, verbose=False):
        if verbose:
            for i in range(len(self.flashcard)):
                if self.flashcard[i][2] == 1:
                    print("Question ({}): Correct".format(self.flashcard[i][0]))
                elif self.flashcard[i][2] == 0:
                    print("Question ({}): Incorrect".format(self.flashcard[i][0]))
            print("Total number of the correct answers: {} out of {}".format(self.correct, len(self.flashcard)))

    def csv_creator(self):  # This part should take questions and answers from the user input and put them into a csv
                            # file
        creation = input("Would you like a CSV file of your questions and answers? Yes or No?: ")
        if creation == "No":
            print("Thank you for playing.")
        elif creation == "Yes":
            flashcards = {}
            flashcards[question] = answer


J = Flashcard()
J.user_input()
J.test()
J.print_result()
J.print_result(verbose=True)
