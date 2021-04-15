from question_model import Question
from data import get_question
from quiz_brain import QuizBrain
from quizzler_user_interface import QuizzlerInterface

# instead of importing question_data from data, we could  import get_question instead
# and save the return value  in a question_data variable
# question_data=get_question()

question_bank = []
for question in get_question():
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quizzler_ui = QuizzlerInterface(quiz=quiz)
while quiz.still_has_questions():
    quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
