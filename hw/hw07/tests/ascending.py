test = {
  'name': 'ascending?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ascending? '(1 2 3 4 5))  ; #t or #f
          dd1c8dcce7b8598825d7b6b7d237639d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(1 5 2 4 3))  ; #t or #f
          9e1a295fed6e9113292585fe7acb7556
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(2 2))  ; #t or #f
          dd1c8dcce7b8598825d7b6b7d237639d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(1 2 2 4 3))  ; #t or #f
          9e1a295fed6e9113292585fe7acb7556
          # locked
          """,
          'hidden': False,
          'locked': True,
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
