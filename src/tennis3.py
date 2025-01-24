class TennisGame3:
    def __init__(self, leftplayer_name, rightplayer_name):
        self.leftplayer_name = leftplayer_name
        self.rightplayer_name = rightplayer_name
        self.leftplayer_points = 0
        self.rightplayer_points = 0

    def won_point(self, playername):
        if playername == self.leftplayer_name:
            self.leftplayer_points += 1
        else:
            self.rightplayer_points += 1

    def score(self):
        if (self.leftplayer_points < 4 and self.rightplayer_points < 4) and (self.leftplayer_points + self.rightplayer_points < 6):
            score_annotation = ["Love", "Fifteen", "Thirty", "Forty"]
            current_anotatedscore = score_annotation[self.leftplayer_points]
            return current_anotatedscore + "-All" if (self.leftplayer_points == self.rightplayer_points) else current_anotatedscore + "-" + score_annotation[self.rightplayer_points]
        else:
            if self.leftplayer_points == self.rightplayer_points:
                return "Deuce"
            current_anotatedscore = self.leftplayer_name if self.leftplayer_points > self.rightplayer_points else self.rightplayer_name
            return (
                "Advantage " + current_anotatedscore
                if ((self.leftplayer_points - self.rightplayer_points) * (self.leftplayer_points - self.rightplayer_points) == 1)
                else "Win for " + current_anotatedscore
            )
