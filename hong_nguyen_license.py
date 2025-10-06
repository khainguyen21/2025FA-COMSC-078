# Part 1: Driver’s License Exam
# The local driver’s license office has asked you to create an application that grades the written portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here are the correct answers:
#
# Sample Output
# 1. A   	6. B   	11. A   	16. C
# 2. C   	7. C   	12. D   	17. B
# 3. A   	8. A   	13. C   	18. B
# 4. A   	9. C   	14. A   	19. D
# 5. D   	10. B   15. D   	20. A
# Your program, named in the form lastname_firstname_license.py, must store these correct answers in a list. The program must then prompt the student to enter their answers to each of the twenty questions and store the answers in another list.
#
# After the student’s answers have been entered, the program will display a message indicating whether the student passed or failed the exam. (A student must correctly answer 15 of the 20 questions to pass the exam.) Your program will then display the total number of correctly answered questions, the total number of incorrectly answered questions, and a list showing the question numbers of the incorrectly answered questions.
#
# The following are examples of the output from two separate runs of this program:
#
# >>> %Run estrada_license.py
# Number of correct answers: 6
# Number of incorrect answers: 14
# You did not pass the test.
# Questions answered incorrectly: 3, 4, 6, 7, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20
#
# >>> %Run estrada_license.py
# Number of correct answers: 16
# Number of incorrect answers: 4
# You passed the test.
# Questions answered incorrectly: 2, 7, 11, 15
# >>>

# Store the correct answers into a list
answer_list = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
# Initialize the empty list for user's output
user_answer_list = []

# Keep asking user until the 20th question
for question_number in range(1, 21):
    user_output = input(f"Enter your answer for question #{question_number}: ")
    user_answer_list.append(user_output.upper())

correct_ans = 0
wrong_ans = 0
# Initialize the incorrect questions list to display for the user
incorrect_list = []

# Loop through each both list and check its correctness for each question
for i in range(len(answer_list)):
    if user_answer_list[i] == answer_list[i]:
        correct_ans += 1
    else:
        wrong_ans += 1
        incorrect_list.append(str(i + 1))

# Display the number of correct and incorrect answers
print(f"Number of correct answers: {correct_ans}")
print(f"Number of incorrect answers: {wrong_ans}")

if correct_ans < 15:
    print("You did not pass the test.")
else:
    print("You passed the test.")

# Display which question was incorrect
print(f"Questions answered incorrectly: {", ".join(incorrect_list)}")





