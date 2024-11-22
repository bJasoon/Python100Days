from question_model import Question
from quiz_brain import Quiz_Brain
from data import question_data

question_bank = []

for question in question_data:
    question_obj = Question(question["text"], question["answer"])
    question_bank.append(question_obj)

quiz_brain = Quiz_Brain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_quesiton()

print("\n\nYou've completed the quiz!")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
