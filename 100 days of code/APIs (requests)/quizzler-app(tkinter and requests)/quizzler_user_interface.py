from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
Canvas_WIDTH = 300
Canvas_HEIGHT = 250
QUESTION_FONT = ("Arial", 18, "italic")
SCORE_FONT = ("Arial", 15, "italic")
SCORE_COLOR = "white"
Canvas_BG_COLOR = "white"
TRUE_IMG_PATH = "images/true.png"
FALSE_IMG_PATH = "images/false.png"


class QuizzlerInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Creating canvas to present the question texts
        self.canvas = Canvas(width=Canvas_WIDTH, height=Canvas_HEIGHT, bg=Canvas_BG_COLOR)
        self.question_text = self.canvas.create_text(Canvas_WIDTH / 2, Canvas_HEIGHT / 2, width=280,
                                                     text="Default Text",
                                                     fill=THEME_COLOR, font=QUESTION_FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # create label to view the score
        self.label = Label(text=f"Score: 0", bg=THEME_COLOR, fg=SCORE_COLOR, font=SCORE_FONT)
        self.label.grid(column=1, row=0)
        # Adding buttons
        true_image = PhotoImage(file=TRUE_IMG_PATH)
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        false_image = PhotoImage(file=FALSE_IMG_PATH)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        self.show_question()
        self.window.mainloop()

    def show_question(self):
        """Shows the Quiz questions and the user's scores in the UI """
        # to activate the buttons again for the next question
        self.false_button.config(state="active")
        self.true_button.config(state="active")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have completed the quiz.\nYour final score is: "
                                                            f"{self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        # the following lines (the first line in true_pressed() and false_pressed() ) are  to prevent multiple click
        # (and with that prevent recoding multiple true answers by multiple clicks for the same question)
        # after the user chooses an answer and clicks a button, the buttons are disabled until the answer is evaluated
        # and the user is shown the feedback.

    def true_pressed(self ):
        self.true_button.config(state="disabled")
        self.check_answer("true")

    def false_pressed(self):
        self.false_button.config(state="disabled")
        self.check_answer("false")

    def check_answer(self, answer):
        """Checks the user's answer to the current question."""
        self.show_feedback(self.quiz.check_answer(answer))

    def show_feedback(self, answer_evaluation: bool):
        """gives the user feedback on his answers, green if the answer is correct, otherwise red."""
        if answer_evaluation:
            self.canvas.config(bg='spring green')
        else:
            self.canvas.config(bg='firebrick1')
        self.window.after(1000, self.show_question)
