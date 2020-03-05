#
# check-seo
# copyright 2020 AngeMort
# 05/03/2020
#

import requests

def def_headers(url):
  r = requests.get(url)
  print('URL :',url)
  print('Status :',r.status_code)

  print('Server : ',r.headers['server'])
  print('Type de Contenu :',r.headers['content-type'])

  print('Temps de chargement :',r.elapsed.total_seconds())

  if 'transfer-encoding' in r.headers:
    print('Transfère : ',r.headers['transfer-encoding'])
  else:
    print('Transfère : Null')

  if 'content-encoding' in r.headers:
    print('Encodage : ',r.headers['content-encoding'])
  else:
    print('Encodage : Null')

