from random import choice


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.asked_questions = []

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # current_question = self.question_list[self.question_number]
        current_question = self.choose_random_question()
        self.question_number += 1
        valid_answer = False
        while not valid_answer:
            user_answer = input(f"\n\nQ.{self.question_number}: {current_question.text} (True/False): ")
            if user_answer.lower() in ["true", "false", "yes", "no", "y", "n"]:
                valid_answer = True
                self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() in ["yes", "y"]:
            user_answer = "true"
        elif user_answer.lower() in ["no", "n"]:
            user_answer = "false"
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def choose_random_question(self):
        random_question = choice(self.question_list)
        while self.still_has_questions() and random_question in self.asked_questions:
            random_question = choice(self.question_list)
        self.asked_questions.append(random_question)
        return random_question
