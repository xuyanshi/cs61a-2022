test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab08 import *
          >>> link = Link(1000)
          >>> link.first
          6812c36ce75fc0b1c442b1d56b8c98f1
          # locked
          >>> link.rest is Link.empty
          0528ddea472f19174e0c4eb75b4de3de
          # locked
          >>> link = Link(1000, 2000)
          8a2fd4e4c3c6dcce2dc631af62ee217a
          # locked
          >>> link = Link(1000, Link())
          8a2fd4e4c3c6dcce2dc631af62ee217a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from lab08 import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          802285b020b27240a3824a7e42f8cc8c
          # locked
          >>> link.rest.first
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> link.rest.rest.rest is Link.empty
          0528ddea472f19174e0c4eb75b4de3de
          # locked
          >>> link.first = 9001
          >>> link.first
          2f870cb7220a96bf2531180ebc182058
          # locked
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest is Link.empty
          9b87ee740b72a262114634ab6b9e401e
          # locked
          >>> link.rest.rest.rest.rest.first
          802285b020b27240a3824a7e42f8cc8c
          # locked
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          802285b020b27240a3824a7e42f8cc8c
          # locked
          >>> link2.rest.first
          9338923f09aac77121029c604f7ce4f3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from lab08 import *
          >>> link = Link(5, Link(6, Link(7)))
          >>> link                  # Look at the __repr__ method of Link
          c4be84510df152813dfac1955471823d
          # locked
          >>> print(link)          # Look at the __str__ method of Link
          9e4aa8611562bf27deef2ea24cf05283
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
