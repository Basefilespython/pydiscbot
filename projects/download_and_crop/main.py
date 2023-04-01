import subprocess
import os
from os import system
import time
import logging

if str(os.name) == 'nt':
  dir_pref = "\\"
else:
  dir_pref = "/"

do = os.getcwd()



def set_logger_settings():
  py_logger = logging.getLogger(__name__)
  py_logger.setLevel(logging.INFO)
  py_handler = logging.FileHandler(f"loger.log", mode='w')
  #py_handler.setFormatter(logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s"))
  #py_handler.setFormatter(logging.Formatter("[%(asctime)s] - [%(levelname)s] - [%(message)s]"))
  py_handler.setFormatter(
    logging.Formatter(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}] - [%(levelname)s] - [%(message)s]"))
  py_logger.addHandler(py_handler)
  os.chdir(do)
  py_logger.info(
    f"{'='*15}- STARTing script in [{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}] -{'='*15}"
  )
  return py_logger


try:
  os.mkdir('logging')
  os.chdir(f'{do + dir_pref + "logging"}')
  py_logger = set_logger_settings()
except FileExistsError:
  py_logger = set_logger_settings()
  pass
except PermissionError:
  py_logger = set_logger_settings()
  pass


def cls():

  try:
    subprocess.call("clear")  # linux/mac
  except:
    subprocess.call("cls", shell=True)


cls()

from time import sleep
import http

try:
  from PIL import Image
  py_logger.info(f"[Import module from PIL] successfully.")
except ModuleNotFoundError:
  system('pip install Pillow')
  from PIL import Image
  py_logger.info(
    f"[Import module from PIL] failed -> [Import module from PIL] successfully."
  )

import sys
import json
from urllib.request import HTTPError
import urllib.request

import random

try:
  import requests
  py_logger.info(f"Import module [requests] successfully.")
except:
  system("pip install requests")
  import requests
  py_logger.info(
    f"Import module [requests] failed -> Import module [requests] successfully."
  )

s_version = "2.1.18"

black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"

try:
  from alive_progress import alive_bar
  alive_a = True
  py_logger.info(f"[Import alive_bar from alive_progress] successfully.")
except:
  system("pip install alive-progress")
  #system("pip3 install alive-progress")
  try:
    from alive_progress import alive_bar
    alive_a = True
    py_logger.info(
      f"[Import module from PIL] failed -> [Import module from PIL] successfully."
    )
  except ModuleNotFoundError:
    alive_a = False
    print(f'{red}[!] ModuleNotFoundError: alive_progress.{white}')
    py_logger.info(f"[Import module from PIL] failed.")


def logo():
  try:
    from colorama import Fore
    colors = [
      Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA,
      Fore.WHITE
    ]
  except:
    system('pip install colorama')
    try:
      from colorama import Fore
      colors = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA,
        Fore.WHITE
      ]
    except:
      print(f'{red}[!] ModuleImportError: colorama.{white}')
      colors = [red, green, yellow, blue, violet, turquoise, white]

  color1 = random.choice(colors)
  colors.remove(color1)
  color2 = random.choice(colors)
  #print(f'''{color1}


#[--------------------------------]
#    [------------------------]
#        [----------------]
#            [----------]
#  {white}''')

logo()

try:
  import PIL
except:
  system("pip install Pillow")
  import PIL

try:
  do = os.getcwd()
except OSError:
  py_logger.critical(f"Unable to get a working directory.")
  raise OSError(f'{red}[!] ПЕРЕЗАПУСТИТЕ СРЕДУ ВЫПОЛНЕНИЯ СКИПТА.')

