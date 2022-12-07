test = {
  'name': 'quasiquote',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> '(1 x 3)
          40872d78b7b7ba900024092a0e736c3c
          # locked
          scm> (define x 2)
          ecf2b304041c91c68610920edf6214eb
          # locked
          scm> `(1 x 3)
          40872d78b7b7ba900024092a0e736c3c
          # locked
          scm> `(1 ,x 3)
          e22664e28f584ac557399a1ec17a51ec
          # locked
          scm> '(1 ,x 3)
          8fe0e290891534b51c4a0b02b9c417be
          # locked
          scm> `(,1 x 3)
          40872d78b7b7ba900024092a0e736c3c
          # locked
          scm> `,(+ 1 x 3)
          f78ad3e385d3f17fa39a463669c2c0e7
          # locked
          scm> `(1 (,x) 3)
          761f601c0e88889ce14f15ce00131bdd
          # locked
          scm> `(1 ,(+ x 2) 3)
          41d43988d2f73bb6fcbfe5af6b4d10eb
          # locked
          scm> (define y 3)
          87e09802e0243f4d9aa26908b733336c
          # locked
          scm> `(x ,(* y x) y)
          60c0498008908fac327c366c0b48d14f
          # locked
          scm> `(1 ,(cons x (list y 4)) 5)
          1fb3a3c38831dda521e143e95f4305a6
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
