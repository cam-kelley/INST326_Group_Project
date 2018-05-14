# this is just a basic csv creator that I wanted to base ours off of


flashcards = {}
while True:
    question = str(input("Enter the question: "))
    if question == 'DONE':
        break
    answer = str(input("Enter the answer: "))
    flashcards[question] = answer


upload_csv = "example.csv"

flash_file = open(upload_csv, 'w')

columnTitleRow = "Question, Answer\n"
flash_file.write(columnTitleRow)

for key in flashcards.keys():
    question = key
    answer = flashcards[key]
    row = question + ',' + answer + '\n'
    flash_file.write(row)
