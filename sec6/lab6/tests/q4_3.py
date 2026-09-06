OK_FORMAT = True

test = {
    "name": "q4_3",
    "points": [
        1,
        3,
        2
    ],
    "suites": [
        {
            "type": "doctest",
            "cases": [
                {
                    "code": ">>> lower_end < upper_end\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.isclose(lower_end, percentile(2.5, resampled_slopes))\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.isclose(upper_end, percentile(97.5, resampled_slopes))\nTrue",
                    "hidden": False,
                    "locked": False
                }
            ]
        }
    ]
}
