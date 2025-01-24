class TennisGame1:
    POINT = 1
    MATCHPOINT = 4

    def __init__(self, leftplayer_name, rightplayer_name):
        self.leftplayer_name = leftplayer_name
        self.rightplayer_name = rightplayer_name
        self.leftplayer_points = 0
        self.rightplayer_points = 0

    def won_point(self, player_name):
        if player_name == self.leftplayer_name:
            self.leftplayer_points += TennisGame1.POINT
        else:
            self.rightplayer_points += TennisGame1.POINT

    def score(self):
        SCORES_ANNOTATION = {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty"
                    }

        if self.leftplayer_points == self.rightplayer_points:
            return {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.leftplayer_points, "Deuce")
        elif self.leftplayer_points >= TennisGame1.MATCHPOINT or self.rightplayer_points >= TennisGame1.MATCHPOINT:
            return self.__matchpoint()
        else:
            return SCORES_ANNOTATION.get(self.leftplayer_points) + "-" + SCORES_ANNOTATION.get(self.rightplayer_points)
    
    def __matchpoint(self):
        winningpart = ''
        if self.leftplayer_points > self.rightplayer_points:
            winningpart = self.leftplayer_name
        else:
            winningpart = self.rightplayer_name

        return "" + ("Advantage " if abs(self.leftplayer_points-self.rightplayer_points) == 1 else "Win for ") + winningpart
    
