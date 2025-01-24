class TennisGame1:
    def __init__(self, leftplayer_name, rightplayer_name):
        self.leftplayer_name = leftplayer_name
        self.rightplayer_name = rightplayer_name
        self.leftplayer_points = 0
        self.rightplayer_points = 0

    def won_point(self, player_name):
        if player_name == self.leftplayer_name:
            self.leftplayer_points += 1
        else:
            self.rightplayer_points += 1

    def score(self):
        result = ""
        temp_score = 0

        if self.leftplayer_points == self.rightplayer_points:
            return {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.leftplayer_points, "Deuce")
        elif self.leftplayer_points >= 4 or self.rightplayer_points >= 4:
            minus_result = self.leftplayer_points - self.rightplayer_points
            if minus_result == 1:
                return "Advantage " + str(self.leftplayer_name)
            elif minus_result == -1:
                return "Advantage " + str(self.rightplayer_name)
            elif minus_result >= 2:
                return "Win for " + str(self.leftplayer_name)
            else:
                return "Win for " + str(self.rightplayer_name)
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.leftplayer_points
                else:
                    result += "-"
                    temp_score = self.rightplayer_points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result