if '/content' in os.getcwd():
  py_logger.info(f"Colab platform found.")
  try:
    system(
      '!mkdir data && wget https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/setup.py'
    )
  except:
    pass
  print(f'''{white}{'='*15}- {red}WARNING!{white} -{'='*15}''')
  print(
    f"{red}Ваша OS похожа на Colab. Все скачанные файлы будут скачиваться в ваш Google Drive. А точнее в подпапку где сохранен данный файл.{white}"
  )
  from google.colab import drive
  try:
    print(f'''{white}{'='*15}- {green}Connecting...{white} -{'='*15}''')
    drive.mount("/content/MyDrive", force_remount=True)
  except:
    print(f'''{white}{'='*15}- {red}Connecting Failed...{white} -{'='*15}''')
    py_logger.critical(f"Unable to connect to Google Collab")
    raise SystemError(f'{red}[!] Error to connecting to drive...{white}')
  print(f'''{white}{'='*15}- {green}Connecting OK...{white} -{'='*15}''')

  try:
    per1 = os.getcwd()
    os.chdir('/content/MyDrive/MyDrive/Colab Notebooks')
    per2 = os.getcwd()
    py_logger.info(f"[Directory change] {per1} -> {per2}")
  except OSError as err:
    raise OSError(f'{red}[!] ПЕРЕЗАПУСТИТЕ СРЕДУ ВЫПОЛНЕНИЯ СКИПТА.')
  try:
    os.mkdir('Dand_Crop')
  except FileExistsError:
    pass
  os.chdir(os.getcwd() + '/' + 'Dand_Crop')
  system('!touch "/content/MyDrive/Colab Notebooks/setup.py"')


def download_file_from_github(file_name):
  url = f'https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/{file_name}'
  local_filename = url.split('/')[-1]
  try:
    py_logger.info(f"[Downloading file] Name: {file_name}")
    with requests.get(url, stream=True, allow_redirects=True) as r:
      r.raise_for_status()
      with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
          f.write(chunk)
    return 'ok'
  except Exception as err:
    return "err", err


try:
  from random_neko_list import *
  py_logger.info("The database has been successfully imported!")
except ModuleNotFoundError:
  try:
    from modules.random_neko_list import *
  except ModuleNotFoundError:
    py_logger.warning(f"Database not found! Trying to download database...")
    posle = os.getcwd()
    do_1212 = os.getcwd() + dir_pref + 'modules' + dir_pref
    os.chdir(do_1212)
    download_file_from_github('random_neko_list.py')
    os.chdir(posle)
    try:
      try:
        # import sys
        sys.path.insert(1, '../Dand_Crop')
        from random_neko_list import *
        py_logger.info("The database has been successfully imported!")
      except NameError:
        try:

          from modules.random_neko_list import *
          py_logger.info("The database has been successfully imported!")
        except:
          py_logger.critical(f"Database not found!")
          raise SystemExit('\n[!] База не обнаружена!')
    except ImportError:
      py_logger.critical(f"Database not found!")
      raise SystemExit('\n[!] База не обнаружена!')


def check(file_name):
  er = ""
  out = download_file_from_github(file_name)
  if "err" in out:
    out = out.replace('err', '')
    er = er + f"{red}[-] DownloadingFileError: {file_name}{white}\n"
  print(er)


def update():
  file_names = ['random_neko_list.py', 'main.py']
  for file_name in file_names:
    check(file_name)

  import time
  time.sleep(2)


# update()

cls()

print(f'''{'='*15}- TIME -{'='*15}{turquoise}
{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}{white}''')


def old(nversion):
  py_logger.warning(f"An obsolete version of the script has been found!")
  print(f"{violet}[*] OLD-VERSION: {s_version}, NEW-VERSION: {nversion}")
  print(f'''{yellow}[*] У вас установлена устаревшая версия скрипта!{white}''')
  ch = input(f"{green}[!]{white} Установить новую версию? (Y/N) >>> ")
  if ch == "Y":
    check("main.py")
    raise SystemError("")
  else:
    pass


#NT / POSIX

print(f'''{'='*15}- OS -{'='*15}
{yellow}[*] OS Name: {os.name.upper()}{white}''')


