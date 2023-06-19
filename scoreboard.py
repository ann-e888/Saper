import csv

class Scoreboard:
    def __init__(self, filename):
        self.filename = filename
        self.scores = []

    def add_score(self, name, time):
        self.scores.append((name, time))
        self.save_scores()

    def save_scores(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.scores)

    def load_scores(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                self.scores = list(reader)
        except FileNotFoundError:
            print("No previous resluts")