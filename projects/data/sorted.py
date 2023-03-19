black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"

from one import imgs as imgs_1
from two import imgs as imgs_2
from tree import imgs as imgs_3
from four import imgs as imgs_4
from five import imgs as imgs_5

from one import imgs18 as imgs18_1 
from two import imgs18 as imgs18_2 
from tree import imgs18 as imgs18_3 
from four import imgs18 as imgs18_4
from five import imgs18 as imgs18_5






import json

semnad = []
vosem = []

gelb = []

for url in imgs_1:
  if 'gelbooru.com' in url:
    gelb.append(url)
  if url not in semnad:
    if 'gelbooru.com' not in url or  '.mp4' in url:
      semnad.append(url)

for url in imgs_2:
  if 'gelbooru.com' in url:
    gelb.append(url)
  if url not in semnad:
    if 'gelbooru.com' not in url or  '.mp4' in url:
      semnad.append(url)

for url in imgs_3:
  if 'gelbooru.com' in url:
    gelb.append(url)
  if url not in semnad:
    if 'gelbooru.com' not in url or  '.mp4' in url:
      semnad.append(url)

for url in imgs_4:
  if 'gelbooru.com' in url:
    gelb.append(url)
  if url not in semnad:
    if 'gelbooru.com' not in url or  '.mp4' in url:
      semnad.append(url)

for url in imgs_5:
  if 'gelbooru.com' in url:
    gelb.append(url)
  if url not in semnad:
    if 'gelbooru.com' not in url or  '.mp4' in url:
      semnad.append(url)




for url in imgs18_1:
  if 'gelbooru.com' in url:
    gelb.append(url)
  if url not in vosem:
    if 'gelbooru.com' not in url or  '.mp4' in url:
      vosem.append(url)


for url in imgs18_2:
  if 'gelbooru.com' in url:
    gelb.append(url)
  if url not in vosem:
    if 'gelbooru.com' not in url or  '.mp4' in url:
      vosem.append(url)


for url in imgs18_3:
  if 'gelbooru.com' in url:
    gelb.append(url)
  if url not in vosem:
    if 'gelbooru.com' not in url or  '.mp4' in url:
      vosem.append(url)

for url in imgs18_4:
  if 'gelbooru.com' in url:
    gelb.append(url)
  if url not in vosem:
    if 'gelbooru.com' not in url or  '.mp4' in url:
      vosem.append(url)


for url in imgs18_5:
  if 'gelbooru.com' in url:
    gelb.append(url)
  if url not in vosem:
    if 'gelbooru.com' not in url or  '.mp4' in url:
      vosem.append(url)



semnad=list(sorted(set(semnad)))
vosem=list(sorted(set(vosem)))
gelb=list(sorted(set(gelb)))

with open("17.json", "w") as outfile:
  json.dump(semnad, outfile, indent = 4)

with open("18.json", "w") as outfile:
  json.dump(vosem, outfile, indent = 4)  

with open("gelb.json", "w") as outfile:
  json.dump(gelb, outfile, indent = 4)  

print(f'semnad = {len(semnad)}, vosem = {len(vosem)}, gelb = {len(gelb)}')
