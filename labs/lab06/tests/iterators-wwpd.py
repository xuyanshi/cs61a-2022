test = {
  'name': 'Iterators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [1, 2, 3, 4]
          >>> t = iter(s)
          >>> next(s)
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          >>> next(t)
          c659f52f950a31de33b0888e439f05a7
          # locked
          >>> next(t)
          d05bc830613dfa69ef96df4f94a8da70
          # locked
          >>> iter(s)
          13c9bf76229d2e5cca16e9b9c044d4e4
          # locked
          >>> next(iter(s))
          c659f52f950a31de33b0888e439f05a7
          # locked
          >>> next(iter(t))
          214f1f0cf62380259278c29f0dd9185d
          # locked
          >>> next(iter(s))
          c659f52f950a31de33b0888e439f05a7
          # locked
          >>> next(iter(t))
          41cc26e29cc2a9e0b6fb880e349243bb
          # locked
          >>> next(t)
          480e2afbef4ea5033f7ed1d175609b6e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> r = range(6)
          >>> r_iter = iter(r)
          >>> next(r_iter)
          5b62c9d6f358ce77683fee7b403e4cee
          # locked
          >>> [x + 1 for x in r]
          ff5a839523694926c5109e5b6a40db7d
          # locked
          >>> [x + 1 for x in r_iter]
          3599898b41ed92836fc2d788cf3c88d2
          # locked
          >>> next(r_iter)
          480e2afbef4ea5033f7ed1d175609b6e
          # locked
          >>> list(range(-2, 4))   # Converts an iterable into a list
          5fbbba1ca6846ab4c8284abcdb653606
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> map_iter = map(lambda x : x + 10, range(5))
          >>> next(map_iter)
          f6b228b9600512664524ace9bb20487f
          # locked
          >>> next(map_iter)
          e8c16581add35bc404672e54d14aa222
          # locked
          >>> list(map_iter)
          f713ba8c5c3e496289c4eb738fbf14ec
          # locked
          >>> for e in filter(lambda x : x % 2 == 0, range(1000, 1008)):
          ...     print(e)
          4c54662f8cc7843b0d0c7304d9aea453
          49997c1f2b100c379b7dc11fbeca9acc
          53d7745981558f7e8c26148d16d17451
          feadf216fc357bcef6948ecbbe485ab2
          # locked
          >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
          7ad6104e44cc3932c03229aa44e6763f
          # locked
          >>> for e in zip([10, 9, 8], range(3)):
          ...   print(tuple(map(lambda x: x + 2, e)))
          fc256b507aea54543e84f2838c2bbb62
          310160eef8ed7ef357f0a1551017325a
          5256c0c8831146d1adfffbbc4fa65772
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
