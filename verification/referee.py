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
