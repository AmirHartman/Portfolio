from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzller")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='test',
            font=('Arial', 14, 'italic'),
            width=280,
            justify=CENTER,
            fill='black'
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_text = Label(text=f"Score: {self.quiz.score}", background=THEME_COLOR, fg='white',
                                font=('Ariel', 18, 'bold'))
        self.score_text.grid(row=0, column=1)

        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.right_answer_button = Button(image=true_image, highlightthickness=0,
                                          command=self.true_button_click)
        self.right_answer_button.grid(row=2, column=0)
        self.wrong_answer_button = Button(image=false_image, highlightthickness=0,
                                          command=self.wrong_button_click)
        self.wrong_answer_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg='white')
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_text.config(text=f"Score: {self.quiz.score}")
        else:
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg='blue')
            self.canvas.itemconfig(self.question_text,
                                   text=f"GAME OVER!\n\nYour final score is {self.quiz.score}/{self.quiz.question_number}",
                                   fill='white')
            self.right_answer_button.config(state='disabled')
            self.wrong_answer_button.config(state='disabled')

    def true_button_click(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def wrong_button_click(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.quiz.score += 1
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


