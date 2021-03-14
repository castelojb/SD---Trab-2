Start-Process -FilePath python  -ArgumentList (
  'equipament_server.py','actuator','"AR-CONDICIONADO"',8011
)
Start-Process -FilePath python  -ArgumentList (
  'equipament_server.py','sensor','"TERMOMETRO MIL GRAU"',8010
)
Start-Process -FilePath python  -ArgumentList (
  'equipament_server.py','actuator','"Luz"',8012
)
Start-Process -FilePath python  -ArgumentList (
  'equipament_server.py','sensor','"Sensor de Luminosidade"',8013
)
Start-Process -FilePath python  -ArgumentList (
  'equipament_server.py','actuator','"Alarme De Incêndio"',8014
)
Start-Process -FilePath python  -ArgumentList (
  'equipament_server.py','sensor','"Sensor de Fumaça"',8015
)