def check_version(sversion):
  try:
    nversion = json.loads(
      requests.get(
        "https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/version.json"
      ).text)['ver']
  except:
    nversion = None
  if nversion != None:
    s1, s2, s3, n1, n2, n3 = str(sversion).split('.')[0], str(sversion).split(
      '.')[1], str(sversion).split('.')[2], str(nversion).split('.')[0], str(
        nversion).split('.')[1], str(nversion).split('.')[2]
    print(f'''{'='*15}- VERSION -{'='*15}''')
    if s1 >= n1:
      if s2 >= n2:
        if s3 >= n3:
          py_logger.info(f"The current version of the script has been found!")
          print(f'''{violet}[*] VERSION: {s_version}''')
          print(
            f'''{green}[*] У вас установлена самая актуальная версия скрипта!{white}'''
          )

        else:
          old(nversion)
      else:
        old(nversion)
    else:
      old(nversion)
  else:
    py_logger.warning(f"Version check failed.")
    print(f'''{red}[!] Проверка версии не удалась!
{violet}[*] VERSION: {s_version}''')


check_version(s_version)

name_dir = "data"
one_path = os.getcwd()
try:
  os.mkdir(name_dir)
  name_dir = name_dir
  perm_error = False
  py_logger.info(
    f"Created a new directory named [{name_dir}], perm_error = False.")
except FileExistsError:
  py_logger.warning(f"A directory with the same name [{name_dir}] was found.")
  pass
except PermissionError:
  py_logger.warning("An error occurred while creating a new directory.")
  perm_error = True
  name_dir = ''
  pass

print(f'''{'='*15}- Статусы соединения -{'='*15}
{green}- 200 - Успешно!{white}
{'='*10} HTTP ERROR CODEs: {'='*10}
{red}- 400 - Скрипт не смог обработать URL.
- 401 - Нужна авторизация...надо скачивать ручками.
- 402 - Аналогично 401, доступ после оплаты.
- 403 - Сайт/Браузер/Антивирус запретил вам доступ обращаться по этому URL (возможно дело в VPN).
- 404 - Не найдено, или это устаревшая ссылка.
{white}{'='*10} TIMEOUT ERROR CODEs: {'='*10}
{red}- 522 - Соединение не отвечает (может РКН заблокал). 
- 524 - TCP соеденение провалено. (внутренние ошибки OS).
- 526 - Блокировка сертификата/ом (скорее разное время, или родительский контроль)
{white}{'='*10} ПРОЧЕЕ: {'='*10}
{violet}- 101 - Вы отключены от сети Internet.
- 102 - Ошибка связанная с обработкой URL.
- ___ - Неизвестная ошибка.{white}''')

py_logger.info(f"Dir_pref = [ {dir_pref} ]")
print(f'''{white}{'='*15}- PATH -{'='*15}
{green}[*] Работающий каталог: {os.getcwd()}
[*] Скачивание в :      {os.getcwd() + dir_pref +str(name_dir)}''')

py_logger.info(f'''{'='*15}- PATH -{'='*15}''')
py_logger.info(f"Working Directory: {os.getcwd()}")
py_logger.info(f''' Download in:      {os.getcwd() + dir_pref +str(name_dir)}''')




