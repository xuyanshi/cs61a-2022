test = {
  'name': 'Problem 8c',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '9f40b97857ecfadf1e7ad1c7965f2464',
          'choices': [
            'ContainerAnt class',
            'Insect class',
            'the BodyguardAnt does not inherit from any other class',
            'Ant class'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Where does a BodyguardAnt directly inherit all of its instance attributes from?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing BodyguardAnt parameters
          >>> bodyguard = BodyguardAnt()
          >>> BodyguardAnt.food_cost
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          >>> bodyguard.health
          20d533d3e06345c8bd7072212867f2d1
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
