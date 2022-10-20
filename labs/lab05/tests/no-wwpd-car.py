test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.model
          a75b891a2cacc4ea2f479ce55445bcdf
          # locked
          >>> deneros_car.gas = 10
          >>> deneros_car.drive()
          a1631be3dd57e616078c95dd5070ed5f
          # locked
          >>> deneros_car.drive()
          618f8fcace852e85e8b1a381eb8b57f3
          # locked
          >>> deneros_car.fill_gas()
          d4af78edc8e00de0aed3930ffe3c6c47
          # locked
          >>> deneros_car.gas
          64cd9271679b23a0524338694072ea06
          # locked
          >>> Car.gas
          a3a638f06097c60c08da188a9a8ad3a3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.wheels = 2
          >>> deneros_car.wheels
          31f02e75f8bef5a0621b68131795447b
          # locked
          >>> Car.num_wheels
          fef77a143fa87e746554afe9ebb16a3d
          # locked
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          618f8fcace852e85e8b1a381eb8b57f3
          # locked
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          66901ed5775b51743d745870a1a883e3
          # locked
          >>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          618f8fcace852e85e8b1a381eb8b57f3
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
