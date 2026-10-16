OK_FORMAT = True

test = {'name': 'q1_2',
 'points': 6,
 'suites': [{'type': 'doctest',
             'cases': [{'code': '>>> ground_strokes.num_rows == 14865\nTrue',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Expected 14865 rows. Check all four filters: ground_stroke, '
                                           'near, far, and not out.'},
                       {'code': ">>> sorted(ground_strokes.labels) == ['bounce_location_long', 'bounce_y', "
                                "'hit_velocity_x', 'hit_velocity_y', 'hit_velocity_z']\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Keep exactly these five columns: hit_velocity_x, hit_velocity_y, '
                                           'hit_velocity_z, bounce_location_long, bounce_y. Any order is '
                                           'fine.'},
                       {'code': ">>> np.count_nonzero(ground_strokes.column('bounce_location_long') == "
                                "'out') == 0\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': "There are still shots labelled 'out' in your table. Check the "
                                           'fourth filter.'},
                       {'code': ">>> np.count_nonzero(ground_strokes.column('bounce_location_long') == "
                                "'service_box') == 5684\n"
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Expected 5684 service_box shots. Check the hit_court_side and '
                                           'bounce_court_side filters.'}],
             'scored': True,
             'setup': '',
             'teardown': ''}]}
