test = {
  'name': 'Squared Virahanka Fibonacci',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def virfib_sq(n):
          ...     print(n)
          ...     if n <= 1:
          ...         return n
          ...     return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2
          >>> r0 = virfib_sq(0)
          0
          >>> r1 = virfib_sq(1)
          1
          >>> r2 = virfib_sq(2)
          2
          1
          0
          >>> r3 = virfib_sq(3)
          3
          2
          1
          0
          1
          >>> r3
          4
          >>> (r1 + r2) ** 2
          4
          >>> r4 = virfib_sq(4)
          4
          3
          2
          1
          0
          1
          2
          1
          0
          >>> r4
          25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
