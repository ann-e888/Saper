import csv
from tkinter import Toplevel, Label, messagebox
from scorewindow import ScoresWindow


class ScoreSave:
    def __init__(self, filename):
        self.filename = filename
        self.scores = []

    def add_score(self, name, time):
        self.scores.append((name, time))
        self.save_scores()

    def save_scores(self):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.scores)

    def load_scores(self):
        scores = []
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                scores = list(reader)
                if not scores:
                    return None
        except FileNotFoundError:
            messagebox.showinfo("Scores", "No previous results")
        return scores

    def show_scores(self):
        scores = self.load_scores()

        if scores is not None:
            scores_window = ScoresWindow(scores)
        


