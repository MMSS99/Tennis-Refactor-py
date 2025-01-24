import unittest

from src.tennis1 import TennisGame1
from src.tennis3 import TennisGame3

test_cases = [
    (0, 0, "Love-All", "player1", "player2"),
    (1, 1, "Fifteen-All", "player1", "player2"),
    (2, 2, "Thirty-All", "player1", "player2"),
    (3, 3, "Deuce", "player1", "player2"),
    (4, 4, "Deuce", "player1", "player2"),
    (1, 0, "Fifteen-Love", "player1", "player2"),
    (0, 1, "Love-Fifteen", "player1", "player2"),
    (2, 0, "Thirty-Love", "player1", "player2"),
    (0, 2, "Love-Thirty", "player1", "player2"),
    (3, 0, "Forty-Love", "player1", "player2"),
    (0, 3, "Love-Forty", "player1", "player2"),
    (4, 0, "Win for player1", "player1", "player2"),
    (0, 4, "Win for player2", "player1", "player2"),
    (2, 1, "Thirty-Fifteen", "player1", "player2"),
    (1, 2, "Fifteen-Thirty", "player1", "player2"),
    (3, 1, "Forty-Fifteen", "player1", "player2"),
    (1, 3, "Fifteen-Forty", "player1", "player2"),
    (4, 1, "Win for player1", "player1", "player2"),
    (1, 4, "Win for player2", "player1", "player2"),
    (3, 2, "Forty-Thirty", "player1", "player2"),
    (2, 3, "Thirty-Forty", "player1", "player2"),
    (4, 2, "Win for player1", "player1", "player2"),
    (2, 4, "Win for player2", "player1", "player2"),
    (4, 3, "Advantage player1", "player1", "player2"),
    (3, 4, "Advantage player2", "player1", "player2"),
    (5, 4, "Advantage player1", "player1", "player2"),
    (4, 5, "Advantage player2", "player1", "player2"),
    (15, 14, "Advantage player1", "player1", "player2"),
    (14, 15, "Advantage player2", "player1", "player2"),
    (6, 4, "Win for player1", "player1", "player2"),
    (4, 6, "Win for player2", "player1", "player2"),
    (16, 14, "Win for player1", "player1", "player2"),
    (14, 16, "Win for player2", "player1", "player2"),
]


def play_game(TennisGame, leftplayer_points_points, rightplayer_points_points, leftplayer_nameame, rightplayer_nameame):
    game = TennisGame(leftplayer_nameame, rightplayer_nameame)
    for i in range(max(leftplayer_points_points, rightplayer_points_points)):
        if i < leftplayer_points_points:
            game.won_point(leftplayer_nameame)
        if i < rightplayer_points_points:
            game.won_point(rightplayer_nameame)
    return game


class TestTennis(unittest.TestCase):
    def test_score_games_1_thru_6(self):
        for TennisGameClass in (
            TennisGame1,
            TennisGame3,
        ):
            for testcase in test_cases:
                (leftplayer_points_points, rightplayer_points_points, score, leftplayer_nameame, rightplayer_nameame) = testcase
                game = play_game(
                    TennisGameClass, leftplayer_points_points, rightplayer_points_points, leftplayer_nameame, rightplayer_nameame
                )
                with self.subTest(f"{TennisGameClass.__name__} - {testcase}"):
                    self.assertEqual(score, game.score())




if __name__ == "__main__":
    unittest.main()
