test = {
  'name': 'Problem 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> soda_reviews = [make_review('Soda', 4.5),
          ...                 make_review('Soda', 4)]
          >>> soda = make_restaurant('Soda', [127.0, 0.1],
          ...                        ['Restaurants', 'Breakfast & Brunch'],
          ...                        1, soda_reviews)
          >>> restaurant_name(soda)
          72915c31b7b5a29ae54d3c5fd964368f
          # locked
          >>> restaurant_location(soda)
          45013648009573e47bea9c4f0f933977
          # locked
          >>> restaurant_categories(soda)
          b7a0d141faa2b17caf8ff9b1a32b45cf
          # locked
          >>> restaurant_price(soda)
          0371813f881bf637f2dca7a167d20c45
          # locked
          >>> restaurant_ratings(soda)
          a131ee26d99ec1bd2a9cfdf6ef591a32
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from abstractions import *
      >>> import abstractions
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(abstractions, rest=False)
          >>> make_review = abstractions.make_review
          >>> soda_reviews = [make_review('Soda', 4.5),
          ...                 make_review('Soda', 4)]
          >>> soda = make_restaurant('Soda', [127.0, 0.1],
          ...                        ['Restaurants', 'Breakfast & Brunch'],
          ...                        1, soda_reviews)
          >>> restaurant_name(soda)
          'Soda'
          >>> restaurant_location(soda)
          [127.0, 0.1]
          >>> restaurant_categories(soda)
          ['Restaurants', 'Breakfast & Brunch']
          >>> restaurant_price(soda)
          1
          >>> restaurant_ratings(soda)
          [4.5, 4]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from abstractions import *
      >>> import abstractions
      >>> import tests.test_functions as test
      """,
      'teardown': r"""
      >>> test.restore_implementations(abstractions)
      """,
      'type': 'doctest'
    }
  ]
}
