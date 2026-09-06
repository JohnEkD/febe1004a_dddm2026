OK_FORMAT = True

test = {
    "name": "q2_2",
    "points": [
        2,
        1,
        1
    ],
    "suites": [
        {
            "type": "doctest",
            "cases": [
                {
                    "code": ">>> np.isclose(lsq_slope, slope(fifa.column('age'), fifa.column('value_eur')), rtol=1e-3)\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.isclose(lsq_intercept, np.mean(fifa.column('value_eur')) - lsq_slope * np.mean(fifa.column('age')), rtol=1e-2)\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> rmse(lsq_slope, lsq_intercept) <= rmse(lsq_slope * 1.02, lsq_intercept) + 1e-6\nTrue",
                    "hidden": False,
                    "locked": False
                }
            ]
        }
    ]
}
