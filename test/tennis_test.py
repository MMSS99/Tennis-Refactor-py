import pytest

from src.tennis1 import TennisGame1
from src.tennis3 import TennisGame3
from test.tennis_unittest import play_game, test_cases


@pytest.mark.parametrize(
    "TennisGameClass",
    [
        TennisGame1,
        TennisGame3,
    ],
)
@pytest.mark.parametrize(
    "leftplayer_points_points rightplayer_points_points score leftplayer_nameame rightplayer_nameame".split(), test_cases
)
def test_get_score_most_games(
    TennisGameClass, leftplayer_points_points, rightplayer_points_points, score, leftplayer_nameame, rightplayer_nameame
):
    game = play_game(TennisGameClass, leftplayer_points_points, rightplayer_points_points, leftplayer_nameame, rightplayer_nameame)
    assert score == game.score()

