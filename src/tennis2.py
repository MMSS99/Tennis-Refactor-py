class TennisGame2:
    def __init__(self, leftplayer_name, rightplayer_name):
        self.leftplayer_name = leftplayer_name
        self.rightplayer_name = rightplayer_name
        self.leftplayer_points = 0
        self.rightplayer_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score()
        else:
            self.p2_score()

    def score(self):
        result = ""
        if self.leftplayer_points == self.rightplayer_points and self.leftplayer_points < 3:
            if self.leftplayer_points == 0:
                result = "Love"
            if self.leftplayer_points == 1:
                result = "Fifteen"
            if self.leftplayer_points == 2:
                result = "Thirty"
            result += "-All"
        if self.leftplayer_points == self.rightplayer_points and self.leftplayer_points > 2:
            result = "Deuce"

        p1res = ""
        p2res = ""
        if self.leftplayer_points > 0 and self.rightplayer_points == 0:
            if self.leftplayer_points == 1:
                p1res = "Fifteen"
            if self.leftplayer_points == 2:
                p1res = "Thirty"
            if self.leftplayer_points == 3:
                p1res = "Forty"

            p2res = "Love"
            result = p1res + "-" + p2res
        if self.rightplayer_points > 0 and self.leftplayer_points == 0:
            if self.rightplayer_points == 1:
                p2res = "Fifteen"
            if self.rightplayer_points == 2:
                p2res = "Thirty"
            if self.rightplayer_points == 3:
                p2res = "Forty"

            p1res = "Love"
            result = p1res + "-" + p2res

        if self.leftplayer_points > self.rightplayer_points and self.leftplayer_points < 4:
            if self.leftplayer_points == 2:
                p1res = "Thirty"
            if self.leftplayer_points == 3:
                p1res = "Forty"
            if self.rightplayer_points == 1:
                p2res = "Fifteen"
            if self.rightplayer_points == 2:
                p2res = "Thirty"
            result = p1res + "-" + p2res
        if self.rightplayer_points > self.leftplayer_points and self.rightplayer_points < 4:
            if self.rightplayer_points == 2:
                p2res = "Thirty"
            if self.rightplayer_points == 3:
                p2res = "Forty"
            if self.leftplayer_points == 1:
                p1res = "Fifteen"
            if self.leftplayer_points == 2:
                p1res = "Thirty"
            result = p1res + "-" + p2res

        if self.leftplayer_points > self.rightplayer_points and self.rightplayer_points >= 3:
            result = "Advantage player1"

        if self.rightplayer_points > self.leftplayer_points and self.leftplayer_points >= 3:
            result = "Advantage player2"

        if (
            self.leftplayer_points >= 4
            and self.rightplayer_points >= 0
            and (self.leftplayer_points - self.rightplayer_points) >= 2
        ):
            result = "Win for player1"
        if (
            self.rightplayer_points >= 4
            and self.leftplayer_points >= 0
            and (self.rightplayer_points - self.leftplayer_points) >= 2
        ):
            result = "Win for player2"
        return result

    def set_p1_score(self, number):
        for i in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for i in range(number):
            self.p2_score()

    def p1_score(self):
        self.leftplayer_points += 1

    def p2_score(self):
        self.rightplayer_points += 1