def download_function(url,name_file, err_dict, err_info, vk_403_err):
              if '?size=' in url:
                ind = url.find('?size=')
              else:
                if '?extra=' in url:
                  ind = url.find('?extra=')
                else:
                  ind = len(url)

              try:
                urllib.request.urlretrieve(str(url), name_file)
                #print(f"{green}[+] 200: {blue}{name_file}{white}  URL: {url[0:ind]}")
                py_logger.info(
                  f'''File with name {name_file} and link ({url}) was downloaded successfully.'''
                )
                return '200', err_dict, err_info, vk_403_err
              except HTTPError as err_code:

                print(
                  f"{red}[-] {red}{err_code.code}: {blue}{name_file}{white}  URL: {url[0:ind]}"
                )

                err_dict.append(f"{url}")
                err_info.append({f'{name_file}': f'{err_code.code}'})
                if 'userapi.com' in url and err_code.code == 403:
                  vk_403_err.append(f'{url}')
                py_logger.warning(
                  f'''File named {name_file} and link ({url}) was NOT downloaded and returned code: {err_code.code}'''
                )
                return f'{err_code.code}', err_dict, err_info, vk_403_err

              except urllib.error.URLError as err_code:
                if "[WinError 10054]" in str(err_code):
                  print(
                    f"{red}[-] {red}522: {blue}{name_file}{white}  URL: {url[0:ind]}"
                  )
                  py_logger.warning(
                    f'''File with name {name_file} and link ({url}) was NOT downloaded due to lack of server response.'''
                  )
                  err_info.append({f'{name_file}': "522"})
                  return f'522', err_dict, err_info, vk_403_err
                if "[Errno 99]" in str(err_code):
                  print(
                    f"{red}[-] {red}524: {blue}{name_file}{white}  URL: {url[0:ind]}"
                  )
                  err_info.append({f'{name_file}': "524"})
                  py_logger.warning(
                    f'''File with name {name_file} and link ({url}) was NOT downloaded due to connection failure.'''
                  )
                  return f'524', err_dict, err_info, vk_403_err
                if "[SSL: WRONG_VERSION_NUMBER]" in str(err_code):
                  print(
                    f"{red}[-] {red}526: {blue}{name_file}{white}  URL: {url[0:ind]}"
                  )
                  err_info.append({f'{name_file}': "526"})
                  py_logger.warning(
                    f'''The file with name {name_file} and link ({url}) was NOT downloaded due to mismatch of security certificate or parental controls.'''
                  )
                  return f'526', err_dict, err_info, vk_403_err
                else:
                  pass

                err_dict.append(f"{url}")
                if 'userapi.com' in url: vk_403_err.append(f'{url}')

              except http.client.RemoteDisconnected:
                print(
                  f"{violet}[-] {violet}101: {blue}{name_file}{white}  URL: {url[0:ind]}"
                )
                err_info.append({f'{name_file}': "101"})
                py_logger.warning(
                  f'''The file with the name {name_file} and link ({url}) was NOT downloaded due to the user disconnecting from the Internet.'''
                )
                return f'101', err_dict, err_info, vk_403_err

              except ConnectionResetError:
                print(
                  f"{violet}[-] {violet}101: {blue}{name_file}{white}  URL: {url[0:ind]}"
                )
                err_info.append({f'{name_file}': "101"})
                py_logger.warning(
                  f'''The file with the name {name_file} and link ({url}) was NOT downloaded due to the user disconnecting from the Internet.'''
                )
                return f'101', err_dict, err_info, vk_403_err

              except ValueError as err:
                print(
                  f"{violet}[?] 102: {blue}{name_file}{white}  URL: {url[0:ind]}"
                )
                err_info.append({f'{name_file}': f"{err}"})
                py_logger.warning(
                  f'''File with name {name_file} and link ({url}) was NOT downloaded due to unformatted link.'''
                )
                return f'102', err_dict, err_info, vk_403_err
              except Exception as err:
                print(
                  f"{violet}[?] ___: {blue}{name_file}{white}  URL: {url[0:ind]}"
                )
                err_info.append({f'{name_file}': f"{err}"})
                py_logger.warning(
                  f'''File with name {name_file} and link ({url}) was NOT loaded due to unknown error: {err}.'''
                )
                return f'___', err_dict, err_info, vk_403_err



chosing_directory = imgs18

from exctensions_module import sizing_dict
dict_size = sizing_dict(chosing_directory)

print(f"{white}")

