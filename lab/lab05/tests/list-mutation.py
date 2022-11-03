test = {
  'name': 'List Mutation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If nothing would be output by Python, type Nothing
          >>> # If the code would error, type Error
          >>> lst = [5, 6, 7, 8]
          >>> lst.append(6)
          a4011416c969fbf2a5267fe8187bdbe9
          # locked
          >>> lst
          6de38eb54c018161d3c8f75907754469
          # locked
          >>> lst.insert(0, 9)
          >>> lst
          871af6e28abfe8c39a4d56d33d9eed15
          # locked
          >>> x = lst.pop(2)
          >>> lst
          1160320e9aa967971c9e439a9ffa0d32
          # locked
          >>> lst.remove(x)
          >>> lst
          e01057a31c9675511ae231a194bb343c
          # locked
          >>> a, b = lst, lst[:]
          >>> a is lst
          4975a2633e94dd9ea1ce929c1df08a3b
          # locked
          >>> b == lst
          4975a2633e94dd9ea1ce929c1df08a3b
          # locked
          >>> b is lst
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          >>> lst = [1, 2, 3]
          >>> lst.extend([4,5])
          >>> lst
          2408321dff6f2b70ed3d9a1548f2acb2
          # locked
          >>> lst.extend([lst.append(9), lst.append(10)])
          >>> lst
          94d885976bc1344b55cbbddb06d263dc
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
