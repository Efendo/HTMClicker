class Cbutton:
      def __init__(self):
            self.ScoreDisp = Element("ScoreDisp")
            self.score = 0

      def click(self):
            self.ScoreDisp.remove_class("transition-all")
            self.ScoreDisp.remove_class("duration-150")
            self.ScoreDisp.remove_class("rotate-[360deg]")
            self.score += 1
            self.ScoreDisp.element.innerHTML = self.score

            if self.score % 100 == 0:
                  self.ScoreDisp.add_class("rotate-[360deg]")
                  self.ScoreDisp.add_class("transition-all")
                  self.ScoreDisp.add_class("duration-150")


C = Cbutton()