#Zad 1 Old Books
book_found = False
book_count = 0
book_name = input()
curr_book = input()
while curr_book != "No More Books":
    if curr_book == book_name:
        book_found = True
        break
    book_count += 1
    curr_book = input()
if book_found:
    print(f"You checked {book_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")

# Zad 2 Exam Preparation
failed = int(input())
failed_count = 0
sucess_count = 0
sum = 0
lastProblem = ' '
while failed_count < failed:
    problem_name = input()
    if problem_name == "Enough":
        break
    grade = int(input())
    if grade <= 4:
        failed_count += 1
    else:
        sucess_count += 1
    sum += grade
    lastProblem = problem_name
if failed_count == failed:
    print(f"You need a break, {failed_count} poor grades.")
else:
    print(f"Average score: {sum / (sucess_count + failed_count):.2f}")
    print(f"Number of problems: {sucess_count + failed_count}")
    print(f"Last problem: {lastProblem}")