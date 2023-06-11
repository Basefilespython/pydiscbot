# <---------------------->

# ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
# ▐░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░▌
# ▐░█░░░█░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░▌
# ▐░█░░░░█░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌
# ▐░█░░░░█░░░███░░░███░░░░████░░░░░░░░░░░█░░░░░░░█░███░░░░████░░░░████░░▌
# ▐░█░░░░█░░█░░█░░░█░░█░░█░░░█░░░░░░░░░░░█░░░░░░░██░░░█░░█░░░░█░░█░░░░█░▌
# ▐░█░░░█░░░█░░█░░░█░░█░░█░░░█░░░░░░░░░░░█░░░░█░░█░░░░░░░█░░░░█░░█░░░░█░▌
# ▐░████░░░░░██░█░░█░░█░░░███░█░░█████░░░░████░░░█░░░░░░░░████░░░█████░░▌
# ▐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░▌
# ▐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░▌
# ▐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌
# ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌

main_script_version = "2.1.30"

# <---------------------->

# The script was written ©https://vk.com/id435600030©
# Download from https://github.com/Basefilespython/pydiscbot/tree/main

black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"


# <-------------------------->

import subprocess
import os
from os import system
import time
import logging
import sys
import json
from urllib.request import HTTPError
import urllib.request
from time import sleep
import http
import random
from datetime import datetime, timedelta
from threading import Thread

if str(os.name) == "nt":
  dir_pref = "\\"
else:
  dir_pref = "/"

# <-------------------------->


def cls():
  try:
    subprocess.call("clear")  # linux/mac
  except:
    subprocess.call("cls", shell=True)


# <-------------------------->

do = os.getcwd()

# <-------------------------->


def old_Thread(nversion,sversion, name_file,name_d,loc_n,redir=os.getcwd()):
  if val_toast == True:
    if name_file == 'version.json':
       loc_n = loc['9']
    else:
      loc_n = loc['30']
    tit = f'{loc_n}\n{sversion} --> {nversion}'
    # toast(
    #       #title = tit,
    #       #loc_n, 
    #       buttons=[{'activationType': 'protocol','arguments': check(0, name_file,redir),'content': 'Download'}],
    #       icon = {'src': 'https://unsplash.it/64?image=669','placement': 'appLogoOverride'})
    #toast('Hello', 'Hello from Python', button={'activationType': 'protocol', 'arguments': 'https://google.com', 'content': 'Open Google'})
    toast(
          title = tit,
          icon = {'src': 'https://unsplash.it/64?image=669','placement': 'appLogoOverride'},
          buttons=[{'activationType': 'protocol','arguments': 'https://github.com/Basefilespython/pydiscbot/tree/main/projects/download_and_crop/setup','content': 'Download'}],
          #callback_on_click=check(0, name_file,redir)
          )
    # toast(tit,f'{loc_n}...',buttons=[
    #       {
    #         'activationType': 'protocol',
    #         'arguments': check(0, name_file,redir),
    #         'content': 'Download'
    #       }])
  else:
    pass


def old(loc_n_, nversion_,sversion_, name_file_, name_d_, redir_=os.getcwd(), Th= False):
  if Th == False:
    if name_file_ == 'random_neko_list_v.json':
      name_file_ = name_file_.replace('_v.json','.py')
    if name_file_ == 'version.json':
      name_file_ =  'main.py'
    py_logger.warning(f"An obsolete version of the script has been found (NEW-{nversion_}, OLD-{sversion_})!")
    print(f"""{yellow}[*] {name_d_}{white}""")
    print(f"{violet}[*] An old version: {sversion_}, A new version: {nversion_}")
    ch = input(f"{green}[!] {loc['10']} (Y/N) >>> ")
    print(white)
    if ch == "Y":
      check(0, name_file_,redir_)
      raise ForcedRebootException(loc["19"])
    else:
      pass
  
  if Th == True:
    old_Thread(nversion_,sversion_, name_file_, name_d_, loc_n_, redir=os.getcwd())







def ch_version(url,sversion,loc_n,name_d,print_val):
  redir_cd = os.getcwd() + dir_pref + 'modules'
  name_file = url.split('/')[-1]
  try:nversion = json.loads(requests.get(url).text)["ver"]
  except Exception as err:nversion = None
  if print_val == True: Th_val = False
  else: Th_val = True

  if nversion != None:
    s1, s2, s3, n1, n2, n3 = (
     str(sversion).split(".")[0],
     str(sversion).split(".")[1],
     str(sversion).split(".")[2],
     str(nversion).split(".")[0],
     str(nversion).split(".")[1],
     str(nversion).split(".")[2])
    if s1 >= n1:
      if s2 >= n2:
        if s3 >= n3:
          if print_val == True:
            py_logger.info(f"The current version of the script has been found ({sversion})!")
            print(f"""{green}[*] {loc_n}: {sversion}{white}""")
          # else:
          #   print(f'АКТУАльная версия - {name_file} - {sversion} - {nversion}')
        else:old(nversion_=nversion, sversion_= sversion, name_file_= name_file, name_d_ = name_d, redir_ = redir_cd,Th=Th_val ,loc_n_=loc_n)
      else:old(nversion_=nversion, sversion_= sversion, name_file_= name_file, name_d_ = name_d, redir_ = redir_cd,Th=Th_val ,loc_n_=loc_n)
    else:old(nversion_=nversion, sversion_= sversion, name_file_= name_file, name_d_ = name_d, redir_ = redir_cd,Th=Th_val ,loc_n_=loc_n)
  else:
    py_logger.warning(f"Version check failed. Cause: {err}")
    if print_val == True:print(f"""{red}[!] {loc['18']} Cause: {err}
{violet}[*] {loc_n}: {sversion}{white}""")


