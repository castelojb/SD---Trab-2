Start-Process -FilePath python  -ArgumentList (
  'equipament_server.py','actuator','"AR-CONDICIONADO DE CAIXA"',8011
)
Start-Process -FilePath python  -ArgumentList (
  'equipament_server.py','sensor','"TERMOMETRO MIL GRAU"',8010
)
Start-Process -FilePath python  -ArgumentList (
  'equipament_server.py','sensor','"TERMOMETRO TOP"',8012
)