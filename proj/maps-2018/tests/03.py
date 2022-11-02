test = {
  'name': 'Problem 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': '26c0cd6d106fdf26fd85aa6de414e1ac',
          'choices': [
            'number; e.g. 1',
            "restaurant; e.g. make_restaurant('A', [1, 1], ['Food'], 1, [])",
            'pair; e.g. [1, 1]',
            "string of a pair; e.g. '[1, 1]'"
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Which of the following types of values can be passed as
          an argument to distance?
          """
        },
        {
          'answer': '11ad45795e3c3a916d2bde6489676409',
          'choices': [
            'lambda x, y: pow(-x, y)',
            'lambda x, y: abs(x - y)',
            'lambda x: abs(x[0] - x[1])',
            'sum'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Consider the list l = [[4, 1], [-3, 2], [5, 0]]. Which of
          the choices below for fn would make min(l, key=fn) evaluate
          to [4, 1]?
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
          >>> distance([0, 0], [3, 4]) # should be a decimal
          05ffc04ece796bc36354d7ef3f5ecb4b
          # locked
          >>> distance([6, 1], [6, 1]) # should be a decimal
          42beece70d3b51719b1ca47780e3f5b5
          # locked
          >>> distance([-2, 7], [-3.5, 9]) # should be a decimal
          17bb99edcf293ff077118c4bcc975596
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> find_closest([6, 1],
          ...              [[1, 5], [3, 3]])
          56c587b685afb8be4741df4d7f3bb220
          # locked
          >>> find_closest([1, 6],
          ...              [[1, 5], [3, 3]])
          71dfc270dd0cb21a153bad71eca045b9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> find_closest([0, 0],
          ...              [[-2, 0], [2, 0]])
          53c0b010aa948332eccb7355b56828fd
          # locked
          >>> find_closest([0, 0],
          ...              [[1000, 1000]])
          42bc5d4535a0f39499f807f8f1e11e9d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Be sure to use the distance function!
          >>> find_closest([0, 0],
          ...              [[2, 2], [0, 3]])
          7cc3e5c11ab42007181d16531b7d93a9
          # locked
          >>> find_closest([0, 0],
          ...              [[5, 5], [2, 7]])
          8b15a09e0d9053bc3b1a0ac4755210ff
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> find_closest([0, 0],
          ...              [[1, 0], [0, 1], [-1, 0], [0, -1]])
          [1, 0]
          >>> find_closest([0, 0],
          ...              [[0, 1], [1, 0], [0, -1], [-1, 0]])
          [0, 1]
          >>> find_closest([0, 0],
          ...              [[1, 1], [2, 2], [3, 3]])
          [1, 1]
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
    }
  ]
}