def main():

  ur = chosing_directory = dict_size

  print(f'''{white}{'='*15}- Количество изображений - {len(ur)} -{'='*15}''')

  py_logger.info(f'''{'='*15}- Downloading Info -{'='*15}''')

  err_dict = []
  vk_403_err = []
  err_info = []

  name_file_and_ext = []

  def download():
    i = 0


    if alive_a == True:
      with alive_bar(len(ur)) as bar:

        for zn in ur:
          #print("512", zn[f"{list(zn.keys())[0]}"])
          # {'https://sun9-48.userapi.com/impg/0B8_GiHN8UAPS4c4V2VhL1qVijnEMugYiYAprg/fVytxCYhXWI.jpg?size=768x512&quality=95&sign=3e76087ea05610fea034e2b4df1bd24a&type=album': '.jpg'}
          url = list(zn.keys())[0]
          #print(list((zn)))
          exten = zn[f"{list(zn.keys())[0]}"]
          #print(url, exten)
          #raise

          def ww1(i, url, err_dict, err_info, vk_403_err, exten):




            name_file = f"{i}{exten}"
            while not os.path.exists(name_file):
                #print(name_file, url)
                #print(download_function(url,name_file, err_dict, err_info, vk_403_err))
                status, err_dict, err_info, vk_403_err = download_function(url,name_file, err_dict, err_info, vk_403_err)
                #print(status)
                if status != '200':
                  break
                else:
                  pass



            if url not in err_dict:
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

          ww1(i,url, err_dict, err_info, vk_403_err, exten)
          i = i + 1
    if alive_a == False:
       
        for zn in ur:
          #print("512", zn[f"{list(zn.keys())[0]}"])
          # {'https://sun9-48.userapi.com/impg/0B8_GiHN8UAPS4c4V2VhL1qVijnEMugYiYAprg/fVytxCYhXWI.jpg?size=768x512&quality=95&sign=3e76087ea05610fea034e2b4df1bd24a&type=album': '.jpg'}
          url = list(zn.keys())[0]
          #print(list((zn)))
          exten = zn[f"{list(zn.keys())[0]}"]
          #print(url, exten)
          #raise

          def ww2(i, url, err_dict, err_info, vk_403_err, exten):




            name_file = f"{i}{exten}"
            while not os.path.exists(name_file):
                #print(name_file, url)
                #print(download_function(url,name_file, err_dict, err_info, vk_403_err))
                status, err_dict, err_info, vk_403_err = download_function(url,name_file, err_dict, err_info, vk_403_err)
                #print(status)
                if status != '200':
                  break
                else:
                  pass



            if url not in err_dict:
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


          ww2(i,url, err_dict, err_info, vk_403_err, exten)
          i = i + 1

  return err_dict, vk_403_err, err_info


try:
  err_count, vk_403_err, err_info = main()
except KeyboardInterrupt:
  py_logger.critical(f'''The user aborted code execution.''')
  print(f'{red}[!] Вы прервали выполнение кода...')

try:
  if len(err_count) != 0:
    with open("errors.json", "w") as outfile:
      json.dump(err_count, outfile, indent=4)
    py_logger.info(f'''File created [errors.json]''')

  if len(vk_403_err) != 0:
    with open("vk403.json", "w") as outfile:
      json.dump(vk_403_err, outfile, indent=4)
    py_logger.info(f'''File created [vk403.json]''')

  if len(err_info) != 0:
    with open("err_info.json", "w") as outfile:
      json.dump(err_info, outfile, indent=4)
    py_logger.info(f'''File created [err_info.json]''')

except NameError:
  pass

py_logger.info(
  f'''The database download was completed in [{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]'''
)

try:
  from module_res_def import res_def
  ch = input(f'\n{red}[!] Откадрировать изображения в базе? (Y/n) >>> {white}')
  if ch == 'Y':
    res_def(name_dir)
  else:
    pass
  py_logger.info(
    f'''The meaning of calling the image processing function:  {ch}.''')
except KeyboardInterrupt:
  py_logger.info(
    f'''The user has canceled an image encoding call request (KeyboardInterrupt).'''
  )
except Exception as err:
  py_logger.info(
    f'''The script has canceled an image encoding call request ({err}).''')



try:
  from module_in_the_papka import in_the_papka
  in_the_papka(dir_pref)
except Exception as err:
  pass

print("DONE")
sleep(30)
