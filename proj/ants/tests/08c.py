test = {
  'name': 'Problem 8c',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'ContainerAnt class',
          'choices': [
            'ContainerAnt class',
            'Insect class',
            'the BodyguardAnt does not inherit from any other class',
            'Ant class'
          ],
          'hidden': False,
          'locked': False,
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
          4
          >>> bodyguard.health
          2
          """,
          'hidden': False,
          'locked': False,
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
