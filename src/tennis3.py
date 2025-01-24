class TennisGame3:
    POINT = 1
    MATCHPOINT = 4
    ADVANTAGEPOINT = 6

    def __init__(self, leftplayer_name, rightplayer_name):
        self.leftplayer_name = leftplayer_name
        self.rightplayer_name = rightplayer_name
        self.leftplayer_points = 0
        self.rightplayer_points = 0

    def won_point(self, playername):
        if playername == self.leftplayer_name:
            self.leftplayer_points += TennisGame3.POINT
        else:
            self.rightplayer_points += TennisGame3.POINT

    def score(self):
        if (self.leftplayer_points < TennisGame3.MATCHPOINT and self.rightplayer_points < TennisGame3.MATCHPOINT) and (self.leftplayer_points + self.rightplayer_points < TennisGame3.ADVANTAGEPOINT):
            score_annotation = ["Love", "Fifteen", "Thirty", "Forty"]
            current_anotatedscore = score_annotation[self.leftplayer_points]
            return current_anotatedscore + "-All" if (self.leftplayer_points == self.rightplayer_points) else current_anotatedscore + "-" + score_annotation[self.rightplayer_points]
        else:
            if self.leftplayer_points == self.rightplayer_points:
                return "Deuce"
            winningplayer_name = self.leftplayer_name if self.leftplayer_points > self.rightplayer_points else self.rightplayer_name
            return (
                "Advantage " + winningplayer_name
                if ((self.leftplayer_points - self.rightplayer_points) * (self.leftplayer_points - self.rightplayer_points) == 1)
                else "Win for " + winningplayer_name
            )
