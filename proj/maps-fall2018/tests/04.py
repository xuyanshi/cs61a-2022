test = {
  'name': 'Problem 4',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '2469a4d8eebd9bc17c255730129b6132',
          'choices': [
            'A list of lists of restaurants',
            'A list of restaurants',
            'A list of locations',
            'A list of lists of locations'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What best describes the return value of group_by_centroid?'
        },
        {
          'answer': '68bfc2807796d89422585a6881500e29',
          'choices': [
            '[-2, 1]',
            '[0, 3]',
            '[5, 3]'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          If centroids is [[-2, 1], [0, 3], [5, 3]], with which
          centroid will the restaurant returned by
          make_restaurant('Sliver', [4, 2], ['Pizza'], 3, [])
          be associated?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> r1 = make_restaurant('Sliver', [4, 0], ['Pizza'], 2, [])
          >>> r2 = make_restaurant('La Burrita', [-1, 5], ['Mexican'], 1, [])
          >>> r3 = make_restaurant('Thai Basil', [-1, 3], ['Thai'], 2, [])
          >>> centroids = [[3, 0], [0, 4]]
          >>> groups = group_by_centroid([r1, r2, r3], centroids)
          >>> len(groups)
          93487d35d01069da0bd3a3bfb9f1a1c0
          # locked
          >>> [restaurant_name(r) for r in groups[0]]  # Cluster containing Sliver
          cf1363fd97b3c829eef0cb4794ea5f1a
          # locked
          >>> [restaurant_name(r) for r in groups[1]]  # Second cluster
          9ceb763c2bedb8d868f181b94e5ef759
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> r1 = make_restaurant('A', [-10, 2], [], 2, [
          ...         make_review('A', 4),
          ...      ])
          >>> r2 = make_restaurant('B', [-9, 1], [], 3, [
          ...         make_review('B', 5),
          ...         make_review('B', 3.5),
          ...      ])
          >>> c1 = [0, 0]
          >>> groups = group_by_centroid([r1, r2], [c1])
          >>> test.deep_check_same_elements(groups, [[r1, r2]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> r1 = make_restaurant('A', [-10, 2], [], 2, [
          ...         make_review('A', 4),
          ...      ])
          >>> r2 = make_restaurant('B', [-9, 1], [], 3, [
          ...         make_review('B', 5),
          ...         make_review('B', 3.5),
          ...      ])
          >>> r3 = make_restaurant('C', [4, 2], [], 1, [
          ...         make_review('C', 5)
          ...      ])
          >>> c1 = [0, 0]
          >>> c2 = [3, 4]
          >>> groups = group_by_centroid([r1, r2, r3], [c1, c2])
          >>> test.deep_check_same_elements(groups, [[r1, r2], [r3]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> r1 = make_restaurant('A', [-10, 2], [], 2, [
          ...         make_review('A', 4),
          ...      ])
          >>> r2 = make_restaurant('B', [-9, 1], [], 3, [
          ...         make_review('B', 5),
          ...         make_review('B', 3.5),
          ...      ])
          >>> r3 = make_restaurant('C', [4, 2], [], 1, [
          ...         make_review('C', 5)
          ...      ])
          >>> r4 = make_restaurant('D', [-2, 6], [], 4, [
          ...         make_review('D', 2)
          ...      ])
          >>> r5 = make_restaurant('E', [4, 2], [], 3.5, [
          ...         make_review('E', 2.5),
          ...         make_review('E', 3),
          ...      ])
          >>> c1 = [0, 0]
          >>> c2 = [3, 4]
          >>> groups = group_by_centroid([r1, r2, r3, r4, r5], [c1, c2])
          >>> test.deep_check_same_elements(groups, [[r1, r2], [r3, r4, r5]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> r = make_restaurant('Zero', [0, 0], [], 1, [
          ...         make_review('Zero', 5)
          ...     ])
          >>> groups = group_by_centroid(
          ...     [r], [[x, y] for x in [1, -1] for y in [1, -1]]
          ... )
          >>> test.deep_check_same_elements(groups, [[r]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> r1 = make_restaurant('A', [1, 0], [], 1, [
          ...          make_review('A', 5)
          ...      ])
          >>> r2 = make_restaurant('B', [2, 0], [], 1, [
          ...          make_review('B', 5)
          ...      ])
          >>> r3 = make_restaurant('C', [3, 0], [], 1, [
          ...          make_review('C', 5)
          ...      ])
          >>> c1, c2, c3 = [[i, 1] for i in range(1, 4)]
          >>> groups = group_by_centroid([r1, r2, r3], [c1, c2, c3])
          >>> test.deep_check_same_elements(groups, [[r1], [r2], [r3]])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> from recommend import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> r1 = make_restaurant('A', [-10, 2], [], 2, [
          ...         make_review('A', 4),
          ...      ])
          >>> r2 = make_restaurant('B', [-9, 1], [], 3, [
          ...         make_review('B', 5),
          ...         make_review('B', 3.5),
          ...      ])
          >>> c1 = [0, 0]
          >>> groups = group_by_centroid([r1, r2], [c1])
          >>> test.deep_check_same_elements(groups, [[r1, r2]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> r1 = make_restaurant('A', [-10, 2], [], 2, [
          ...         make_review('A', 4),
          ...      ])
          >>> r2 = make_restaurant('B', [-9, 1], [], 3, [
          ...         make_review('B', 5),
          ...         make_review('B', 3.5),
          ...      ])
          >>> r3 = make_restaurant('C', [4, 2], [], 1, [
          ...         make_review('C', 5)
          ...      ])
          >>> c1 = [0, 0]
          >>> c2 = [3, 4]
          >>> groups = group_by_centroid([r1, r2, r3], [c1, c2])
          >>> test.deep_check_same_elements(groups, [[r1, r2], [r3]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> r1 = make_restaurant('A', [-10, 2], [], 2, [
          ...         make_review('A', 4),
          ...      ])
          >>> r2 = make_restaurant('B', [-9, 1], [], 3, [
          ...         make_review('B', 5),
          ...         make_review('B', 3.5),
          ...      ])
          >>> r3 = make_restaurant('C', [4, 2], [], 1, [
          ...         make_review('C', 5)
          ...      ])
          >>> r4 = make_restaurant('D', [-2, 6], [], 4, [
          ...         make_review('D', 2)
          ...      ])
          >>> r5 = make_restaurant('E', [4, 2], [], 3.5, [
          ...         make_review('E', 2.5),
          ...         make_review('E', 3),
          ...      ])
          >>> c1 = [0, 0]
          >>> c2 = [3, 4]
          >>> groups = group_by_centroid([r1, r2, r3, r4, r5], [c1, c2])
          >>> test.deep_check_same_elements(groups, [[r1, r2], [r3, r4, r5]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> r = make_restaurant('Zero', [0, 0], [], 1, [
          ...         make_review('Zero', 5),
          ...     ])
          >>> groups = group_by_centroid(
          ...     [r], [[x, y] for x in [1, -1] for y in [1, -1]]
          ... )
          >>> test.deep_check_same_elements(groups, [[r]])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> r1 = make_restaurant('A', [1, 0], [], 1, [
          ...          make_review('A', 5)
          ...      ])
          >>> r2 = make_restaurant('B', [2, 0], [], 1, [
          ...          make_review('B', 5)
          ...      ])
          >>> r3 = make_restaurant('C', [3, 0], [], 1, [
          ...          make_review('C', 5)
          ...      ])
          >>> c1, c2, c3 = [[i, 1] for i in range(1, 4)]
          >>> groups = group_by_centroid([r1, r2, r3], [c1, c2, c3])
          >>> test.deep_check_same_elements(groups, [[r1], [r2], [r3]])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> import recommend
      >>> test.swap_implementations(recommend)
      >>> make_user, make_review, make_restaurant = recommend.make_user, recommend.make_review, recommend.make_restaurant
      >>> distance = recommend.distance
      >>> find_closest, group_by_centroid = recommend.find_closest, recommend.group_by_centroid
      """,
      'teardown': r"""
      >>> test.restore_implementations(recommend)
      """,
      'type': 'doctest'
    }
  ]
}
