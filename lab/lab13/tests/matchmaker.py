test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          dog|Bohemian Rhapsody|green|blue
          dog|Bohemian Rhapsody|green|white
          dog|Bohemian Rhapsody|green|red
          dog|Bohemian Rhapsody|green|blue
          horse|good 4 u|purple|royal blue
          dog|Leave the Door Open|blue|pink
          dog|Leave the Door Open|blue|purple
          cat|I Won't Say I'm in Love|blue|green
          dog|Clair de Lune|orange|piink
          dog|Clair de Lune|orange|blue
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
