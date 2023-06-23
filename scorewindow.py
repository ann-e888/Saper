from tkinter import Toplevel, Label, messagebox

class ScoresWindow:
    def __init__(self, scores):
        self.scores = scores
        self.window = Toplevel()
        self.window.title("Scores")
        self.display_scores()

    def display_scores(self):
        for i, (name, time) in enumerate(self.scores):
            if isinstance(time, float):
                score_label = Label(self.window, text=f"{i+1}. {name} - {time:.2f} seconds")
            else:
                score_label = Label(self.window, text=f"{i+1}. {name} - {time}")
            score_label.pack()