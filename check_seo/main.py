from . import headers
from . import links
import sys
import requests

def run():
  for arg in sys.argv:
      url=arg
  
  headers.def_headers(url)
  r = requests.get(url)
  if r.status_code == requests.codes.ok:
    links.def_links(url)
  
  print('Finish !')