"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
       {
            "input": ( {"A": 10, "B": 0, "AB": 25, "O": 5},{"A": 0, "B": 0, "AB": 30, "O": 10}),
            "answer": ( {"A": 10, "B": 0, "AB": 25, "O": 5},{"A": 0, "B": 0, "AB": 30, "O": 10}, 35 )
        },
        {
            "input": ( {"A": 120, "B": 40, "AB": 20, "O": 90},{"A": 150, "B": 40, "AB": 20, "O": 60}),
            "answer": ( {"A": 120, "B": 40, "AB": 20, "O": 90},{"A": 150, "B": 40, "AB": 20, "O": 60}, 270 )
        },
        {
            "input": ( {"A": 120, "B": 40, "AB": 20, "O": 90},{"A": 150, "B": 40, "AB": 20, "O": 60}),
            "answer": ( {"A": 120, "B": 40, "AB": 20, "O": 90},{"A": 150, "B": 40, "AB": 20, "O": 60}, 270 )
        },
        

    ],
     "Extra": [
        {
            "input": ( {"A": 10, "B": 0, "AB": 25, "O": 5},{"A": 0, "B": 0, "AB": 30, "O": 10}),
            "answer": ( {"A": 10, "B": 0, "AB": 25, "O": 5},{"A": 0, "B": 0, "AB": 30, "O": 10}, 35 )
        },
        {
            "input": ( {"A": 120, "B": 40, "AB": 20, "O": 90},{"A": 150, "B": 40, "AB": 20, "O": 60}),
            "answer": ( {"A": 120, "B": 40, "AB": 20, "O": 90},{"A": 150, "B": 40, "AB": 20, "O": 60}, 270 )
        },
        

    ]
    
    
}

