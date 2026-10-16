OK_FORMAT = True

test = {'name': 'q2_2',
 'points': 6,
 'suites': [{'type': 'doctest',
             'cases': [{'code': ">>> _pair = Table().with_columns('hit_velocity_x', make_array(99.0, -99.0), "
                                "'hit_velocity_y', make_array(0.0, 3.0), 'hit_velocity_z', make_array(0.0, "
                                '4.0))\n'
                                ">>> _same = Table().with_columns('hit_velocity_x', make_array(1.0, 50.0), "
                                "'hit_velocity_y', make_array(2.0, 2.0), 'hit_velocity_z', make_array(7.0, "
                                '7.0))\n'
                                '>>> distance(_pair.row(0), _pair.row(1)) is not None\n'
                                'True',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Your function worked something out but did not give it back, so '
                                           'it returned None. The last line needs to start with return.'},
                       {'code': ">>> _pair = Table().with_columns('hit_velocity_x', make_array(99.0, -99.0), "
                                "'hit_velocity_y', make_array(0.0, 3.0), 'hit_velocity_z', make_array(0.0, "
                                '4.0))\n'
                                ">>> _same = Table().with_columns('hit_velocity_x', make_array(1.0, 50.0), "
                                "'hit_velocity_y', make_array(2.0, 2.0), 'hit_velocity_z', make_array(7.0, "
                                '7.0))\n'
                                '>>> round(distance(_pair.row(0), _pair.row(1)), 4)\n'
                                '5.0',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'For two shots 3 apart in y and 4 apart in z, the distance should '
                                           'be 5.0 (a 3-4-5 triangle). Check you squared each gap, added '
                                           'them, then took the square root.'},
                       {'code': ">>> _pair = Table().with_columns('hit_velocity_x', make_array(99.0, -99.0), "
                                "'hit_velocity_y', make_array(0.0, 3.0), 'hit_velocity_z', make_array(0.0, "
                                '4.0))\n'
                                ">>> _same = Table().with_columns('hit_velocity_x', make_array(1.0, 50.0), "
                                "'hit_velocity_y', make_array(2.0, 2.0), 'hit_velocity_z', make_array(7.0, "
                                '7.0))\n'
                                '>>> round(distance(_same.row(0), _same.row(1)), 4)\n'
                                '0.0',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'Two shots with the same hit_velocity_y and hit_velocity_z are at '
                                           'distance 0, even when hit_velocity_x differs. Do not use '
                                           'hit_velocity_x.'},
                       {'code': ">>> _pair = Table().with_columns('hit_velocity_x', make_array(99.0, -99.0), "
                                "'hit_velocity_y', make_array(0.0, 3.0), 'hit_velocity_z', make_array(0.0, "
                                '4.0))\n'
                                ">>> _same = Table().with_columns('hit_velocity_x', make_array(1.0, 50.0), "
                                "'hit_velocity_y', make_array(2.0, 2.0), 'hit_velocity_z', make_array(7.0, "
                                '7.0))\n'
                                '>>> round(distance(_pair.row(1), _pair.row(0)), 4)\n'
                                '5.0',
                        'hidden': False,
                        'locked': False,
                        'failure_message': 'The distance from A to B should equal the distance from B to A. '
                                           'Check you squared the gaps.'}],
             'scored': True,
             'setup': '',
             'teardown': ''}]}
