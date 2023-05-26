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
from checkio.referees.cover_codes import unwrap_args

from tests import TESTS
def verify(answ, user_result):
    blood_avail, blood_needs, tot_used = answ
    blood_types = ["A", "B", "AB", "O"]
    distribution = user_result

    for blood_type in blood_types:
        used_blood = sum(distribution[blood_type].values())
        if used_blood > blood_avail[blood_type]:
            return False, f"Overused blood type {blood_type}"

        for target_type in blood_types:
            if blood_type == "A":
                if target_type not in ["A", "AB"]:
                    if distribution[blood_type][target_type] > 0:
                        return (
                            False,
                            f"Blood type {blood_type} is not compatible with {target_type}",
                        )
            elif blood_type == "B":
                if target_type not in ["B", "AB"]:
                    if distribution[blood_type][target_type] > 0:
                        return (
                            False,
                            f"Blood type {blood_type} is not compatible with {target_type}",
                        )
            elif blood_type == "AB":
                if target_type != "AB":
                    if distribution[blood_type][target_type] > 0:
                        return (
                            False,
                            f"Blood type {blood_type} is not compatible with {target_type}",
                        )
            elif blood_type == "O":
                if distribution[blood_type][target_type] > blood_needs[target_type]:
                    return False, f"Overfulfilled blood type {target_type} need"
                
    total_transplanted_blood = 0
    for blood_type in distribution:
        for target_type in distribution[blood_type]:
            total_transplanted_blood += distribution[blood_type][target_type]
    if total_transplanted_blood < tot_used:
        return False, f"You need to use more blood"
    if total_transplanted_blood > tot_used:
        return False, f"You have used blood illegaly!"    
    
    return True, "Success"





api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        checker=verify,
        function_name="distribute_blood",
         cover_code={
            'python-27': unwrap_args,
            'python-3': unwrap_args
         
        }
          ).on_ready)
