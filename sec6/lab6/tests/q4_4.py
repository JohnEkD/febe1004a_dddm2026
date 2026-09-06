OK_FORMAT = True

test = {
    "name": "q4_4",
    "points": 4,
    "suites": [
        {
            "type": "doctest",
            "cases": [
                {
                    "code": ">>> slope_conclusion in (1, 2, 3)\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> import hashlib\n>>> hashlib.sha256(('data8-lab6-q44::' + str(slope_conclusion)).encode()).hexdigest() == 'e611d5316d56994c4eda57113dd3079d82a9e70af41753481c64bab825ff864e'\nTrue",
                    "hidden": False,
                    "locked": False
                }
            ]
        }
    ]
}
