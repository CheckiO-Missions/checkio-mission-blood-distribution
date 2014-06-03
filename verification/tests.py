"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

import random

TESTS = {
    "0. Basics": [
        {
            "input": [3, 3, 3, 3, 6, 6],
            "answer": ([3, 3, 3, 3, 6, 6], True)
        },
        {
            "input": [4, 4, 4, 4, 4, 4],
            "answer": ([4, 4, 4, 4, 4, 4], True)
        },
        {
            "input": [2, 2, 5, 5, 5, 5],
            "answer": ([2, 2, 5, 5, 5, 5], True)
        },
        {
            "input": [1, 1, 1, 4],
            "answer": ([1, 1, 1, 4], True)
        },
        {
            "input": [1, 2, 3, 4, 5, 6],
            "answer": ([1, 2, 3, 4, 5, 6], False)
        },
        {
            "input": [2, 3, 4, 5, 6, 7],
            "answer": ([2, 3, 4, 5, 6, 7], True)
        }
    ],
    "1. Small": [
        {
            "input": [1, 1, 1],
            "answer": ([1, 1, 1], False)
        },
        {
            "input": [1, 1, 2],
            "answer": ([1, 1, 2], False)
        },
        {
            "input": [1, 1, 3],
            "answer": ([1, 1, 3], True)
        },
        {
            "input": [2, 2, 2],
            "answer": ([2, 2, 2], False)
        },
        {
            "input": [2, 3, 4],
            "answer": ([2, 3, 4], True)
        },
        {
            "input": [3, 3, 3],
            "answer": ([3, 3, 3], True)
        },
        {
            "input": [4, 4, 4],
            "answer": ([4, 4, 4], True)
        }
    ],
    "2. Big": [
        {
            "input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "answer": ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False)
        },
        {
            "input": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            "answer": ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], False)
        },
        {
            "input": [1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
            "answer": ([1, 1, 1, 2, 2, 2, 3, 3, 3, 4], True)
        },
        {
            "input": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            "answer": ([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], True)
        },
        {
            "input": [1, 5, 5, 5, 5, 6, 6, 6, 6, 10],
            "answer": ([1, 5, 5, 5, 5, 6, 6, 6, 6, 10], True)
        },
        {
            "input": [2, 4, 6, 8, 10, 12, 14, 16, 18],
            "answer": ([2, 4, 6, 8, 10, 12, 14, 16, 18], False)
        }
    ],
    "3. Random": [
    ]
}

for i in range(0, 10):
    sides = random.randint(3, 10)
    die = list(sorted([random.randint(3, 10) for x in range(0, sides)]))
    TESTS["3. Random"].append({"input": die, "answer": (die, True)})
