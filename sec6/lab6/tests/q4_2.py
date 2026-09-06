OK_FORMAT = True

test = {
    "name": "q4_2",
    "points": [
        4,
        4,
        6
    ],
    "suites": [
        {
            "type": "doctest",
            "cases": [
                {
                    "code": ">>> len(resampled_slopes) == 1000\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.std(resampled_slopes) > 0\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> np.abs(np.mean(resampled_slopes) - slope(birds.column('Egg Weight'), birds.column('Bird Weight'))) < 0.05\nTrue",
                    "hidden": False,
                    "locked": False
                }
            ]
        }
    ]
}
