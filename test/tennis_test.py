import pytest

from src.tennis1 import TennisGame1
from src.tennis3 import TennisGame3
from test.tennis_unittest import play_game, test_cases


@pytest.mark.parametrize(
    "tennisgame_class",
    [
        TennisGame1,
        TennisGame3,
    ],
)
@pytest.mark.parametrize(
    "leftplayer_points rightplayer_points score leftplayer_name rightplayer_name".split(), test_cases
)
def test_get_score(
    tennisgame_class, leftplayer_points, rightplayer_points, score, leftplayer_name, rightplayer_name
):
    game = play_game(tennisgame_class, leftplayer_points, rightplayer_points, leftplayer_name, rightplayer_name)
    assert score == game.score()

