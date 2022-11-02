test = {
  'name': 'Problem 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Remember that the mean should return a decimal value
          >>> # If any line causes an error, write AssertionError
          >>> mean([0])
          42beece70d3b51719b1ca47780e3f5b5
          # locked
          >>> mean([1, 2, 3, 4, 5])
          0569d1cff8db32983ed84da6c2fa39b9
          # locked
          >>> mean([3, 1, -2, 7])
          bd2c331291adcb64b2a4d4c97faa1ef2
          # locked
          >>> mean([1] * 100000)
          b31e5467d1490928605bc0575f592e0e
          # locked
          >>> mean([2, 4, 6, 8] * 1000000)
          05ffc04ece796bc36354d7ef3f5ecb4b
          # locked
          >>> mean([])
          7c6bc93c499510232a264297f2f44da3
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from utils import mean
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
