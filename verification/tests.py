"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "0. Basics": [
        {
            "input":  ({'A': 120, 'B': 80, 'AB': 50, 'O': 100},
{'A': 30, 'B': 40, 'AB': 20, 'O': 60}) ,
            "answer": ({'A': 120, 'B': 80, 'AB': 50, 'O': 100},
 {'A': 30, 'B': 40, 'AB': 20, 'O': 60})
        },
        {
            "input":  [{'A': 120, 'B': 80, 'AB': 50, 'O': 100},
{'A': 30, 'B': 40, 'AB': 20, 'O': 60}] ,
            "answer": ({'A': 120, 'B': 80, 'AB': 50, 'O': 100},
 {'A': 30, 'B': 40, 'AB': 20, 'O': 60}),
        },
        {
            "input":  [{'A': 120, 'B': 80, 'AB': 50, 'O': 100},
{'A': 30, 'B': 40, 'AB': 20, 'O': 60}] ,
            "answer": ({'A': 120, 'B': 80, 'AB': 50, 'O': 100},
 {'A': 30, 'B': 40, 'AB': 20, 'O': 60})
        },
        {
            "input":  [{'A': 120, 'B': 80, 'AB': 50, 'O': 100},
{'A': 30, 'B': 40, 'AB': 20, 'O': 60}] ,
            "answer": ({'A': 120, 'B': 80, 'AB': 50, 'O': 100},
 {'A': 30, 'B': 40, 'AB': 20, 'O': 60})
        },
        {
            "input":  [{'A': 120, 'B': 80, 'AB': 50, 'O': 100},
{'A': 30, 'B': 40, 'AB': 20, 'O': 60}] ,
            "answer": ({'A': 120, 'B': 80, 'AB': 50, 'O': 100},
 {'A': 30, 'B': 40, 'AB': 20, 'O': 60}) 
        }
    ],
    "1. Small": [
        {
            "input":  [{'A': 120, 'B': 80, 'AB': 50, 'O': 100},
{'A': 30, 'B': 40, 'AB': 20, 'O': 60}] ,
            "answer": ({'A': 120, 'B': 80, 'AB': 50, 'O': 100},
 {'A': 30, 'B': 40, 'AB': 20, 'O': 60}) 
        },
        {
            "input":  [{'A': 120, 'B': 80, 'AB': 50, 'O': 100},
{'A': 30, 'B': 40, 'AB': 20, 'O': 60}] ,
            "answer": ({'A': 120, 'B': 80, 'AB': 50, 'O': 100},
 {'A': 30, 'B': 40, 'AB': 20, 'O': 60} )
        }

    ],
    "2. Big": [
        {
            "input":  [{'A': 120, 'B': 80, 'AB': 50, 'O': 100},
{'A': 30, 'B': 40, 'AB': 20, 'O': 60}] ,
            "answer": ({'A': 120, 'B': 80, 'AB': 50, 'O': 100},
 {'A': 30, 'B': 40, 'AB': 20, 'O': 60} )
        },
        {
            "input":  [{'A': 120, 'B': 80, 'AB': 50, 'O': 100},
{'A': 30, 'B': 40, 'AB': 20, 'O': 60}] ,
            "answer": ({'A': 120, 'B': 80, 'AB': 50, 'O': 100},
 {'A': 30, 'B': 40, 'AB': 20, 'O': 60} )
        }

    ]
}

