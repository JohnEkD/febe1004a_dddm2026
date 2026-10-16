OK_FORMAT = True

test = {'name': 'q2_1',
 'points': 6,
 'suites': [{'type': 'doctest',
             'cases': [{'code': '>>> shuffled_coords.num_rows == coords.num_rows\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'shuffled_coords should be the whole coords table in a new order, '
                                           'so it should have the same number of rows.'},
                       {'code': '>>> test_coords.num_rows == 200\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'test_coords should hold exactly 200 shots.'},
                       {'code': '>>> training_coords.num_rows == coords.num_rows - 200\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'training_coords should hold every shot that is not in '
                                           'test_coords.'},
                       {'code': '>>> test_coords.row(0) == shuffled_coords.row(0)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'test_coords should be the first 200 rows of shuffled_coords, '
                                           'starting at row 0.'},
                       {'code': '>>> training_coords.row(0) == shuffled_coords.row(200)\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'training_coords should start at row 200. Remember np.arange(200, '
                                           'n) starts at 200 and stops just before n, so row 200 is '
                                           'included.'}],
             'scored': True,
             'setup': '',
             'teardown': ''}]}
