import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Returns True is the question list still has questions"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """returns the next question and updates the question number"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # to unescape characters of the question text we get , such as quotation marks,... etc.
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_answer):
        """Checks the answer of the current question.
        Returns true if the user's answer matches the question's answer and updates the score."""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
