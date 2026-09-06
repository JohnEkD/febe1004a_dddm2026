OK_FORMAT = True

test = {
    "name": "q2_1",
    "points": [
        1,
        4,
        3
    ],
    "suites": [
        {
            "type": "doctest",
            "cases": [
                {
                    "code": ">>> import numpy as np\n>>> type(rmse(1, 2)) == np.float64 or type(rmse(1, 2)) == float\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.isclose(rmse(0, np.mean(fifa.column('value_eur'))), np.std(fifa.column('value_eur')))\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> rmse(slope(fifa.column('age'), fifa.column('value_eur')), intercept(fifa.column('age'), fifa.column('value_eur'))) < rmse(0, np.mean(fifa.column('value_eur')))\nTrue",
                    "hidden": False,
                    "locked": False
                }
            ]
        }
    ]
}
