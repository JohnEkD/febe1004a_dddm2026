OK_FORMAT = True

test = {
    "name": "q4_1",
    "points": [
        3,
        3,
        8
    ],
    "suites": [
        {
            "type": "doctest",
            "cases": [
                {
                    "code": ">>> type(slope_and_intercept(Table().with_columns('x', make_array(0, 1), 'y', make_array(1, 3)), 'x', 'y')) == np.ndarray\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> len(slope_and_intercept(Table().with_columns('x', make_array(0, 1), 'y', make_array(1, 3)), 'x', 'y')) == 2\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.allclose(np.round(slope_and_intercept(Table().with_columns('x', make_array(0, 1), 'y', make_array(1, 3)), 'x', 'y'), 5), np.array([2, 1]))\nTrue",
                    "hidden": False,
                    "locked": False
                }
            ]
        }
    ]
}
