import requests
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
response.raise_for_status()
payload=response.json()
pprint(payload)

res = requests.get(
    'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
    headers={'X-Auth-Token': payload['Token']}).json()
data = res['response']

dash = '-' * 140
print(dash)
print("{:^20s} {:^20} {:<35} {:>30} {:>25}".format(
    'Tipo de Equipos',
    'Hostname',
    'Direccion IP de administracion',
    'Fecha de ultima actualizacion',
    'Estatus del equipo'))
print(dash)

for i in data:
    print('{:^20s} {:^20s} {:^30s} {:^40s} {:^25s}'.format(
        i['family'],
        i['hostname'],
        i['managementIpAddress'],
        i['lastUpdated'],
        i['reachabilityStatus']
    ))