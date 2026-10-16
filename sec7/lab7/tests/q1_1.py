OK_FORMAT = True

test = {'name': 'q1_1',
 'points': 3,
 'suites': [{'type': 'doctest',
             'cases': [{'code': '>>> bounce_locations.num_rows == 3\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'bounce_locations should have one row for each value in '
                                           'bounce_location_long. There are three.'},
                       {'code': ">>> sorted(bounce_locations.column(0)) == ['no_mans_land', 'out', "
                                "'service_box']\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The first column should hold the values found in '
                                           'bounce_location_long.'},
                       {'code': ">>> sum(bounce_locations.column('count')) == 55448\nTrue",
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The counts should add up to the number of rows in shots. Check '
                                           'you grouped the whole shots table.'}],
             'scored': True,
             'setup': '',
             'teardown': ''}]}
