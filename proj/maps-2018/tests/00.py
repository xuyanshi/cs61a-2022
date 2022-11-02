test = {
  'name': 'Problem 0',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> square = lambda x: x * x
          >>> is_odd = lambda x: x % 2 == 1
          >>> map_and_filter([1, 2, 3, 4, 5], square, is_odd)
          dab62dc32550156f38bcbd91d9a48b1a
          # locked
          >>> map_and_filter(['hi', 'hello', 'hey', 'world'],
          ...                lambda x: x[4], lambda x: len(x) > 4)
          08d56251df05a668e2cc1a38b0cff68b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> min([-2, -1, 0, 1, 2], key=lambda x: x*x)
          053aedcca9c69b8fb1dca420ff3c179b
          # locked
          >>> min([[0, 3], [1, 2], [2, 1]], key=lambda x: x[1])
          5ac34b462e921b53662ffe06fb46b255
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> key_of_min_value({1: 6, 2: 5, 3: 4})
          f86124ac9392b60456505ccefe002925
          # locked
          >>> key_of_min_value({'a': 6, 'b': 5, 'c': 4})
          78ecf8091bdb914c48fc1311604e0c87
          # locked
          >>> key_of_min_value({'hello': 'world', 'hi': 'there'})
          c8a87e36951a07938124fd8df6fbaf1e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> enumerate([6, 'one', 'a'], 3)[1]
          736a16a06f9e289bf5bcd4cd6f238b2c
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from utils import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'answer': '805cc5fdbc962de6ce1fb691ed01ab75',
          'choices': [
            'xs + ys',
            '(xs, ys)',
            'zip([xs, ys])',
            'zip(xs, ys)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Consider the lists xs = [6, 1, 4] and ys = [2, 6, 2]. Which
          of the choices below for EXPR would produce the following
          output?
          
          >>> for x, y in EXPR:
          ...     print(x + y)
          8
          7
          6
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
