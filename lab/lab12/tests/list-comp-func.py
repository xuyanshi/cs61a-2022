test = {
  'name': 'list-comp-func',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (list-of '(* x x) 'for 'x 'in ''(3 4 5) 'if '(odd? x))
          (map (lambda (x) (* x x)) (filter (lambda (x) (odd? x)) (quote (3 4 5))))
          scm> (eval (list-of '(* x x) 'for 'x 'in ''(3 4 5) 'if '(odd? x)))
          (9 25)
          scm> (list-of ''hi 'for 'x 'in ''(1 2 3 4 5 6) 'if '(= (modulo x 3) 0))
          (map (lambda (x) (quote hi)) (filter (lambda (x) (= (modulo x 3) 0)) (quote (1 2 3 4 5 6))))
          scm> (eval (list-of ''hi 'for 'x 'in ''(1 2 3 4 5 6) 'if '(= (modulo x 3) 0)))
          (hi hi)
          scm> (eval (list-of '(car e) 'for 'e 'in ''((10) 11 (12) 13 (14 15)) 'if '(list? e)))
          (10 12 14)
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
