test = {
  'name': 'duplicate',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (duplicate '()) 
          ()
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (duplicate '(1 2 3)) 
          (1 1 2 2 3 3)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (duplicate '(1)) 
          (1 1)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (duplicate '(0)) 
          (0 0)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
