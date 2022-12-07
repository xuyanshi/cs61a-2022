test = {
  'name': 'repeat-macro',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (replicate '(+ 1 2) 3)
          ((+ 1 2) (+ 1 2) (+ 1 2))
          scm> (replicate (+ 1 2) 1)
          (3)
          scm> (replicate 'hi 0)
          ()
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (repeat-n (print '(resistance is futile)) 3)
          (resistance is futile)
          (resistance is futile)
          (resistance is futile)
          scm> (repeat-n (print (+ 3 3)) (+ 1 1))  ; Pass a call expression in as n
          6
          6
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
