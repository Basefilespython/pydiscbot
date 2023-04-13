# <---------------------->

s_version = "2.1.21"

# <---------------------->
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"

import subprocess
import os
from os import system
import time
import logging
# <-------------------->
import sys
import json
from urllib.request import HTTPError
import urllib.request
from time import sleep
import http
import random
from datetime import datetime, timedelta

if str(os.name) == 'nt':
  dir_pref = "\\"
else:
  dir_pref = "/"


def cls():

  try:
    subprocess.call("clear")  # linux/mac
  except:
    subprocess.call("cls", shell=True)


do = os.getcwd()

# <-------------------------->

en_loc_reserve = {
  '0': f'''{'='*15}- Connection statuses -{'='*15}
{green}- 200 - Success!{white}
{'='*10} HTTP ERROR CODEs: {'='*10}
{red}- 400 - The script was unable to parse the URL.
- 401 - Authorization is needed ... you need to download it manually.
- 402 - Similar to 401, access after payment.
- 403 - Site/Browser/Anti-Virus denied you access to access this URL (perhaps VPN).
- 404 - Not found, or this is an outdated link.
{white}{'='*10} TIMEOUT ERROR CODEs: {'='*10}
{red}- 522 - The connection is not responding (maybe ILV blocked).
- 524 - TCP connection failed. (internal OS errors).
- 526 - Certificate blocking (rather different times, or parental control)
{white}{'='*10} OTHER: {'='*10}
{violet}- 101 - You are disconnected from the Internet.
- 102 - Error processing URL.{white}''',
  '1': 'Time',
  '2': 'Operating system',
  '3': 'Version',
  '4': 'You have the latest version of the script installed!',
  '5': 'Failed to get working directory.',
  '6':
  'Your OS is similar to Colab. All downloaded files will be downloaded to your Google Drive. Or rather, to the subfolder where this file is saved.',
  '7': 'RESTART THE SKIP RUNNING ENVIRONMENT.',
  '8': 'Base not found!',
  '9': 'You have an outdated version of the script installed!',
  '10': 'Install new version?',
  '11': 'Version check failed!',
  '12': 'Working directory',
  '13': 'Download to',
  '14': 'Number of images',
  '15': 'You aborted code execution',
  '16': 'Crop images in database?',
  '17': 'Localization file was not found!'
}

# <------------------------->