def check_all_relevant_version(loc_val, print_val=True):
    loc = loc_val
    main_version = 'https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/ver/version.json'
    data_version = 'https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/ver/random_neko_list_v.json'

    if print_val == True:
      ch_version(main_version,main_script_version, loc['25'],loc['9'],print_val)
      ch_version(data_version,random_neko_list_version(),loc['26'],loc['30'],print_val)
    
    if print_val == False:
      while True:
        ch_version(main_version,main_script_version, loc['25'],loc['9'],print_val)
        ch_version(data_version,random_neko_list_version(),loc['26'],loc['30'],print_val)
        time.sleep(10)





# <-------------------------->





# def remind():
#     # Спрашиваем текст напоминания, который нужно потом показать пользователю
#     print("О чём вам напомнить?")
#     # Ждём ответа пользователя и результат помещаем в строковую переменную text
#     text = str(input())
#     # Спрашиваем про время
#     print("Через сколько минут?")
#     # Тут будем хранить время, через которое нужно показать напоминание
#     local_time = float(input())
#     # Переводим минуты в секунды
#     local_time = local_time * 60
#     # Ждём нужное количество секунд, программа в это время ничего не делает
#     time.sleep(local_time)
#     # Показываем текст напоминания
#     print(text)


# <-------------------------->


