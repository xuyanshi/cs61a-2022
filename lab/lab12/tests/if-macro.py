test = {
  'name': 'if-macro',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (if-macro (= 0 0) 2 3)
          2
          scm> (if-macro (= 1 0) (print 3) (print 5))
          5
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
