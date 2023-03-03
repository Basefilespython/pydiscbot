#from random_neko_list import *

#https://replit.com/@BSNIKYT/CheerfulPrestigiousHashfunction.zip
from os import system
import urllib.request
from urllib.request import HTTPError
import requests

s_version = "2.1.5"


def download_file_from_github(file_name):
  try:

    url = f'https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/{file_name}'


    def download_file(url):
      local_filename = url.split('/')[-1]
      with requests.get(url, stream=True, allow_redirects=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
      return local_filename

    file_name = download_file(url)
    pass
  except Exception as err:
    return err


def update():
  file_names = ['random_neko_list.py', 'main.py']
  er = ''
  for file_name in file_names:
    er = er + "\n" + file_name + "\n" + str(
      download_file_from_github(file_name))
    #er = download_file_from_github(file_name)
  #print(er)
  import time
  time.sleep(2)


#update()

black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"

print(f"{violet}[*] VERSION: {s_version}")

try:
  import PIL
except:
  system("pip install Pillow")
  import PIL
import os
import shutil
import json


def check_version(sversion):
  nversion = json.loads(requests.get("https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/version.json").text)['ver']
  #print(f'NEW_VERSION - {nversion}, OLD_VERSION - {sversion}')
  s1 = str(sversion).split('.')[0]
  s2 = str(sversion).split('.')[1]
  s3 = str(sversion).split('.')[2]

  n1 = str(nversion).split('.')[0]
  n2 = str(nversion).split('.')[1]
  n3 = str(nversion).split('.')[2]
  if (s1 == n1) and (s2 == n2) and (s3 == n3):
    print(
      f"{green}[*] У вас установлена самая актуальная версия скрипта!{white}")
    pass
  elif (s1 > n1) or ((s1 <= n1) and (s2 > n2)) or (((s1 <= n1) and (s2 <= n2)) and (s3 > n3)):
    print(f"{blue}[*] У вас установлена НОВЕЙШАЯ версия скрипта!{white}")
    pass
  else:
    print(f'''{yellow}[*] У вас установлена устаревшая версия скрипта!{white}''')
    ch = input("Установить новую версию? (Y/N)")
    if ch == "Y"
        download_file_from_github('main.py')
    else:
      pass


check_version(s_version)

try:
  from alive_progress import alive_bar
except ImportError:
  system("pip install alive-progress")

name_dir = "NeKo_18+"
one_path = os.getcwd()
try:
  os.mkdir(name_dir)
  name_dir = name_dir
  perm_error = False
except FileExistsError:
  pass
except PermissionError:
  perm_error = True
  name_dir = ''
  pass

print("Работающий каталог:", os.getcwd())

if str(os.name) == 'nt':
  dir_pref = "\\"
else:
  dir_pref = "//"


import os
try:
  from random_neko_list import *
except ModuleNotFoundError:
    path_1 = os.getcwd() + dir_pref + 'Dand_Crop'
    print(path_1)
    #os.chdir(path_1)
    print(os.getcwd())

import PIL
from PIL import Image

import os
one_path_1 =  os.getcwd()

def main():
  try:
    
    ur = imgs
  except NameError:
    
    
    raise SystemExit('База не обнаружена!')

  
  print("Количество изображений:", len(ur), "\n")

  err = []

  def download():
    i = 0
    with alive_bar(len(ur)) as bar:
      for url in ur:

        url = str(url)

        def ww(i):

          if "mp4" in url:
            name_file = f"{i}.mp4"
          else:
            if "gif" in url:
              name_file = f"{i}.gif"
            else:
              if "jpg" in url:
                name_file = f"{i}.jpg"
              else:
                if "webp" in url:
                  name_file = f"{i}.webp"
                else:
                  name_file = f"{i}.png"

          while not os.path.exists(name_file):
            try:
              urllib.request.urlretrieve(str(url), name_file)
              print(
                f"{green}[+] 200 (обработан): {blue}{name_file}{white}  URL: {url}"
              )
            except HTTPError as err_code:
              if err_code.code == 400:
                print(
                  f"{red}[-] {yellow}400 (некорректный запрос): {blue}{name_file}{white}  URL: {url}"
                )
              if err_code.code == 401:
                print(
                  f"{red}[-] {yellow}401 (не авторизован): {blue}{name_file}{white}  URL: {url}"
                )
              if err_code.code == 402:
                print(
                  f"{red}[-] {yellow}402 (необходима оплата): {blue}{name_file}{white}  URL: {url}"
                )
              if err_code.code == 403:
                print(
                  f"{red}[-] {yellow}403 (запрещено): {blue}{name_file}{white}  URL: {url}"
                )
              if err_code.code == 404:
                print(
                  f"{red}[-] {yellow}404 (не найдено): {blue}{name_file}{white}  URL: {url}"
                )
              else:
                pass

              err.append(f"{url}")
              break
            except urllib.error.URLError as err_code:
              if "[WinError 10054]" in str(err_code):
                print(
                  f"{red}[-] {yellow}522 (WE10054) (соединение не отвечает): {blue}{name_file}{white}  URL: {url}"
                )
              if "[Errno 99]" in str(err_code):
                print(
                  f"{red}[-] {yellow}524 (OSE99) (TCP соеденение): {blue}{name_file}{white}  URL: {url}"
                )
              if "[SSL: WRONG_VERSION_NUMBER]" in str(err_code):
                print(
                  f"{red}[-] {yellow}526 (недействительный SSL): {blue}{name_file}{white}  URL: {url}"
                )
              else:
                pass
              err.append(f"{url}")
              break

          if url not in err:
            src = one_path + dir_pref + name_file
            os.chdir(one_path)
            dest = f'{os.getcwd()}{dir_pref}{name_dir}{dir_pref}{name_file}'
            try:
              os.rename(src, dest)
            except FileExistsError:
              os.chdir(f'{os.getcwd()}{dir_pref}{name_dir}{dir_pref}')
              os.remove(name_file)
              os.chdir(one_path)
              os.rename(src, dest)
            except FileNotFoundError:
              pass
          bar()

        ww(i)
        i = i + 1

  download()
  return err

try:
  err_count = main()
except SystemExit as err:
  print(f"{red}[-] Error:{violet}",err)
  while True:
    pass

with open("errors.json", "w") as outfile:
  json.dump(err_count, outfile)


def res_def(name_dir):

  img_resize = []
  os.chdir(f'{os.getcwd()}/{name_dir}')
  path = os.getcwd()
  arts_names = []
  with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
      # печать всех записей, являющихся файлами
      if entry.is_file():
        filename, file_extension = os.path.splitext(entry.name)
        if entry.name.endswith(".jpg"):
          arts_names.append(entry.name)
        if file_extension == ".png":
          arts_names.append(entry.name)

      if entry.is_dir():
        pass

  for name_file in arts_names:
    if os.getcwd() == one_path:
      os.chdir(f'{os.getcwd()}/{name_dir}')

    os.chdir(f'{os.getcwd()}')

    try:
      im = Image.open(f'{name_file}')
      (width, height) = im.size
      height = int(height)
      width = int(width)
      im.close()

      if width > height:
        img_resize.append({f'{name_file}': 'horizontal'})
      if width < height:
        img_resize.append({f'{name_file}': 'vertical'})
      if width == height:
        img_resize.append({f'{name_file}': 'square'})
      else:
        pass
    except PIL.UnidentifiedImageError:
      img_resize.append({f'{name_file}': 'error'})

  import json
  e = '''
4320p : 7680 x 4320
2160p : 3840 x 2160
1440p : 2560 x 1440
1080p : 1920 x 1080
720p  : 1280 x 720
480p  : 854 x 480
360p  : 640 x 360
240p  : 426 x 240'''

  with open("sample.json", "w") as outfile:
    json.dump(img_resize, outfile)

  import time
  #from progress.bar import IncrementalBar
  try:
    from alive_progress import alive_bar
  except ImportError:
    system("pip install alive-progress")

  with alive_bar(len(img_resize)) as bar:
    for data in img_resize:

      try:
        img = Image.open(str(data).split("'")[1])

        viev = str(data).split("'")[3]

        if viev == "vertical":
          #pass
          (width, height) = im.size
          new_image = img.resize((height, width))
        if viev == "horizontal":
          new_image = img.resize((7680, 4320))
        if viev == "square":
          new_image = img.resize((7680, 7680))

        new_image.save(str(str(data).split("'")[1]))
        img.close()
      except PIL.UnidentifiedImageError:
        pass
      bar()


res_def(name_dir)


def in_the_papka(dir_pref):  #перемещение файлов в их папки
  os.chdir(f'{os.getcwd()}/')
  path_one = os.getcwd()
  try:
    name_dir = "vertical"
    os.mkdir(name_dir)
  except FileExistsError:
    pass
  path_vert = f'{os.getcwd()}{dir_pref}vertical'

  try:
    name_dir = "horizontal"
    os.mkdir(name_dir)
  except FileExistsError:
    pass
  path_hori = f'{os.getcwd()}{dir_pref}horizontal'

  try:
    name_dir = "square"
    os.mkdir(name_dir)
  except FileExistsError:
    pass
  path_square = f'{os.getcwd()}{dir_pref}square'

  path = os.getcwd()
  arts_names = []
  with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
      # печать всех записей, являющихся файлами
      if entry.is_file():
        if entry.name.endswith(".jpg"):
          arts_names.append(entry.name)
        if entry.name.endswith(".png"):
          arts_names.append(entry.name)
        if entry.name.endswith(".webp"):
          arts_names.append(entry.name)

      if entry.is_dir():
        pass

  with alive_bar(len(arts_names)) as bar:
    for name_file in arts_names:

      im = Image.open(f'{name_file}')
      (width, height) = im.size
      im.close()
      height = int(height)
      width = int(width)
      one_path = os.getcwd()

      if width > height:
        src = os.getcwd() + dir_pref + name_file
        dest = f'{path_hori}{dir_pref}{name_file}'
        try:
          os.rename(src, dest)
        except FileExistsError as err:
          os.remove(name_file)
          pass
        except PermissionError as err:
          print(f"PermissionError: {name_file}\nError: {err}")
          pass
      elif width < height:

        src = os.getcwd() + dir_pref + name_file
        dest = f'{path_vert}{dir_pref}{name_file}'
        try:
          os.rename(src, dest)
        except FileExistsError as err:
          os.remove(name_file)
          pass
        except PermissionError as err:
          print(f"PermissionError: {name_file}\nError: {err}")
          pass

      elif width == height:
        src = os.getcwd() + dir_pref + name_file
        os.chdir(one_path)
        dest = f'{path_square}{dir_pref}{name_file}'

        try:
          os.rename(src, dest)
        except FileExistsError as err:
          os.remove(name_file)
          pass
        except PermissionError as err:
          print(f"PermissionError: {name_file}\nError: {err}")
          pass

      elif width == "error":
        try:
          name_dir = "error"
          os.mkdir(name_dir)
        except FileExistsError:
          pass
        src = os.getcwd() + dir_pref + name_file
        os.chdir(one_path)
        dest = f'error{dir_pref}{name_file}'
        print("dest - 397", dest)
        try:
          os.rename(src, dest)
        except FileExistsError as err:
          os.remove(name_file)
          pass
        except PermissionError as err:
          print(f"PermissionError: {name_file}\nError: {err}")
          pass

      else:
        try:
          name_dir = "no_sorted"
          os.mkdir(name_dir)
        except FileExistsError:
          pass
        src = os.getcwd() + dir_pref + name_file
        os.chdir(one_path)
        dest = f'no_sorted{dir_pref}{name_file}'

        try:
          os.rename(src, dest)
        except FileExistsError as err:
          pass
        except PermissionError as err:
          print(f"PermissionError: {name_file}\nError: {err}")
          pass

      bar()


in_the_papka(dir_pref)
print("DONE")

from time import sleep

sleep(30)
