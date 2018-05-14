import random
import csv


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
        while True:
            upload = input('Would you like to upload a CSV file? Enter "Yes" or "No": ')
            if upload == "No":
                question = str(input("Your question: "))
                if question == 'DONE':
                    break
                answer = str(input("Your answer: "))
                self.flashcard.append([question, answer, -1])
            elif upload == "Yes":
                upload_csv = input("Enter the file name you would like to use, in the form 'example.csv': ")
                the_file = open(upload_csv, 'r')
                reader = csv.DictReader(the_file)
                for row in reader:
                    the_q = row['Question']
                    the_a = row['Answer']
                    self.flashcard.append([the_q, the_a, -1])
                the_file.close()
                break
            else:
                print('Please enter either "Yes" or "No"')
                continue

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

    def csv_creator(self):
        while True:
            creation = input("Would you like a CSV file of your questions and answers? Yes or No?: ")
            if creation == "No":
                print("Thank you for playing.")
                break
            elif creation == "Yes":
                flashcards = {}
                for item in self.flashcard:
                    ques = item[0]
                    ans = item[1]
                    flashcards[ques] = ans

                download_csv = "Flashcards.csv"
                flash_file = open(download_csv, 'w')

                columnTitleRow = "Question,Answer\n"
                flash_file.write(columnTitleRow)

                for key in flashcards.keys():
                    question = key
                    answer = flashcards[key]
                    row = question + ',' + answer + '\n'
                    flash_file.write(row)

                print('A file called "Flashcards.csv" has been created on your computer.')
                flash_file.close()
                break
            else:
                print('Please enter either "Yes" or "No"')
                continue


J = Flashcard()
J.user_input()
J.test()
J.print_result()
J.print_result(verbose=True)
J.csv_creator()
