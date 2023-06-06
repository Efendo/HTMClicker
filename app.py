class Application:
    def __init__(self): # Initialize the Score Display object and the Score
        self.ScoreDisp = Element("ScoreDisp")
        self.score = 0

    def click(self): # The click behavior
        self.ScoreDisp.remove_class("transition-all")
        self.ScoreDisp.remove_class("duration-150")
        self.ScoreDisp.remove_class("rotate-[360deg]")
        self.score += 1
        self.ScoreDisp.innerHTML = self.score
        if self.score % 100 == 0:
            self.ScoreDisp.add_class("rotate-[360deg]")
            self.ScoreDisp.add_class("transition-all")
            self.ScoreDisp.add_class("duration-150")


app = Application() # Initialize the application