def set_logger_settings():
  py_logger = logging.getLogger(__name__)
  py_logger.setLevel(logging.INFO)

  s = str(str((str(datetime.now())).split()[1]).split(".")[0]).split(":")[2]
  m = str(str((str(datetime.now())).split()[1]).split(".")[0]).split(":")[1]
  h = str(str((str(datetime.now())).split()[1]).split(".")[0]).split(":")[0]

  py_handler = logging.FileHandler(f"{s}-{m}-{h}.log", mode='w')
  #py_handler.setFormatter(logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s"))
  py_handler.setFormatter(
    logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
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
  os.chdir(f'{do + dir_pref + "logging"}')
  py_logger = set_logger_settings()
  pass
except PermissionError:
  py_logger = set_logger_settings()
  pass

try:
  import requests
  py_logger.info(f"Import module [requests] successfully.")
except:
  system("pip install requests")
  try:
    import requests
    py_logger.info(
      f"Import module [requests] failed -> Import module [requests] successfully."
    )
  except ModuleNotFoundError:
    py_logger.error("Import module [requests] failed.")

try:
  import PIL
  py_logger.info(f"Import module [PIL] successfully.")
except:
  system("pip install Pillow")
  try:
    import PIL
    py_logger.info(
      f"Import module [PIL] failed -> Import module [PIL] successfully.")
  except ModuleNotFoundError:
    py_logger.error("Import module [PIL] failed.")

try:
  from PIL import Image
  py_logger.info(f"[Import module from PIL] successfully.")
except ModuleNotFoundError:
  system('pip install Pillow')
  try:
    from PIL import Image
    py_logger.info(
      f"[Import module from PIL] failed -> [Import module from PIL] successfully."
    )
  except ModuleNotFoundError:
    py_logger.error("[Import module from PIL] failed.")

try:
  from alive_progress import alive_bar
  alive_a = True
  py_logger.info(f"[Import alive_bar from alive_progress] successfully.")
except:
  system("pip3 install alive-progress")
  try:
    from alive_progress import alive_bar
    alive_a = True
    py_logger.info(
      f"[Import module from PIL] failed -> [Import module from PIL] successfully."
    )
  except ModuleNotFoundError:
    alive_a = False
    print(f'{red}[!] ModuleNotFoundError: alive_progress.{white}')
    py_logger.info(f"[Import alive_bar from alive_progress] failed.")



def download_file_from_github(ind,file_name):
  if ind == 0:
    url = f'https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/{file_name}'
  if ind == 1:
    url = f'https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/localization/{file_name}'
  local_filename = url.split('/')[-1]
  #def l(file_name):
  try:
    py_logger.info(f"[Downloading file] Name: {file_name}")
    with requests.get(url, stream=True, allow_redirects=True) as r:
      r.raise_for_status()
      with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
          f.write(chunk)
    return 'ok'
  #return l(file_name)
  except requests.exceptions.HTTPError as err:
    print(err)
    if '404' in str(err):
      return "errне найдено"
  except Exception as err:
    return "err", err


def check(ind,file_name):
  er = ""
  out = download_file_from_github( ind, file_name)
  if "err" in out:
    out = str(out).replace('err', '')
    er = er + f"{red}[-] DownloadingFileError ({out}): {file_name}{white}\n"
  print(er)





localization = input(f'Выберите локализацию (ru) / Select localization (en) >>> ').upper()

if localization == 'RU':
  
  try:
    from RU import ru_loc as loc
    #loc_tag = 'ru'
  except ModuleNotFoundError:
    loc = en_loc_reserve
    try:
      from localization.RU import ru_loc as loc
      #loc_tag = 'ru'
    except ModuleNotFoundError:
      py_logger.warning(
        f"Localization for the Russian language was not found. Trying to download Localization..."
      )
      posle = os.getcwd()
      do_1212 = os.getcwd(
      ) + dir_pref + 'localization' + dir_pref # + 'RU.py'
      os.chdir(do_1212)
      check(1, 'RU.py')
      #download_file_from_github('RU.py')
      os.chdir(posle)
      try:
        try:
          # import sys
          sys.path.insert(1, '../Dand_Crop')
          from localization.RU import ru_loc as loc
          #loc_tag = 'ru'
          py_logger.info(
            "The localization for the Russian language has been successfully imported!"
          )
        except NameError:
          try:

            from localization.RU import ru_loc as loc
            #loc_tag = 'ru'
            py_logger.info(
              "The localization for the Russian language has been successfully imported!"
            )
          except:
            #loc_tag = 'en'
            loc = en_loc_reserve
            py_logger.critical(
              f"localization for the Russian language was not found!")
            print(f'\n[!] {loc["17"]}')
            print(
              'Локализация была изменена на английскую, из-за отсутствия файла конфигурации.\nThe localization has been changed to English, due to the missing configuration file.'
            )
            #raise SystemExit(f'\n[!] {loc["17"]}')
      except ImportError:
        #loc_tag = 'en'
        loc = en_loc_reserve
        py_logger.critical(
          f"localization for the Russian language was not found!")
        print(f'\n[!] {loc["17"]}')
        print(
          'Локализация была изменена на английскую, из-за отсутствия файла конфигурации.\nThe localization has been changed to English, due to the missing configuration file.'
        )

if localization == 'EN':
  try:
    from EN import en_loc as loc
    #loc_tag = 'en'
  except ModuleNotFoundError:
    loc = en_loc_reserve
    try:
      from localization.RU import *
    except ModuleNotFoundError:
      py_logger.warning(
        f"English localization was not found. Trying to download Localization..."
      )
      posle = os.getcwd()
      do_1212 = os.getcwd(
      ) + dir_pref + 'localization' + dir_pref  #+ 'random_neko_list.py'
      os.chdir(do_1212)
      download_file_from_github(0,'EN.py')
      os.chdir(posle)
      try:
        try:
          # import sys
          sys.path.insert(1, '../Dand_Crop')
          from localization.EN import en_loc as loc
          #loc_tag = 'en'
          py_logger.info(
            "English localization has been successfully imported!")
        except NameError:
          try:

            from localization.EN import en_loc as loc
            #loc_tag = 'en'
            py_logger.info(
              "English localization has been successfully imported!")
          except:
            py_logger.critical(
              f"localization for the English language was not found!")
            raise SystemExit(f'\n[!] {loc["17"]}')
      except ImportError:
        py_logger.critical(
          f"localization for the English language was not found!")
        raise SystemExit(f'\n[!] {loc["17"]}')


#print(loc)


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
      py_logger.info(f"[Import Fore from colorama] failed.")

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

#cls()
try:
  do = os.getcwd()
except OSError:
  py_logger.critical(f"Unable to get a working directory.")
  raise OSError(f'{red}[!] {loc["7"]}')

if '/content' in os.getcwd():
  py_logger.info(f"Colab platform found.")
  try:
    system(
      '!mkdir data && wget https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/setup.py'
    )
  except:
    pass
  print(f'''{white}{'='*15}- {red}WARNING!{white} -{'='*15}''')
  dd = loc["6"]
  print(f"{red} {dd} {white}")

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
    raise OSError(f'{red}[!] {loc["7"]}')
  try:
    os.mkdir('Dand_Crop')
  except FileExistsError:
    pass
  os.chdir(os.getcwd() + '/' + 'Dand_Crop')
  system('!touch "/content/MyDrive/Colab Notebooks/setup.py"')

try:
  from random_neko_list import *
  py_logger.info("The database has been successfully imported!")
except ModuleNotFoundError:
  try:
    from modules.random_neko_list import *
  except ModuleNotFoundError:
    py_logger.warning(f"Database not found! Trying to download database...")
    posle = os.getcwd()
    do_1212 = os.getcwd(
    ) + dir_pref + 'modules' + dir_pref + 'random_neko_list.py'
    os.chdir(do_1212)
    download_file_from_github(0,'random_neko_list.py')
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
          raise SystemExit(f'\n[!] {loc["8"]}')
    except ImportError:
      py_logger.critical(f"Database not found!")
      raise SystemExit(f'\n[!] {loc["8"]}')





def update():
  file_names = ['random_neko_list.py', 'main.py']
  for file_name in file_names:
    check(file_name)

  import time
  time.sleep(2)


# update()

print(f'''{'='*15}- {loc['1']} -{'='*15}{turquoise}
{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}{white}''')


def old(nversion):
  py_logger.warning(
    f"An obsolete version of the script has been found (NEW-{nversion}, OLD-{s_version})!"
  )
  print(f"{violet}[*] OLD-VERSION: {s_version}, NEW-VERSION: {nversion}")
  print(f'''{yellow}[*] {loc["9"]}{white}''')
  ch = input(f"{green}[!]{white} {loc['10']} (Y/N) >>> ")
  if ch == "Y":
    check("main.py")
    raise SystemError("")
  else:
    pass


#NT / POSIX

print(f'''{'='*15}- {loc['2']} -{'='*15}
{yellow}[*] OS Name: {os.name.upper()}{white}''')

py_logger.info(f'''{'='*15}- OS -{'='*15}''')
py_logger.info(f'''[*] OS Name: {os.name.upper()}''')


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
    print(f'''{'='*15}- {loc['3']} -{'='*15}''')
    if s1 >= n1:
      if s2 >= n2:
        if s3 >= n3:
          py_logger.info(
            f"The current version of the script has been found ({s_version})!")
          print(f'''{violet}[*] {loc['3']}: {s_version}''')
          print(
            f'''{green}[*] {loc["4"]}{white}'''
          )

        else:
          old(nversion)
      else:
        old(nversion)
    else:
      old(nversion)
  else:
    py_logger.warning(f"Version check failed.")
    print(f'''{red}[!] {loc['18']}
{violet}[*] VERSION: {s_version}''')


check_version(s_version)

name_dir = "data_2"
one_path = os.getcwd()

print(f"{loc['0']}")

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

#print(f'''{loc["0"]}''')

py_logger.info(f"Dir_pref = {dir_pref}")
print(f'''{white}{'='*15}- {loc['17']} -{'='*15}
{green}[*] {loc["12"]}: {os.getcwd()}
[*] {loc["13"]} :      {os.getcwd() + dir_pref +str(name_dir)}''')

py_logger.info(f'''{'='*15}- PATH -{'='*15}''')
py_logger.info(f"[*] Working Directory: {os.getcwd()}")
py_logger.info(f'''[*] Download in:      {os.getcwd() + dir_pref +str(name_dir)}''')






chosing_directory = imgs
try:
  from exctensions_module import sizing_dict
  dict_size = sizing_dict(chosing_directory)
except:
  dict_size = None
  pass



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
                print(
                  f"{green}[+] 200: {blue}{name_file}{white}  URL: {url[0:ind]}"
                )
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





startTime = time.time()



def main():
  if dict_size == None:
    ur = chosing_directory
  else:
    ur  = dict_size

  print(f'''{white}{'='*15}- {loc['14']} - {len(ur)} -{'='*15}''')

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
          #ww1(i)
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


  download()
  return err_dict, vk_403_err, err_info











try:
  err_count, vk_403_err, err_info = main()


  py_logger.info(f'''{'='*15}- Downloading OK -{'='*15}''')
except KeyboardInterrupt:
  py_logger.info(f'''{'='*15}- Downloading KeyboardInterrupt -{'='*15}''')
  py_logger.critical(f'''The user aborted code execution.''')
  print(f'{red}[!] {loc["15"]}...')

endTime = time.time()

#n = endTime - startTime

#from datetime import datetime


print(f"Время выполнения скрипта / Script execution time: {str(timedelta(seconds = (endTime - startTime))).split('.')[0]}")


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

  if ('errors.json' in str(os.path.exists(os.getcwd()))):# or ('vk403.json' in os.path.exists(os.getcwd())) or ('err_info.json' in os.path.exists(os.getcwd())):  
    if 'config.json' not in os.path.exists(os.getcwd()):
      if input(fr'\n{green}[*] Создавать в дальнейших запусках скрипта файлы с ошибками? (Y\n)>>> ') == 'Y':
        with open('config.json', 'a', encoding='utf-8') as f:
          f.write('{"save files with error information" : True}')
except NameError:
  pass





py_logger.info(
  f'''The database download was completed in [{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]'''
)




try:
  from module_res_def import res_def
  ch = input(f'\n{red}[!] {loc["16"]} (Y/n) >>> {white}')
  py_logger.info(
    f'''The meaning of calling the image processing function:  {ch}.''')

  if ch == 'Y':
    res_def(name_dir)
  else:
    pass
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



if input('Скрипт завершил работу... Запустить бесконечный цикл выполнения? (Y/N) >>> ') == 'Y':
  while True:
    cls()
    main()
else:
  pass
sleep(30)
