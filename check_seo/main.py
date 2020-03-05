from . import headers
from . import links
from . import search
import sys
import requests

def run():
    if sys.argv[1]:
        #specified url compare
        url=sys.argv[1]
        print("chosen url : "+url)

        headers.def_headers(url)
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
          links.def_links(url)

        #first page Search compare
        try:
            query = sys.argv[2]
            print("first page result for the query : ")
            urls = search.search_compare(query)

            for url in urls:
                print("##########################################")
                print(url)
                headers.def_headers(url)
                r = requests.get(url)
                if r.status_code == requests.codes.ok:
                    links.def_links(url)
        except Exception as e:
            pass

        print('Finish !')
    else:
        print("no arg as been given")
