test = {
  'name': 'list-comp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (list-of-macro (* x x) for x in '(3 4 5) if (odd? x))
          (9 25)
          scm> (list-of-macro (* x x) for x in '(3 4 5) if (lambda (x) x))
          (9 16 25)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (list-of-macro (* 2 x) for x in (list-of-macro (* y y) for y in '(1 2 3 4 5) if (lambda (x) x)) if (odd? x))
          (2 18 50)
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
