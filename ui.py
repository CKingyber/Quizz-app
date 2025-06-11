from tkinter import Canvas, Button, PhotoImage, Label
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
import tkinter

class Quiz_Interface:
    def __init__(self, quizbrain:QuizBrain):
        self.score_board = 0
        self.Bchoice = None
        self.quizbrain = quizbrain
        self.window = tkinter.Tk()
        self.window.title("QuizzTopia")
        self.window.minsize(800, 750)
        #--Background img----
        bg_img = PhotoImage(file="C:/Users/Samuel/Downloads/quizzler-app-start/images/New Background.png")
        bg_label = Label(image=bg_img, bg=THEME_COLOR)
        bg_label.grid(column=0, row=0, columnspan=2, rowspan=3)

        #--Centering window
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height)-100 // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        #--Resetting column weights to rectify issue caused through centering window
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        #---Canvas----
        self.canvas = Canvas(width=300, height=350, highlightthickness=1, bg=THEME_COLOR, highlightcolor="#FFFFFF")
        self.canvas.grid(column=0, row=1, columnspan=2)
        # --score---
        self.score = Canvas(width=150, height=50, highlightthickness=0, bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.score_board_txt = self.score.create_text(70, 20, text=f"score: {self.score_board}", font=("Arial", 15))
        #---Question---
        self.question_text = self.canvas.create_text(150, 200, width=290, text="Question Place Holder", font=("Arial", 16), fill="#FFFFFF")


        #---Button---
        self.t_image = PhotoImage(file="C:/Users/Samuel/Downloads/quizzler-app-start/images/true.png")
        self.t_mark = Button(image=self.t_image, highlightthickness=0, borderwidth=0, command=self.ButtonTm)
        self.t_mark.grid(column=0, row=2)

        self.x_image = PhotoImage(file="C:/Users/Samuel/Downloads/quizzler-app-start/images/false.png")
        self.x_mark = Button(image=self.x_image, highlightthickness=0, borderwidth=0, command=self.ButtonXm)
        self.x_mark.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=THEME_COLOR)
        if self.quizbrain.still_has_questions():
            q_txt = self.quizbrain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_txt)
            self.canvas.itemconfig(self.question_text, font=("Arial", 16))

        else:
            self.canvas.itemconfig(self.question_text, text=f"End of the road Bucko.\n\nQuiz Complete.")
            self.t_mark.config(state="disabled")
            self.x_mark.config(state="disabled")

    def get_check_answer(self):
        if self.quizbrain.check_answer() == self.Bchoice:
        #User Visual Feedback
            self.canvas.itemconfig(self.question_text, text="Correct")
            self.canvas.itemconfig(self.question_text, font=("Arial", 30, "bold"))
            self.canvas.config(bg="#008000")
            self.score_board += 1
            self.score.itemconfig(self.score_board_txt, text=f"score: {self.score_board}")

        else:
            self.canvas.itemconfig(self.question_text, text="Incorrect")
            self.canvas.itemconfig(self.question_text, font=("Arial", 30, "bold"))
            self.canvas.config(bg="#FF0000")

        self.window.after(1000, self.get_next_question)


    def ButtonTm(self):
        self.Bchoice = True
        self.get_check_answer()

    def ButtonXm(self):
        self.Bchoice = False
        self.get_check_answer()