def download_file_from_github(ind, file_name,redir=os.getcwd()):
  if ind == 0:
    url = f"https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/{file_name}"
  if ind == 1:
    url = f"https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/localization/{file_name}"
  local_filename = url.split("/")[-1]

  try:
    py_logger.info(f"[Downloading file] Name: {file_name}")
    orig = os.getcwd()
    os.chdir(redir)
    with requests.get(url, stream=True, allow_redirects=True) as r:
      r.raise_for_status()
      with open(local_filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
          f.write(chunk)
    os.chdir(orig)
    return "ok"

  except requests.exceptions.HTTPError as err:

    if "404" in str(err):
      return "errне найдено"
    return "err", err
  except Exception as err:
    return "err", err


def check(ind, file_name,redir_r):
  er = ""
  out = download_file_from_github(ind, file_name,redir=redir_r)
  if "err" in out:
    out = str(out).replace("err", "")
    er = er + f"{red}[-] DownloadingFileError ({out}): {file_name}{white}\n"
  print(er)


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
- 526 - Certificate blocking / ohm (rather different times, or parental control)
{white}{'='*10} OTHER: {'='*10}
{violet}- 101 - You are disconnected from the Internet.
- 102 - Error processing URL.{white}''',
  '1': 'Time',
  '2': 'Operating system',
  '3': 'Version',
  '4': 'You have the latest version of the script installed!',
  '5': 'Failed to get working directory.',
  '6':
  'Your OS is like Colab. All downloaded files will be downloaded to your Google Drive. Or rather, to the subfolder where this file is saved.',
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
  '17': 'Directory',
  '18': 'Update version check failed!',
  "19": "Reload script.",
  "20": "The text below triggers a script termination notification.",
  "21": "Script completed",
  "22": "Done!",
  "23": "Start an endless loop",
  "24": "Downloading additional data",
  "25": "Main Script Version",
  "26": "Data Baze Version",
  "27": "Not Found",
}

# <------------------------->

file_name_errors = "errors.json"
file_name_vk403 = "vk403.json"
file_name_err_info = "err_info.json"
file_name_config = "config.json"

# <------------------------->


def set_logger_settings():
  py_logger = logging.getLogger(__name__)
  py_logger.setLevel(logging.INFO)

  s = str(str((str(datetime.now())).split()[1]).split(".")[0]).split(":")[2]
  m = str(str((str(datetime.now())).split()[1]).split(".")[0]).split(":")[1]
  h = str(str((str(datetime.now())).split()[1]).split(".")[0]).split(":")[0]

  py_handler = logging.FileHandler(f"{s}-{m}-{h}.log", mode="w")
  # py_handler.setFormatter(logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s"))
  py_handler.setFormatter(
    logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
  py_logger.addHandler(py_handler)
  os.chdir(do)
  py_logger.info(
    f"{'='*15}- STARTing script in [{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}] -{'='*15}"
  )
  return py_logger


# <------------------------->


try:
  os.mkdir("logging")
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
  from win11toast import notify, update_progress, toast

  py_logger.info(f"Import module [win11toast] successfully.")
  val_toast = True
except:
  system("pip install win11toast")
  try:
    from win11toast import notify, update_progress, toast

    py_logger.info(
      f"[Import notify, update_progress, toast from win11toast] failed -> [Import notify, update_progress, toast from win11toast] successfully."
    )
    val_toast = True
  except ModuleNotFoundError:
    py_logger.error(
      "[Import notify, update_progress, toast from win11toast] failed.")
    val_toast = False

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
  system("pip install Pillow")
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
  system("pip install alive-progress")
  try:
    from alive_progress import alive_bar

    alive_a = True
    py_logger.info(
      f"[Import module from PIL] failed -> [Import module from PIL] successfully."
    )
  except ModuleNotFoundError:
    alive_a = False
    print(f"{red}[!] ModuleNotFoundError: alive_progress.{white}")
    py_logger.info(f"[Import alive_bar from alive_progress] failed.")


try:
  from random_neko_list import *
  from random_neko_list import version_data_baze as random_neko_list_version
  py_logger.info("The database has been successfully imported!")
except ModuleNotFoundError:
  try:
    from modules.random_neko_list import *
    from modules.random_neko_list import version_data_baze as random_neko_list_version
  except ModuleNotFoundError:
    py_logger.warning(f"Database not found! Trying to download database...")
    posle = os.getcwd()
    do_1212 = os.getcwd(
    ) + dir_pref + "modules" + dir_pref
    os.chdir(do_1212)
    download_file_from_github(0, "random_neko_list.py")
    os.chdir(posle)

    try:
      from modules.random_neko_list import *
      from modules.random_neko_list import version_data_baze as random_neko_list_version
      py_logger.info("The database has been successfully imported!")
    except ImportError:
      py_logger.critical(f"Database not found!")
      raise SystemExit(f'\n[!] {loc["8"]}')
  


# <-------------------------->

# Forced reboot


class ForcedRebootException(Exception):
  def __init__(self, *args):
    if args:self.message = args[0]
    else:self.message = None

  def __str__(self):
    if self.message:return self.message
    else:return "ForcedRebootException has been raised"
conf_file = []


def logo():
  try:
    from colorama import Fore
    colors = [
      Fore.RED,
      Fore.GREEN,
      Fore.YELLOW,
      Fore.BLUE,
      Fore.CYAN,
      Fore.MAGENTA,
      Fore.WHITE,
    ]
    py_logger.info(
      f"[Import module from PIL] successfully."
    )
  except:
    system("pip install colorama")
    try:
      from colorama import Fore
      colors = [
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.CYAN,
        Fore.MAGENTA,
        Fore.WHITE,
      ]
      py_logger.info(
      f"[Import module from PIL] failed -> [Import module from PIL] successfully."
    )
    except:
      print(f"{red}[!] ModuleImportError: colorama.{white}")
      colors = [red, green, yellow, blue, violet, turquoise, white]
      py_logger.info(f"[Import Fore from colorama] failed.")

  color1 = random.choice(colors)
  colors.remove(color1)
  color2 = random.choice(colors)
  print(f"""{color1}
{color2}▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
{color2}▐{color1}░░{color2}███{color1}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{color2}████{color1}░░░░░░░░░░░░░░░░░░░░░░░░░░{color2}▌
{color2}▐{color1}░{color2}█{color1}░░░{color2}█{color1}░░░░░░░░░░░░░░░░░░░░░{color2}█{color1}░░░░░░░░░░{color2}█{color1}░░░░{color2}█{color1}░░░░░░░░░░░░░░░░░░░░░░░░░{color2}▌
{color2}▐{color1}░{color2}█{color1}░░░░{color2}█{color1}░░░░░░░░░░░░░░░░░░░░{color2}█{color1}░░░░░░░░░░{color2}█{color1}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{color2}▌
{color2}▐{color1}░{color2}█{color1}░░░░{color2}█{color1}░░░{color2}███{color1}░░░{color2}███{color1}░░░░{color2}████{color1}░░░░░░░░░░░{color2}█{color1}░░░░░░░{color2}█{color1}░{color2}███{color1}░░░░{color2}████{color1}░░░░{color2}████{color1}░░{color2}▌
{color2}▐{color1}░{color2}█{color1}░░░░{color2}█{color1}░░{color2}█{color1}░░{color2}█{color1}░░░{color2}█{color1}░░{color2}█{color1}░░{color2}█{color1}░░░{color2}█{color1}░░░░░░░░░░░{color2}█{color1}░░░░░░░{color2}██{color1}░░░{color2}█{color1}░░{color2}█{color1}░░░░{color2}█{color1}░░{color2}█{color1}░░░░{color2}█{color1}░{color2}▌
{color2}▐{color1}░{color2}█{color1}░░░{color2}█{color1}░░░{color2}█{color1}░░{color2}█{color1}░░░{color2}█{color1}░░{color2}█{color1}░░{color2}█{color1}░░░{color2}█{color1}░░░░░░░░░░░{color2}█{color1}░░░░{color2}█{color1}░░{color2}█{color1}░░░░░░░{color2}█{color1}░░░░{color2}█{color1}░░{color2}█{color1}░░░░{color2}█{color1}░{color2}▌
{color2}▐{color1}░{color2}████{color1}░░░░░{color2}██{color1}░{color2}█{color1}░░{color2}█{color1}░░{color2}█{color1}░░░{color2}███{color1}░{color2}█{color1}░░{color2}█████{color1}░░░░{color2}████{color1}░░░{color2}█{color1}░░░░░░░░{color2}████{color1}░░░{color2}█████{color1}░░{color2}▌
{color2}▐{color1}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{color2}█{color1}░░░░░░{color2}▌
{color2}▐{color1}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{color2}█{color1}░░░░░░{color2}▌
{color2}▐{color1}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{color2}▌
{color2}▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌{white}"""
        )










try:
  with open(f"{file_name_config}", "r") as file:
    data = json.loads(file.read())
    localization = data[0]['localization']
except Exception as err:
  cls()
  localization = input(
    f"Выберите локализацию (ru) / Select localization (en) >>> ").upper()


  if (localization != "RU"):
    if (localization != "EN"):
      localization = "EN"

  zn = str(localization).lower().replace(" ", "")
  conf_file.append({'localization': zn})



cls()

localization_val = localization.upper()
py_logger.info(f"Localization: {localization_val}")
if localization_val == "RU":
  try:
    from localization.RU import ru_loc as loc
    py_logger.info(f"Localization for the Russian language was  found!")
  except ModuleNotFoundError:
    py_logger.warning(f"Localization for the Russian language was NOT found!")
    loc = en_loc_reserve

if localization_val == "EN":
    loc = en_loc_reserve

logo()



th = Thread(target=check_all_relevant_version, args=(loc,False))
th.start()


try:
  do = os.getcwd()
except OSError:
  py_logger.critical(f"Unable to get a working directory.")
  raise OSError(f'{red}[!] {loc["7"]}')

if "/content" in os.getcwd():
  py_logger.info(f"Colab platform found.")
  try:
    system(
      "!mkdir data && wget https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/setup.py"
    )
  except:
    pass
  print(f"""{white}{'='*15}- {red}WARNING!{white} -{'='*15}""")
  print(f'{red} {loc["6"]} {white}')

  from google.colab import drive

  try:
    print(f"""{white}{'='*15}- {green}Connecting...{white} -{'='*15}""")
    drive.mount("/content/MyDrive", force_remount=True)
    py_logger.critical(f"Connect to Google Collab - OK")
  except:
    print(f"""{white}{'='*15}- {red}Connecting Failed...{white} -{'='*15}""")
    py_logger.critical(f"Unable to connect to Google Collab")
    raise SystemError(f"{red}[!] Error to connecting to drive...{white}")
  print(f"""{white}{'='*15}- {green}Connecting OK...{white} -{'='*15}""")


  try:
    per1 = os.getcwd()
    os.chdir("/content/MyDrive/MyDrive/Colab Notebooks")
    per2 = os.getcwd()
    py_logger.info(f"[Directory change] {per1} -> {per2}")
  except OSError as err:
    raise OSError(f'{red}[!] {loc["7"]}')
  try:
    os.mkdir("Dand_Crop")
  except FileExistsError:
    pass
  os.chdir(os.getcwd() + "/" + "Dand_Crop")

  system('!touch "/content/MyDrive/Colab Notebooks/setup.py"')



# <------------------------->

# def update():
#   file_names = ["random_neko_list.py", "main.py"]
#   for file_name in file_names:
#     check(0, file_name)
#   import time

#   time.sleep(2)


print(f"""{'='*15}- {loc['1']} -{'='*15}{turquoise}
{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}{white}""")


check_all_relevant_version(loc,True)


print(f"""{'='*15}- {loc['2']} -{'='*15}
{yellow}[*] OS Name: {os.name.upper()}{white}""")

py_logger.info(f"""{'='*15}- OS -{'='*15}""")
py_logger.info(f"""[*] OS Name: {os.name.upper()}""")



print(f"""{'='*15}- {loc['3']} -{'='*15}""")

# <------------------------->




#def check_version(sversion):
#  try:
#    nversion = json.loads(
#      requests.get(
#        "https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/ver/version.json"
#      ).text)["ver"]
#  except:
#    nversion = None
#
#  if nversion != None:
#    s1, s2, s3, n1, n2, n3 = (
#      str(sversion).split(".")[0],
#      str(sversion).split(".")[1],
#      str(sversion).split(".")[2],
#      str(nversion).split(".")[0],
#      str(nversion).split(".")[1],
#      str(nversion).split(".")[2],
#    )
#    if s1 >= n1:
#      if s2 >= n2:
#        if s3 >= n3:
#          py_logger.info(
#            f"The current version of the script has been found ({main_script_version})!"
#          )
#
#          print(f"""{green}[*] {loc["25"]}: {main_script_version}{white}""")
#
#        else:
#          old(nversion)
#      else:
#        old(nversion)
#    else:
#      old(nversion)
#  else:
#    py_logger.warning(f"Version check failed.")
#    print(f"""{red}[!] {loc['18']}
#{violet}[*] {loc["25"]}: {main_script_version}{white}""")

# <------------------------->

#check_version(main_script_version)
#data_version = random_neko_list_version()
#print(f"""{green}[*] {loc["26"]}: {data_version}{white}""")

# <------------------------->

one_path = os.getcwd()
ext_list = list()

print(f"{loc['0']}")
print(f'''{white} {'='*15} Выберите скачиваемую библиотеку {'='*15}''')

# <------------------------->


chdir = input(f'''{red}[!]{yellow} Скачивание какой библиотеки вы бы хотели совершить?
{turquoise}[1] IMGS
[2] IMGS18 (18+)
[3] Своя
{blue}>>> ''')
              
while chdir != '1' or chdir != '2':
    #print(chdir)
    if chdir == '1':
        chosing_directory = imgs
        name_dir = 'DataDir'
        print(f'{yellow}[!] Была выбрана {green}обычная{yellow} библиотека...')
        break

    elif chdir == '2':
        chosing_directory = imgs18
        name_dir = 'DataDir18'
        print(f'{yellow}[!] Была выбрана {red}18+{yellow} библиотека...')
        break

    elif chdir == '3':
        print(f'{red}[!] Данная фукция находится в разработке... Была выбрана {green}обычная {red}библиотека.{white}')
        chosing_directory = imgs
        name_dir = 'DataDir'
        time.sleep(3)
        break    
    else:
        chdir = input(f'''{red}>>> ''')


# <------------------------->

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
  name_dir = ""
  pass

py_logger.info(f"Dir_pref = {dir_pref}")
download_to = os.getcwd() + dir_pref + str(name_dir)
print(f"""{white}{'='*15}- {loc['17']} -{'='*15}
{green}[*] {loc["12"]}: {os.getcwd()}
[*] {loc["13"]} :      {download_to}""")

py_logger.info(f"""{'='*15}- PATH -{'='*15}""")
py_logger.info(f"[*] Working Directory: {os.getcwd()}")
py_logger.info(
  f"""[*] Download in:      {os.getcwd() + dir_pref +str(name_dir)}""")

pythonanywhere_key = False


# chosing_directory = ['lol']
try:
  from modules.exctensions_module import sizing_dict

  dict_size = sizing_dict(chosing_directory)
except:
  dict_size = None
  pass

_200 = []

_400 = []
_401 = []
_402 = []
_403 = []
_404 = []

_522 = []
_524 = []
_526 = []

_000 = []
_101 = []
_102 = []
_unc = []


def download_function(url, name_file, err_dict, err_info, vk_403_err,
                      pythonanywhere_key):
  if pythonanywhere_key == True:
    pass
  else:
    if 'imgs' in url:
      pythonanywhere_key = False

    if 'imgs18' in url:
      pythonanywhere_key = True

  url = url.replace(" ", "%20")

  if "?size=" in url:
    ind = url.find("?size=")
  else:
    if "?extra=" in url:
      ind = url.find("?extra=")
    else:
      ind = len(url)

  print('\r', end='')

  try:
    urllib.request.urlretrieve(str(url), name_file)

    print(f"{green}[+] 200: {blue}{name_file}{white}  URL: {url[0:ind]}")
    py_logger.info(
      f"""File with name {name_file} and link ({url}) was downloaded successfully."""
    )
    status = '200'

  except HTTPError as err_code:

    print(
      f"{red}[-] {red}{err_code.code}: {blue}{name_file}{white}  URL: {url[0:ind]}"
    )
    err_dict.append(f"{url}")
    err_info.append({f"{name_file}": f"{err_code.code}"})
    if "userapi.com" in url and err_code.code == 403:
      vk_403_err.append(f"{url}")
    py_logger.warning(
      f"""File named {name_file} and link ({url}) was NOT downloaded and returned code: {err_code.code}"""
    )
    status = f'{err_code.code}'

  except urllib.error.URLError as err_code:
    err_dict.append(f"{url}")
    if "[WinError 10054]" in str(err_code):
      print(f"{red}[-] {red}522: {blue}{name_file}{white}  URL: {url[0:ind]}")
      py_logger.warning(
        f"""File with name {name_file} and link ({url}) was NOT downloaded due to lack of server response."""
      )
      err_info.append({f"{name_file}": "522"})
      status = f'522'

    if "[Errno 99]" in str(err_code):
      print(f"{red}[-] {red}524: {blue}{name_file}{white}  URL: {url[0:ind]}")
      err_info.append({f"{name_file}": "524"})
      py_logger.warning(
        f"""File with name {name_file} and link ({url}) was NOT downloaded due to connection failure."""
      )
      status = f'524'

    if "[SSL: WRONG_VERSION_NUMBER]" in str(err_code):
      print(f"{red}[-] {red}526: {blue}{name_file}{white}  URL: {url[0:ind]}")
      err_info.append({f"{name_file}": "526"})
      py_logger.warning(
        f"""The file with name {name_file} and link ({url}) was NOT downloaded due to mismatch of security certificate or parental controls."""
      )
      status = f'526'

    if "[Errno 11001]" in str(err_code):
      print(f"{red}[-] {red}101: {blue}{name_file}{white}  URL: {url[0:ind]}")
      err_info.append({f"{name_file}": "101"})
      py_logger.warning(
        f"""The file with name {name_file} and link ({url}) was NOT downloaded due not connected to Enternet."""
      )
      status = f'101'

    else:
      #print(err_code)
      print(f"{violet}[?] ___: {blue}{name_file}{white}  URL: {url[0:ind]}")
      err_info.append({f"{name_file}": f"{err}"})
      py_logger.warning(
        f"""File with name {name_file} and link ({url}) was NOT loaded due to unknown error: {err}."""
      )
      status = f'___'

  except http.client.RemoteDisconnected:
    print(
      f"{violet}[-] {violet}101: {blue}{name_file}{white}  URL: {url[0:ind]}")
    err_info.append({f"{name_file}": "101"})
    py_logger.warning(
      f"""The file with the name {name_file} and link ({url}) was NOT downloaded due to the user disconnecting from the Internet."""
    )
    status = f'101'

  except ConnectionResetError:
    print(
      f"{violet}[-] {violet}101: {blue}{name_file}{white}  URL: {url[0:ind]}")
    err_info.append({f"{name_file}": "101"})
    py_logger.warning(
      f"""The file with the name {name_file} and link ({url}) was NOT downloaded due to the user disconnecting from the Internet."""
    )
    status = f'101'

  except ValueError as err:
    print(f"{violet}[?] 102: {blue}{name_file}{white}  URL: {url[0:ind]}")
    err_info.append({f"{name_file}": f"{err}"})
    py_logger.warning(
      f"""File with name {name_file} and link ({url}) was NOT downloaded due to unformatted link."""
    )
    status = f'102'

  except Exception as err:
    print(f"{violet}[?] ___: {blue}{name_file}{white}  URL: {url[0:ind]}")
    err_info.append({f"{name_file}": f"{err}"})
    py_logger.warning(
      f"""File with name {name_file} and link ({url}) was NOT loaded due to unknown error: {err}."""
    )
    status = f'___'

  return status, err_dict, err_info, vk_403_err, pythonanywhere_key


startTime = time.time()


def main(pythonanywhere_key):
  if dict_size == None:
    ur = chosing_directory
  else:
    ur = dict_size

  if val_toast == True:
    err_name_file = 'НЕ НАЙДЕНО'
    notify(
      progress={
        'title': f'Последняя ошибка: {err_name_file}',
        'status': f'Downloading...',
        'value': '0',
        'valueStringOverride': f'0/{len(ur)} objects.'
      })
  else:
    err_name_file = 'ERROR'
    pass

  print(f"""{white}{'='*15}- {loc['14']} - {len(ur)} -{'='*15}""")

  py_logger.info(f"""{'='*15}- Downloading Info -{'='*15}""")
  py_logger.info(f"""LEN objects - {len(ur)}""")

  err_dict = []
  vk_403_err = []
  err_info = []

  def download(err_name_file, pythonanywhere_key):
    i = 0

    if alive_a == True:
      with alive_bar(len(ur)) as bar:

        for zn in ur:
          try:
            url = list(zn.keys())[0]
            exten = zn[f"{list(zn.keys())[0]}"]
          except AttributeError:
            url = zn
            if "mp4" in url:
              exten = f".mp4"
            else:
              if "gif" in url:
                exten = f".gif"
              else:
                if "jpg" in url:
                  exten = f".jpg"
                else:
                  if "webp" in url:
                    exten = f".webp"
                  else:
                    if "webm" in url:
                      exten = f".webm"
                    else:
                      exten = f".png"

          def ww1(i, url, err_dict, err_info, vk_403_err, exten, err_name_file,pythonanywhere_key):
            name_file = f"{i}{exten}"

            if val_toast == True:update_progress({'value': f'{i}/{len(ur)}','valueStringOverride': f'{i}/{len(ur)} objects','title': f'Последняя ошибка: {err_name_file}'})


            while not os.path.exists(name_file):
              try:
                status, err_dict, err_info, vk_403_err, pythonanywhere_key = (
                  download_function(url, name_file, err_dict, err_info,
                                    vk_403_err, pythonanywhere_key))

                if status == '200':
                  _200.append({f'{name_file}': f'{url}'})
                elif status == '000':
                  _000.append({f'{name_file}': f'{url}'})
                elif status == '101':
                  _101.append({f'{name_file}': f'{url}'})
                elif status == '102':
                  _102.append({f'{name_file}': f'{url}'})
                elif status == '400':
                  _400.append({f'{name_file}': f'{url}'})
                elif status == '401':
                  _401.append({f'{name_file}': f'{url}'})
                elif status == '402':
                  _102.append({f'{name_file}': f'{url}'})
                elif status == '403':
                  _403.append({f'{name_file}': f'{url}'})
                elif status == '404':
                  _404.append({f'{name_file}': f'{url}'})
                elif status == '522':
                  _522.append({f'{name_file}': f'{url}'})
                elif status == '524':
                  _524.append({f'{name_file}': f'{url}'})
                elif status == '526':
                  _526.append({f'{name_file}': f'{url}'})
                elif status == '___':
                  _unc.append({f'{name_file}': f'{url}'})
                else:
                  pass

                if status != "200":
                  err_name_file = name_file
                  break
                else:
                  pass
                if val_toast == True:update_progress({'title': f'Последняя ошибка: {err_name_file}'})
              except Exception:
                break

            try:
              if url not in err_dict:
                src = one_path + dir_pref + name_file
                os.chdir(one_path)
                dest = f"{os.getcwd()}{dir_pref}{name_dir}{dir_pref}{name_file}"
                try:
                  os.rename(src, dest)
                except FileExistsError:
                  os.chdir(f"{os.getcwd()}{dir_pref}{name_dir}{dir_pref}")
                  os.remove(name_file)
                  os.chdir(one_path)
                  os.rename(src, dest)

              else:
                pass

            except FileNotFoundError:
              pass
            except:
              pass

            bar()
            return err_name_file, pythonanywhere_key

          err_d, pythonanywhere_key = ww1(i, url, err_dict, err_info,
                                          vk_403_err, exten, err_name_file,
                                          pythonanywhere_key)
          err_name_file = err_d
          i = i + 1

    if alive_a == False:

      for zn in ur:
        try:
          url = list(zn.keys())[0]
          exten = zn[f"{list(zn.keys())[0]}"]
        except AttributeError:
          url = zn
          if "mp4" in url:
            exten = f".mp4"
          else:
            if "gif" in url:
              exten = f".gif"
            else:
              if "jpg" in url:
                exten = f".jpg"
              else:
                if "webp" in url:
                  exten = f".webp"
                else:
                  if "webm" in url:
                    exten = f".webm"
                  else:
                    exten = f".png"

        def ww2(i, url, err_dict, err_info, vk_403_err, exten):
          name_file = f"{i}{exten}"
          if val_toast == True:update_progress({'value': f'{i}/{len(ur)}','valueStringOverride': f'{i}/{len(ur)} videos'})


          while not os.path.exists(name_file):
            try:
              status, err_dict, err_info, vk_403_err = download_function(
                url, name_file, err_dict, err_info, vk_403_err)

              if status == '200':
                _200.append({f'{name_file}': f'{url}'})
              elif status == '101':
                _101.append({f'{name_file}': f'{url}'})
              elif status == '102':
                _102.append({f'{name_file}': f'{url}'})
              elif status == '400':
                _400.append({f'{name_file}': f'{url}'})
              elif status == '401':
                _401.append({f'{name_file}': f'{url}'})
              elif status == '402':
                _102.append({f'{name_file}': f'{url}'})
              elif status == '403':
                _403.append({f'{name_file}': f'{url}'})
              elif status == '404':
                _404.append({f'{name_file}': f'{url}'})
              elif status == '522':
                _522.append({f'{name_file}': f'{url}'})
              elif status == '524':
                _524.append({f'{name_file}': f'{url}'})
              elif status == '526':
                _526.append({f'{name_file}': f'{url}'})
              elif status == '___':
                _unc.append({f'{name_file}': f'{url}'})
              else:
                _unc.append({f'{name_file}': f'{url}'})
                pass

              if status != "200":
                break
              else:
                pass
              if val_toast == True:update_progress({'title': f'Последняя ошибка: {err_name_file}'})
            except:
              break

          try:
            if url not in err_dict:
              src = one_path + dir_pref + name_file
              os.chdir(one_path)
              dest = f"{os.getcwd()}{dir_pref}{name_dir}{dir_pref}{name_file}"
              try:
                os.rename(src, dest)
              except FileExistsError:
                os.chdir(f"{os.getcwd()}{dir_pref}{name_dir}{dir_pref}")
                os.remove(name_file)
                os.chdir(one_path)
                os.rename(src, dest)
              except FileNotFoundError:
                pass
          except:
            pass
          # bar()

        ww2(i, url, err_dict, err_info, vk_403_err, exten)
        i = i + 1

    if len(_000) != 0:
      ext_list.append({f'000': _000})
    if len(_101) != 0:
      ext_list.append({f'101': _101})
    if len(_102) != 0:
      ext_list.append({f'102': _102})
    if len(_200) != 0:
      ext_list.append({f'200': _200})
    if len(_400) != 0:
      ext_list.append({f'400': _400})
    if len(_401) != 0:
      ext_list.append({f'401': _401})
    if len(_402) != 0:
      ext_list.append({f'402': _402})
    if len(_403) != 0:
      ext_list.append({f'403': _403})
    if len(_404) != 0:
      ext_list.append({f'404': _404})
    if len(_522) != 0:
      ext_list.append({f'522': _522})
    if len(_524) != 0:
      ext_list.append({f'524': _524})
    if len(_526) != 0:
      ext_list.append({f'526': _526})
    if len(_unc) != 0:
      ext_list.append({f'UNC': _unc})

    return pythonanywhere_key

  pythonanywhere_key = download(err_name_file, pythonanywhere_key)
  return err_dict, vk_403_err, err_info, pythonanywhere_key


try:
  err_count, vk_403_err, err_info, pythonanywhere_key = main(
    pythonanywhere_key)
  if pythonanywhere_key == True:
    py_logger.info(f"""pythonanywhere_def = True""")
    if (input(f"{loc['29']}? (Y/N) >>> ") == "Y"):
      try:
        from modules.pythonanywhere import pythonanywhere_def
        os.chdir(download_to)
        print(f'''{'='*15}- {loc['24']} -{'='*15}''')
        pythonanywhere_def(py_logger)
        os.chdir(posle)
      except ModuleNotFoundError as err:
        py_logger.critical(f"""pythonanywhere_def not found ({err}).""")
      except Exception as err:
        py_logger.critical(f"""pythonanywhere_def = Error  ({err}).""")
  else:
    py_logger.info(f"""pythonanywhere_def = False""")

  py_logger.info(f"""{'='*15}- Downloading OK -{'='*15}""")
except KeyboardInterrupt:
  py_logger.info(f"""{'='*15}- Downloading KeyboardInterrupt -{'='*15}""")
  py_logger.critical(f"""The user aborted code execution.""")
  print(f'{red}[!] {loc["15"]}...')

endTime = time.time()

print(
  f"{loc['28']}: {str(timedelta(seconds = (endTime - startTime))).split('.')[0]}"
)

try:
  if len(err_count) != 0:
    with open(f"{file_name_errors}", "w") as outfile:
      json.dump(err_count, outfile, indent=4)
    py_logger.info(f"""File created [{file_name_errors}]""")

  if len(vk_403_err) != 0:
    with open(f"{file_name_vk403}", "w") as outfile:
      json.dump(vk_403_err, outfile, indent=4)
    py_logger.info(f"""File created [{file_name_vk403}]""")

  if len(err_info) != 0:
    with open(f"{file_name_err_info}", "w") as outfile:
      json.dump(err_info, outfile, indent=4)
    py_logger.info(f"""File created [{file_name_err_info}]""")

  if len(ext_list) != 0:
    with open('info.json', 'w') as file:
      json.dump(ext_list, file, indent=4)
    py_logger.info(f"""File created [info.json]""")

except NameError:
  pass

with open(f"{file_name_config}", "w") as outfile:
  json.dump(conf_file, outfile, indent=4)
  py_logger.info(f"""File created [{file_name_config}]""")

py_logger.info(f"""The database download was completed in [{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]""")

try:
  from module_res_def import res_def
  ch = input(f'\n{red}[!] {loc["16"]} (Y/n) >>> {white}')
  py_logger.info(
    f"""The meaning of calling the image processing function:  {ch}.""")
  if ch == "Y": res_def(name_dir)
  else: pass
except KeyboardInterrupt:
  py_logger.info(
    f"""The user has canceled an image encoding call request (KeyboardInterrupt)."""
  )
except Exception as err:
  py_logger.info(
    f"""The script has canceled an image encoding call request ({err}).""")

if val_toast == True:
  print(f'{blue}[.] {loc["20"]}{white}')
  toast(f'{loc["22"]}',
        f'{loc["21"]}...',
        buttons=[{
          'activationType': 'protocol',
          'arguments': f'file:///{download_to}',
          'content': 'Open Folder'
        }])
else:
  pass

if (input(f"{loc['22']}... {loc['23']}? (Y/N) >>> ") == "Y"):
  while True:
    cls()
    main()
else:
  pass

  #sleep(30)
