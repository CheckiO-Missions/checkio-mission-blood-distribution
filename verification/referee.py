"""
CheckiOReferee is a base referee for checking you code.
    arguments:
        tests -- the dict contains tests in the specific structure.
            You can find an example in tests.py.
        cover_code -- is a wrapper for the user function and additional operations before give data
            in the user function. You can use some predefined codes from checkio.referee.cover_codes
        checker -- is replacement for the default checking of an user function result. If given, then
            instead simple "==" will be using the checker function which return tuple with result
            (false or true) and some additional info (some message).
            You can use some predefined codes from checkio.referee.checkers
        add_allowed_modules -- additional module which will be allowed for your task.
        add_close_builtins -- some closed builtin words, as example, if you want, you can close "eval"
        remove_allowed_modules -- close standard library modules, as example "math"

checkio.referee.checkers
    checkers.float_comparison -- Checking function fabric for check result with float numbers.
        Syntax: checkers.float_comparison(digits) -- where "digits" is a quantity of significant
            digits after coma.

checkio.referee.cover_codes
    cover_codes.unwrap_args -- Your "input" from test can be given as a list. if you want unwrap this
        before user function calling, then using this function. For example: if your test's input
        is [2, 2] and you use this cover_code, then user function will be called as checkio(2, 2)
    cover_codes.unwrap_kwargs -- the same as unwrap_kwargs, but unwrap dict.

"""

from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee

from tests import TESTS


def verify(enemy, player):
    if player == []:
        if enemy[1]:
            return False, "There are dice that can beat this one."
        else:
            return True, ""
    try:
        if sum(map(lambda x: x % 1, player)) > 0:
            return False, "Each side of your die must have an integer value."

        if len(player) != len(enemy[0]):
            return False, "You die must have the same number of sides as the opponent's."

        if sum(player) != sum(enemy[0]):
            return False, "Your die must have the same total as the opponent's."

        if min(player) <= 0:
            return False, "Each side of your die must have a positive (greater than 0) number on it."
    except (TypeError, ValueError):
        return False, "Your die must be a single list of integers."

    total = 0
    for p in player:
        for e in enemy[0]:
            if p < e:
                total -= 1
            elif p > e:
                total += 1

    if total > 0:
        if enemy[1]:
            return True, ""
        else:
            return False, "The test data says this shouldn't be possible. Please let us know so we can correct our tests."
    elif total == 0:
        return False, "This is only a tie. You need to find a die that can win."
    else:
        return False, "This is a loss. You need to find a die that can win."


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        checker=verify
    ).on_ready)
