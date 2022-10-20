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
          c4baa133341c5988be93c04ac3d055bb
          # locked
          >>> r1 = virfib_sq(1)
          91b35c416e4c4ef4138ebfcce69874af
          # locked
          >>> r2 = virfib_sq(2)
          61b793952531daad90d65377b695da99
          91b35c416e4c4ef4138ebfcce69874af
          c4baa133341c5988be93c04ac3d055bb
          # locked
          >>> r3 = virfib_sq(3)
          62cb7be5b3f27b8761401e9f99897a30
          61b793952531daad90d65377b695da99
          91b35c416e4c4ef4138ebfcce69874af
          c4baa133341c5988be93c04ac3d055bb
          91b35c416e4c4ef4138ebfcce69874af
          # locked
          >>> r3
          e6efc1fcfbebed28c5068a807b6cce64
          # locked
          >>> (r1 + r2) ** 2
          e6efc1fcfbebed28c5068a807b6cce64
          # locked
          >>> r4 = virfib_sq(4)
          e6efc1fcfbebed28c5068a807b6cce64
          62cb7be5b3f27b8761401e9f99897a30
          61b793952531daad90d65377b695da99
          91b35c416e4c4ef4138ebfcce69874af
          c4baa133341c5988be93c04ac3d055bb
          91b35c416e4c4ef4138ebfcce69874af
          61b793952531daad90d65377b695da99
          91b35c416e4c4ef4138ebfcce69874af
          c4baa133341c5988be93c04ac3d055bb
          # locked
          >>> r4
          6958307009d94c1d298ae9f450f606ff
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
