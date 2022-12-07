test = {
  'name': 'when-macro',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (when (= 1 0) ((/ 1 0) 'error))
          okay
          scm> (when (= 1 1) ((print 6) (print 1) 'a))
          6
          1
          a
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
