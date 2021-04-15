from question_model import Question
from data import get_question
from quiz_brain import QuizBrain
from quizzler_user_interface import QuizzlerInterface

# instead of importing question_data from data, we could  import get_question instead
# and save the return value  in a question_data variable
# question_data=get_question()

question_bank = []
for question in get_question():
    # get the question text
    question_text = question["question"]
    # ge the question answer
    question_answer = question["correct_answer"]
    # create an Question object  of the current question and answer
    new_question = Question(question_text, question_answer)
    # and then created question objects to the question_bank
    question_bank.append(new_question)

# create new quiz out of the question_bank
quiz = QuizBrain(question_bank)
# show quiz on the UI
quizzler_ui = QuizzlerInterface(quiz=quiz)
# update question on the UI
while quiz.still_has_questions():
    quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
