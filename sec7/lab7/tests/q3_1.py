OK_FORMAT = True

test = {'name': 'q3_1',
 'points': 6,
 'suites': [{'type': 'doctest',
             'cases': [{'code': ">>> _train = Table().with_columns('hit_velocity_y', make_array(0.0, 10.0, "
                                "10.5), 'hit_velocity_z', make_array(0.0, 10.0, 10.5), "
                                "'bounce_location_long', make_array('service_box', 'no_mans_land', "
                                "'no_mans_land'))\n"
                                ">>> _test = Table().with_columns('hit_velocity_y', make_array(0.4, 10.2), "
                                "'hit_velocity_z', make_array(0.4, 10.2), 'bounce_location_long', "
                                "make_array('no_mans_land', 'service_box'))\n"
                                '>>> closest_label(_test.row(0), _train) is not None\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Your function did not give anything back. The last line needs to '
                                           'start with return.'},
                       {'code': ">>> _train = Table().with_columns('hit_velocity_y', make_array(0.0, 10.0, "
                                "10.5), 'hit_velocity_z', make_array(0.0, 10.0, 10.5), "
                                "'bounce_location_long', make_array('service_box', 'no_mans_land', "
                                "'no_mans_land'))\n"
                                ">>> _test = Table().with_columns('hit_velocity_y', make_array(0.4, 10.2), "
                                "'hit_velocity_z', make_array(0.4, 10.2), 'bounce_location_long', "
                                "make_array('no_mans_land', 'service_box'))\n"
                                '>>> closest_label(_test.row(0), _train)\n'
                                "'service_box'",
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The nearest training shot to (0.4, 0.4) is (0.0, 0.0), which is '
                                           'a service_box shot.'},
                       {'code': ">>> _train = Table().with_columns('hit_velocity_y', make_array(0.0, 10.0, "
                                "10.5), 'hit_velocity_z', make_array(0.0, 10.0, 10.5), "
                                "'bounce_location_long', make_array('service_box', 'no_mans_land', "
                                "'no_mans_land'))\n"
                                ">>> _test = Table().with_columns('hit_velocity_y', make_array(0.4, 10.2), "
                                "'hit_velocity_z', make_array(0.4, 10.2), 'bounce_location_long', "
                                "make_array('no_mans_land', 'service_box'))\n"
                                '>>> closest_label(_test.row(1), _train)\n'
                                "'no_mans_land'",
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The nearest training shot to (10.2, 10.2) is (10.0, 10.0), which '
                                           'is a no_mans_land shot. Check you sorted by distance in the '
                                           'default (smallest first) order.'}],
             'scored': True,
             'setup': '',
             'teardown': ''}]}
