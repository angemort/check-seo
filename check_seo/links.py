from bs4 import BeautifulSoup 

def def_links(url):

  # importing requests 
  import requests 
    
  # get URL 
  r = requests.get(url) 
    
  data = r.text 
  soup = BeautifulSoup(data, "lxml") 
  print('Titre :',soup.title.string) #conseillé 70 caractères max
  print('Description :',soup.desc) #environ 300 caractères max
  
  metas = soup.find_all('meta')
  for meta in metas:
    if 'name' in meta.attrs:
      if 'description' in meta.attrs:
        print('Description :',meta.attrs['description']['content']) 
      if 'keywords' in meta.attrs:
        print('keywords :',meta.attrs['keywords'])
  
 # print(soup.find("meta", name='description'))
 # print [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ] 
  print('Facebook :','ok' if soup.find("meta", property='og:site_name') else 'no')
  
  #print('Twitter :','ok' if soup.find("meta",  name='twitter:site') else 'no') 
  #print ['Twitter : ok' for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'twitter:site']
  #print(meta_property(soup, 'og:site_name')) 
  
  
  print('Nombre de lien :',len(soup.find_all('a')))
  print('Nombre de H1 :',len(soup.find_all('h1')))
  print('Nombre de H2 :',len(soup.find_all('h2')))
  print('Nombre de H3 :',len(soup.find_all('h3')))

