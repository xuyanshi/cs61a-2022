test = {
  'name': 'Problem 8b',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '7a81f10493cb9dd2a778afa061e3edd5',
          'choices': [
            r"""
            When exactly one of the Ant instances is a container and the
            container ant does not already contain another ant
            """,
            'When exactly one of the Ant instances is a container',
            'When both Ant instances are containers',
            'There can never be two Ant instances in the same place'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When can a second Ant be added to a place that already contains an Ant?'
        },
        {
          'answer': '9ee6782d61a987d40e66726eb2354093',
          'choices': [
            'The Container Ant',
            'The Ant being contained',
            'A list containing both Ants',
            'Whichever Ant was placed there first'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If two Ants occupy the same Place, what is stored in that place's ant
          instance attribute?
          """
        },
        {
          'answer': 'c9e4559526ed96dcae3a8a67e48f2539',
          'choices': [
            'The Ant instance that is in the same place as itself',
            'The Ant instance in the place closest to its own place',
            'A random Ant instance in the gamestate',
            'All the Ant instances in the gamestate'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which Ant does a ContainerAnt guard?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Container ant added before another ant
          >>> container = ContainerAnt()
          >>> other_ant = ThrowerAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(container)  # ContainerAnt in place first
          >>> place.add_insect(other_ant)
          >>> place.ant is other_ant
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> place.ant is container
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> container.ant_contained is other_ant
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Any Container Ant can be added after another ant
          >>> container = ContainerAnt()
          >>> other_ant = ThrowerAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(other_ant)  # Other ant in place first
          >>> place.ant is other_ant
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> place.add_insect(container)
          >>> place.ant is container
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> container.ant_contained is other_ant
          c7a88a0ffd3aef026b98eef6e7557da3
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
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> gamestate = GameState(None, beehive, ant_types(), layout, (1, 9))
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
