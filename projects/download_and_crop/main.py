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

main_script_version = "2.2.4"

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

working_directory = os.getcwd()

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
import socket

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
debugVal = False

# <-------------------------->


def old_Thread(nversion,sversion, name_file,name_d,loc_n,redir=os.getcwd()):
  if val_toast == True:
    if name_file == 'version.json':
       loc_n = loc['9']
    else:
      loc_n = loc['30']
    tit = f'{loc_n}\n{sversion} --> {nversion}'
    toast(
          title = tit,
          image='https://opengraph.githubassets.com/2fb38cef00042d8b977103470ef6e7943a6229e01819c4f2b6a39ca8aba155e1/Basefilespython/pydiscbot',
          icon = 'https://avatars.githubusercontent.com/u/123670499?v=4',
          buttons=[{'activationType': 'protocol','arguments': 'https://github.com/Basefilespython/pydiscbot/tree/main/projects/download_and_crop/setup','content': 'Download'}],
          
          )

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
      val = True
      raise ForcedRebootException(loc["19"])
    else:
      pass
  
  if Th == True:
    old_Thread(nversion_,sversion_, name_file_, name_d_, loc_n_, redir=os.getcwd())





def ch_version(url,sversion,loc_n,name_d,print_val):
  
  name_file = url.split('/')[-1]
  if name_file != 'version.json':
    redir_cd = os.getcwd() + dir_pref + 'modules'
  else:
    redir_cd = os.getcwd()
  

  errs = ''
  try:
    try:
      nversion = json.loads(requests.get(url).text)["ver"]
    except requests.exceptions.ConnectionError as err_code:
      if "[Errno 11001]" in str(err_code):
        errs = 'You are not connected to the Internet'
      nversion = None
    except Exception as err:
      errs = err
      nversion = None
  except NameError:
    print(pip_not_installed())
    try:
      nversion = json.loads(requests.get(url).text)["ver"]
    except requests.exceptions.ConnectionError as err_code:
      if "[Errno 11001]" in str(err_code):
        errs = 'You are not connected to the Internet'
      nversion = None
    except Exception as err:
      errs = err
      nversion = None

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
        else:old(nversion_=nversion, sversion_= sversion, name_file_= name_file, name_d_ = name_d, redir_ = redir_cd,Th=Th_val ,loc_n_=loc_n)
      else:old(nversion_=nversion, sversion_= sversion, name_file_= name_file, name_d_ = name_d, redir_ = redir_cd,Th=Th_val ,loc_n_=loc_n)
    else:old(nversion_=nversion, sversion_= sversion, name_file_= name_file, name_d_ = name_d, redir_ = redir_cd,Th=Th_val ,loc_n_=loc_n)
  else:
    py_logger.warning(f"Version check failed. Cause: {errs}") 
    lens_simvolov = len(list(f'[*] {loc_n}: {sversion}'))
    if print_val == True:print(f"""{violet}[*] {loc_n}: {sversion}{' '*(38-lens_simvolov)}{red}[!] Cause: {errs}{white}""")
      

val = False

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
        if val == True:
          break


def check_internet():
  host = 'www.google.com'
  def is_connected(host):
      try:
          host = socket.gethostbyname(host)
          socket.create_connection((host, 80), 2)
          return True
      except Exception:
          return False
      
  if is_connected(host) == True:
      pass
  else:
      print('\r', end='')
      print(f"{red}Подключитесь к Интернету!{white}")
      while is_connected(host) == False:
          pass



# <-------------------------->


def download_file_from_github(ind, file_name,redir=os.getcwd()):
  if ind == 0:
    url = f"https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/{file_name}"
  if ind == 1:
    url = f"https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/localization/{file_name}"
  local_filename = url.split("/")[-1]

  try:
    if redir != os.getcwd():py_logger.info(f"[Downloading file] Name: {file_name} [REDIRECT]: {redir}")
    else:py_logger.info(f"[Downloading file] Name: {file_name}")
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


def debDEF(text, debugVal, py_logger, py_log_num, exc_info=False):
  if debugVal == True:
    print('\r', end='')
    print(f'{yellow}[DEBUG] {blue}{text}{white}')

  if py_log_num == 1:py_logger.info(text)
  elif py_log_num == 2:py_logger.warning(text)
  elif py_log_num == 3:py_logger.error(text)
  elif py_log_num == 4:py_logger.critical(text)
  else: py_logger.debug(text)








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
{white}{'='*10} TIMEOUT ERROR CODEs: {'='*10}{red}
- 522 - The connection is not responding (maybe ILV blocked).
- 524 - TCP connection failed. (internal OS errors).
- 526 - Certificate blocking / ohm (rather different times, or parental control)
{white}{'='*10} OTHER: {'='*10}
{violet}- 101 - You are disconnected from the Internet.
- 102 - Error processing URL.
- 103 - File download broken.{white}''',
"1": 'Time',
"2": "Operating system",
"3": "Version",
"4": "You have the latest version of the script installed!",
"5": "Unable to get working directory.",
"6": "Your OS is similar to Colab. All uploaded files will be uploaded to your Google Drive. Or rather, to the subfolder where this file is saved.",
"7": "RESTART THE SKIP RUNNING ENVIRONMENT.",
"8": "Base not found!",
"9": "You have an outdated version of the script installed!",
"10": "Install new version?",
"11": "Version check failed!",
"12": "Working directory",
"13": "Upload to",
"14": "Number of images",
"15": "You aborted code execution",
"16": "Crop images in database?",
"17": "Directory",
"18": "Update version check failed!",
"19": "Reload script.",
"20": "The text below triggers a script termination notification.",
"21": "Script completed",
"22": "Done!",
"23": "Start an endless loop",
"24": "Download additional data",
"25": "Main script version",
"26": "Database version",
"27": "Not found",
"28": "Script execution time",
"29": "Start downloading additional data",
"30": "You have an outdated version of the database installed!",
"31": "Old software version"
}



def pip_not_installed():
  import os
  os.system('python3 get-pip.py')
  return 'OKEY NAXYI'







# <------------------------->

file_name_errors = "errors.json"
file_name_site = "vk403.json"
file_name_err_info = "err_info.json"
file_name_config = "config.json"

# <------------------------->

starting_script_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
starting_script_time2 = starting_script_time.replace('-','_').replace(' ','_').replace(':','_')

def set_logger_settings():
  py_logger = logging.getLogger(__name__)
  py_logger.setLevel(logging.INFO)

  s = str(str((str(datetime.now())).split()[1]).split(".")[0]).split(":")[2]
  m = str(str((str(datetime.now())).split()[1]).split(".")[0]).split(":")[1]
  h = str(str((str(datetime.now())).split()[1]).split(".")[0]).split(":")[0]

  py_handler = logging.FileHandler(f"{starting_script_time2}.log", mode="w")
  # py_handler.setFormatter(logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s"))
  py_handler.setFormatter(
    logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
  py_logger.addHandler(py_handler)
  os.chdir(do)
  starting_script_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
  debDEF(f"{'='*15}- STARTing script in [{starting_script_time}] -{'='*15}", debugVal, py_logger, 1)

  return py_logger,starting_script_time


# <------------------------->

for name in ['localization','modules','Statistics']:
    if not os.path.exists(name):
      os.mkdir(name)






try:
  os.mkdir("logging")
  os.chdir(f'{do + dir_pref + "logging"}')
  py_logger, starting_script_time = set_logger_settings()
except FileExistsError:
  os.chdir(f'{do + dir_pref + "logging"}')
  py_logger, starting_script_time = set_logger_settings()
  pass
except PermissionError:
  py_logger, starting_script_time = set_logger_settings()
  pass







try:
  import requests
  debDEF(f"Import module [requests] successfully.", debugVal, py_logger, 1)

except:
  system("pip install requests")
  try:
    import requests
    debDEF(f"Import module [requests] failed -> Import module [requests] successfully.", debugVal, py_logger, 1)
  except ModuleNotFoundError:
    debDEF("Import module [requests] failed.", debugVal, py_logger, 3)


debDEF(f"""{'='*15}- LOCALIZATION -{'='*15}""", debugVal, py_logger, 1)


try:
  with open(f"{file_name_config}", "r") as file:
    data = json.loads(file.read())
    localization = data[0]['localization']
except:
  if debugVal == False:cls()

  localization = input(
    f"Выберите локализацию (ru) / Select localization (en) >>> ").upper()


  if (localization != "RU"):
    if (localization != "EN"):
      localization = "EN"
  conf_file = []
  zn = str(localization).lower().replace(" ", "")
  conf_file.append({'localization': zn})
  with open(f"{file_name_config}", "w") as outfile:
    json.dump(conf_file, outfile, indent=4)
    debDEF(f"""File created [{file_name_config}]""", debugVal, py_logger, 1)
    # py_logger.info(f"""File created [{file_name_config}]""")

localization_val = localization.upper()
debDEF(f"Localization: {localization_val}", debugVal, py_logger, 1)

if localization_val == "RU":
  try:
    from localization.RU import ru_loc as loc
    debDEF(f"Localization for the Russian language was  found!", debugVal, py_logger, 1)

  except ModuleNotFoundError as err:
    debDEF(err, debugVal, py_logger, 3)
    debDEF(f"Localization for the Russian language was NOT found!", debugVal, py_logger, 2)




    do_1212 = os.getcwd() + dir_pref + "localization"
    os.chdir(do_1212)
    check(1, 'RU.py', do_1212)
    os.chdir(working_directory)
    try:
      from localization.RU import ru_loc as loc
      debDEF(f"Localization for the Russian language was  found!", debugVal, py_logger, 1)

    except:
      loc = en_loc_reserve
      
if localization_val == "EN":loc = en_loc_reserve


debDEF(f"""{'='*15}- Modules -{'='*15}""", debugVal, py_logger, 1)


if str(os.name) == "nt":
  try:
    from win11toast import notify, update_progress, toast
    debDEF(f"Import module [win11toast] successfully.", debugVal, py_logger, 1)
    val_toast = True
  except:
    system("pip install win11toast")
    try:
      from win11toast import notify, update_progress, toast
      debDEF(f"[Import notify, update_progress, toast from win11toast] failed -> [Import notify, update_progress, toast from win11toast] successfully.", debugVal, py_logger, 1)
      val_toast = True
    except ModuleNotFoundError:
      debDEF("[Import notify, update_progress, toast from win11toast] failed.", debugVal, py_logger, 3)
      val_toast = False
else:
  debDEF("[Import notify, update_progress, toast from win11toast] failed. (NOT WIN)", debugVal, py_logger, 3)
  val_toast = False


try:
  from tqdm import tqdm
  debDEF(f"[Import tqdm from tqdm] successfully.", debugVal, py_logger, 1)
except:
  system("pip install tqdm")
  try:
    from tqdm import tqdm

    debDEF(f"Import module [tqdm] failed -> Import module [tqdm] successfully.", debugVal, py_logger, 1)
  except ModuleNotFoundError:
    debDEF("Import module [tqdm] failed.", debugVal, py_logger, 3)




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
    from colorama import Fore
    colors = [Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.BLUE,Fore.CYAN,Fore.MAGENTA,Fore.WHITE]
    py_logger.info(f"[Import module from PIL] successfully.")
except:
    system("pip install colorama")
    try:
      from colorama import Fore
      colors = [Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.BLUE,Fore.CYAN,Fore.MAGENTA,Fore.WHITE]
      py_logger.info(f"[Import module from PIL] failed -> [Import module from PIL] successfully.")
    except:
      print(f"{red}[!] ModuleImportError: colorama.{white}")
      colors = [red, green, yellow, blue, violet, turquoise, white]
      py_logger.info(f"[Import Fore from colorama] failed.")

py_logger.info(f"{'='*15}- Script Components -{'='*15}")


try:
  from random_neko_list import *
  from random_neko_list import version_data_baze as random_neko_list_version
  py_logger.info("The database has been successfully imported!")
except ModuleNotFoundError:
  #Installed folder (modules) not found. Trying to create a folder...

  if not os.path.exists('modules'):
      py_logger.warning('Installed folder (modules) not found. Trying to create a folder...')
      try:
        os.mkdir("modules")
        py_logger.info('Folder creation (modules) completed successfully.')
      except FileExistsError:
        py_logger.warning('Installed folder (modules) was found. Finding an error.')
        pass
      except PermissionError:
        py_logger.error('An attempt to create a folder failed due to lack of permissions.')
        pass

  else:
        py_logger.warning('Installed folder (modules) was found. Finding an error.')


  try:
    from modules.random_neko_list import *
    from modules.random_neko_list import version_data_baze as random_neko_list_version
  except ModuleNotFoundError:


    debDEF(f"Database not found! Trying to download database...", debugVal, py_logger, 2)
    do_1212 = os.getcwd() + dir_pref + "modules"
    os.chdir(do_1212)
    check(0, "random_neko_list.py", do_1212)
    os.chdir(working_directory)

    try:
      from modules.random_neko_list import *
      from modules.random_neko_list import version_data_baze as random_neko_list_version

      debDEF("The database has been successfully imported!", debugVal, py_logger, 1)
    except ImportError:
      debDEF(f"Database not found!", debugVal, py_logger, 4)
      raise SystemExit(f'[!] {loc["8"]}')
  


# <-------------------------->



class ForcedRebootException(Exception):
  def __init__(self, *args):
    if args:self.message = args[0]
    else:self.message = None

  def __str__(self):
    if self.message:return self.message
    else:return "ForcedRebootException has been raised"
conf_file = []


def logo():

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




# <-------------------------->









if debugVal == False:cls()
logo()



th = Thread(target=check_all_relevant_version, args=(loc,False)).start()



try:
  do = os.getcwd()
except OSError:

  debDEF(f"Unable to get a working directory.", debugVal, py_logger, 4)
  raise OSError(f'{red}[!] {loc["7"]}')


if "/content" in os.getcwd():

  debDEF(f"Colab platform found.", debugVal, py_logger, 1)
  print(f"""{white}{'='*15}- {red}WARNING!{white} -{'='*15}""")
  print(f'{red} {loc["6"]} {white}')

  from google.colab import drive

  try:
    print(f"""{white}{'='*15}- {green}Connecting...{white} -{'='*15}""")
    drive.mount("/content/MyDrive", force_remount=True)
    debDEF(f"Connect to Google Collab - OK", debugVal, py_logger, 4)


  except:
    print(f"""{white}{'='*15}- {red}Connecting Failed...{white} -{'='*15}""")
    debDEF(f"Unable to connect to Google Collab", debugVal, py_logger, 4)
    raise SystemError(f"{red}[!] Error to connecting to drive...{white}")
  print(f"""{white}{'='*15}- {green}Connecting OK...{white} -{'='*15}""")


  try:
    per1 = os.getcwd()
    os.chdir("/content/MyDrive/MyDrive/Colab Notebooks")
    per2 = os.getcwd()
    debDEF(f"[Directory change] {per1} -> {per2}", debugVal, py_logger, 1)
  except OSError as err:
    raise OSError(f'{red}[!] {loc["7"]}')
  try:
    os.mkdir("Dand_Crop")
  except FileExistsError:
    pass
  os.chdir(os.getcwd() + "/" + "Dand_Crop")

  # system('!touch "/content/MyDrive/Colab Notebooks/setup.py"')



# <------------------------->


print(f"""{'='*15}- {loc['1']} -{'='*15}{turquoise}
{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}{white}""")


print(f"""{'='*15}- {loc['2']} -{'='*15}
{yellow}[*] OS Name: {os.name.upper()}{white}""")


debDEF(f"""{'='*15}- OS -{'='*15}""", debugVal, py_logger, 1)
debDEF(f"""[*] OS Name: {os.name.upper()}""", debugVal, py_logger, 1)


print(f"""{'='*15}- {loc['3']} -{'='*15}""")

check_all_relevant_version(loc,True)

# <------------------------->




one_path = os.getcwd()
ext_list = list()

print(f"{loc['0']}")
print(f'''{white} {'='*15} Выберите скачиваемую библиотеку {'='*15}''')

# <------------------------->

try:
  chdir = input(f'''{red}[!]{yellow} Скачивание какой библиотеки вы бы хотели совершить?
{turquoise}[1] IMGS
[2] IMGS18 (18+)
[3] Своя
{blue}>>> ''')

  ch = input('Выделить какой-либо сайт из списка? (Y/N) >>> ')
  if ch == 'Y':
    ch = input('Введите нужный вам сайт >>> ')
    aaa = 'N'
    while aaa != 'Y':
      aaa = input('Вы ввели правильный текст? (Y/N) >>> ')
      if aaa  == 'Y':
        site_zametka = ch
        file_name_site = site_zametka.replace('.','_').replace('-','_')
      else:
        ch = input('Введите нужный вам сайт >>> ')
  else:
    site_zametka = 'donmai.us'
except KeyboardInterrupt:
      debDEF(f"""{'='*15}- Downloading KeyboardInterrupt -{'='*15}""", debugVal, py_logger, 1)
      debDEF(f"""The user aborted code execution.""", debugVal, py_logger, 4)

      print('\r', end='')
      
      print('The selection of the library to download was interrupted by the user. Terminate permanently?')
      che = input('Terminate? (Y/N) >>> ')
      if che == 'Y':
        val = True
        debDEF(f"""The script has been completed in [{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]""", debugVal, py_logger, 1)
        raise SystemExit
      else:
        print(f'''{white} {'='*15} Выберите скачиваемую библиотеку {'='*15}''')
        chdir = input(f'''{red}[!]{yellow} Скачивание какой библиотеки вы бы хотели совершить?
{turquoise}[1] IMGS
[2] IMGS18 (18+)
[3] Своя
{blue}>>> ''')
except Exception as err:
    debDEF(f'[ERROR] {err} p.s блять что?)', debugVal, py_logger, 3)

      






while chdir != '1' or chdir != '2':
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

  debDEF(f"Created a new directory named [{name_dir}], perm_error = False.", debugVal, py_logger, 1)
except FileExistsError:
  debDEF(f"A directory with the same name [{name_dir}] was found.", debugVal, py_logger, 2)

except PermissionError:
  debDEF("An error occurred while creating a new directory.", debugVal, py_logger, 2)
  perm_error = True
  name_dir = ""
  pass


debDEF(f"Dir_pref = {dir_pref}", debugVal, py_logger, 1)
download_to = os.getcwd() + dir_pref + str(name_dir)
print(f"""{white}{'='*15}- {loc['17']} -{'='*15}
{green}[*] {loc["12"]}: {os.getcwd()}
[*] {loc["13"]} :      {download_to}""")

debDEF(f"""{'='*15}- PATH -{'='*15}""", debugVal, py_logger, 1)
debDEF(f"[*] Working Directory: {os.getcwd()}", debugVal, py_logger, 1)
download_in = os.getcwd() + dir_pref +str(name_dir)
debDEF(f"""[*] Download in:      {download_in}""", debugVal, py_logger, 1)

pythonanywhere_key = False



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
_103 = []
_unc = []


def download_function(url, name_file, err_dict, err_info, site_,
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
    debDEF(f"""File with name {name_file} and link ({url}) was downloaded successfully.""", debugVal, py_logger, 1)
    status = '200'

  except HTTPError as err_code:

    print(f"{red}[-] {red}{err_code.code}: {blue}{name_file}{white}  URL: {url[0:ind]}")
    err_dict.append(f"{url}")
    err_info.append({f"{name_file}": f"{err_code.code}"})
    if err_code.code == 403:
      if site_zametka in url:site_.append(f"{url}")
    debDEF(f"""File named {name_file} and link ({url}) was NOT downloaded and returned code: {err_code.code}""", debugVal, py_logger, 2)
    status = f'{err_code.code}'

  except urllib.error.URLError as err_code:
    err_dict.append(f"{url}")
    if "[WinError 10054]" in str(err_code):
      print(f"{red}[-] {red}522: {blue}{name_file}{white}  URL: {url[0:ind]}")
      
      debDEF(f"""File with name {name_file} and link ({url}) was NOT downloaded due to lack of server response.""", debugVal, py_logger, 2)
      err_info.append({f"{name_file}": "522"})
      status = f'522'

    elif "[Errno 99]" in str(err_code):
      print(f"{red}[-] {red}524: {blue}{name_file}{white}  URL: {url[0:ind]}")
      err_info.append({f"{name_file}": "524"})
      debDEF(f"""File with name {name_file} and link ({url}) was NOT downloaded due to connection failure.""", debugVal, py_logger, 2)
      status = f'524'

    elif "[SSL: WRONG_VERSION_NUMBER]" in str(err_code):
      print(f"{red}[-] {red}526: {blue}{name_file}{white}  URL: {url[0:ind]}")
      err_info.append({f"{name_file}": "526"})
      debDEF(f"""The file with name {name_file} and link ({url}) was NOT downloaded due to mismatch of security certificate or parental controls.""", debugVal, py_logger, 2)
      status = f'526'

    elif "[Errno 11001]" in str(err_code):
      print(f"{red}[-] {red}101: {blue}{name_file}{white}  URL: {url[0:ind]}")
      err_info.append({f"{name_file}": "101"})
      debDEF(f"""The file with name {name_file} and link ({url}) was NOT downloaded due not connected to Enternet.""", debugVal, py_logger, 2)
      status = f'101'

    elif "[WinError 10060]" in str(err_code):
      print(f"{red}[-] {red}524: {blue}{name_file}{white}  URL: {url[0:ind]}")
      err_info.append({f"{name_file}": "524"})
      debDEF(f"""The file with name {name_file} and link ({url}) was NOT downloaded due not connected to Enternet.""", debugVal, py_logger, 2)
      status = f'524'    

    elif "[Errno 104]" in str(err_code):
      print(f"{red}[-] {red}524: {blue}{name_file}{white}  URL: {url[0:ind]}")
      err_info.append({f"{name_file}": "524"})
      debDEF(f"""The file with name {name_file} and link ({url}) was NOT downloaded due not connected to Enternet.""", debugVal, py_logger, 2)
      status = f'524' 

    elif "<urlopen error retrieval incomplete:" in str(err_code):
      print(f"{violet}[?] 103: {blue}{name_file}{white}  URL: {url[0:ind]}")
      err_info.append({f"{name_file}": "103"})
      debDEF(f"""The file with name {name_file} and link ({url}) was NOT downloaded due file download broken.""", debugVal, py_logger, 2)
      status = f'103' 

    else:
      # print(err_code)
      print('\r', end='')
      err_code = str(err_code).replace('<','').replace('>','').replace('urlopen error ','')
      print(f"{violet}[?] ___ ({err_code}): {blue}{name_file}{white}  URL: {url[0:ind]}")
      err_info.append({f"{name_file}": f"{err_code}"})
      debDEF(f"""File with name {name_file} and link ({url}) was NOT loaded due to unknown error: {err_code}.""", debugVal, py_logger, 2)
      status = f'___ ({err_code})'

  except http.client.RemoteDisconnected:
    print(
      f"{violet}[-] {violet}101: {blue}{name_file}{white}  URL: {url[0:ind]}")
    err_info.append({f"{name_file}": "101"})
    debDEF(f"""The file with the name {name_file} and link ({url}) was NOT downloaded due to the user disconnecting from the Internet.""", debugVal, py_logger, 2)
    status = f'101'

  except ConnectionResetError:
    print(
      f"{violet}[-] {violet}101: {blue}{name_file}{white}  URL: {url[0:ind]}")
    err_info.append({f"{name_file}": "101"})
    debDEF(f"""The file with the name {name_file} and link ({url}) was NOT downloaded due to the user disconnecting from the Internet.""", debugVal, py_logger, 2)
    status = f'101'

  except ValueError as err:
    print(f"{violet}[?] 102: {blue}{name_file}{white}  URL: {url[0:ind]}")
    err_info.append({f"{name_file}": f"102"})
    debDEF(f"""File with name {name_file} and link ({url}) was NOT downloaded due to unformatted link.""", debugVal, py_logger, 2)
    status = f'102'
  
  # except urllib.ContentTooShortError:
  #   print(f"{violet}[?] 103: {blue}{name_file}{white}  URL: {url[0:ind]}")
  #   err_info.append({f"{name_file}": f"103"})
  #   debDEF(f"""File with name {name_file} and link ({url}) was NOT downloaded due to file download broken.""", debugVal, py_logger, 2)
  #   status = f'103'


  except Exception as err:
    print(f"{violet}[?] ___  ({err_code}): {blue}{name_file}{white}  URL: {url[0:ind]}")
    err_info.append({f"{name_file}": f"{err}"})
    debDEF(f"""File with name {name_file} and link ({url}) was NOT loaded due to unknown error: {err}.""", debugVal, py_logger, 2)

    status = f'___ ({err_code})'

  return status, err_dict, err_info, site_, pythonanywhere_key


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

  debDEF(f"""{'='*15}- Downloading Info -{'='*15}""", debugVal, py_logger, 1)
  debDEF(f"""LEN objects - {len(ur)}""", debugVal, py_logger, 1)

  err_dict = []
  site_ = []
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

          def ww1(i, url, err_dict, err_info, site_, exten, err_name_file,pythonanywhere_key):
            name_file = f"{i}{exten}"

            
            for f in range(5):
              if f'{(i-f)}{exten}' in str(_101):
                  check_internet()

            if val_toast == True:update_progress({'value': f'{i}/{len(ur)}','valueStringOverride': f'{i}/{len(ur)} objects','title': f'Последняя ошибка: {err_name_file}'})


            while not os.path.exists(name_file):
              try:
                status, err_dict, err_info, site_, pythonanywhere_key = (download_function(url, name_file, err_dict, err_info,site_, pythonanywhere_key))

                if status == '200':
                  _200.append({f'{name_file}': f'{url}'})
                elif status == '000':
                  _000.append({f'{name_file}': f'{url}'})
                elif status == '101':
                  _101.append({f'{name_file}': f'{url}'})
                elif status == '102':
                  _102.append({f'{name_file}': f'{url}'})
                elif status == '103':
                  _103.append({f'{name_file}': f'{url}'})
                elif status == '400':
                  _400.append({f'{name_file}': f'{url}'})
                elif status == '401':
                  _401.append({f'{name_file}': f'{url}'})
                elif status == '402':
                  _402.append({f'{name_file}': f'{url}'})
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
                    if status == '103':
                        sleep(5)
                        status, err_dict, err_info, site_, pythonanywhere_key = (download_function(url, name_file, err_dict, err_info,site_, pythonanywhere_key))
                        if status != "200":
                          err_name_file = name_file
                          break
                    else:
                      err_name_file = name_file
                      break
                else:pass


                if val_toast == True:update_progress({'title': f'Последняя ошибка: {err_name_file}'})
              except Exception as err_:
                debDEF(f'PON: {err_}', debugVal, py_logger, 3)
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
                                          site_, exten, err_name_file,
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

        def ww2(i, url, err_dict, err_info, site_, exten):
          name_file = f"{i}{exten}"
          if val_toast == True:update_progress({'value': f'{i}/{len(ur)}','valueStringOverride': f'{i}/{len(ur)} videos'})


          while not os.path.exists(name_file):
            try:
              status, err_dict, err_info, site_ = download_function(
                url, name_file, err_dict, err_info, site_)

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

        ww2(i, url, err_dict, err_info, site_, exten)
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
  return err_dict, site_, err_info, pythonanywhere_key


try:
  err_count, site_, err_info, pythonanywhere_key = main(pythonanywhere_key)
  debDEF(f"""{'='*15}- Downloading OK -{'='*15}""", debugVal, py_logger, 2)
  if pythonanywhere_key == True:
    debDEF(f"""[Modules.pythonanywhere] -> True""", debugVal, py_logger, 1)
    if (input(f"{loc['29']}? (Y/N) >>> ") == "Y"):
      debDEF(f"""[Modules.pythonanywhere] INPUT-> True""", debugVal, py_logger, 1)
      try:
        from modules.pythonanywhere import pythonanywhere_def
        os.chdir(download_to)
        print(f'''{'='*15}- {loc['24']} -{'='*15}''')

        try:
          os.mkdir('addition')
          perm_error = False
          debDEF(f"Created a new directory named [addition], perm_error = False.", debugVal, py_logger, 1)
        except FileExistsError:
          perm_error == False
          debDEF(f"A directory with the same name [addition] was found.", debugVal, py_logger, 2)
          pass
        except PermissionError:
          debDEF(f"An error occurred while creating a new directory [addition].", debugVal, py_logger, 2)
          perm_error = True
          name_dir = ""
          pass


        
        if perm_error == False:d = download_in  + dir_pref + 'addition'
        else:d = download_in   + dir_pref + ''
        os.chdir(d)
        try:
          outp= pythonanywhere_def()
          if outp != 'OK':
              debDEF(f"""[Modules.pythonanywhere] ResponseCodeError: {outp}""", debugVal, py_logger, 3)
        except Exception as err:
           debDEF(f"""[Modules.pythonanywhere] Error: {err}""", debugVal, py_logger, 4, exc_info=True)

        os.chdir(download_in)
      except ModuleNotFoundError as err:
        debDEF(f"""[Modules.pythonanywhere] ModuleNotFoundError: {err}.""", debugVal, py_logger, 4)
      # except Exception as err:
      #   py_logger.critical(f"""pythonanywhere_def = Error  ({err}).""")
    else:debDEF(f"""[Modules.pythonanywhere] INPUT -> False""", debugVal, py_logger, 1)
  else:debDEF(f"""[Modules.pythonanywhere] -> False""", debugVal, py_logger, 1)

  
except KeyboardInterrupt:
  err_count = [].append({'Downloading KeyboardInterrupt'})
  site_ = [].append({'Downloading KeyboardInterrupt'})
  err_info = [].append({'Downloading KeyboardInterrupt'})

  debDEF(f"""{'='*15}- Downloading KeyboardInterrupt -{'='*15}""", debugVal, py_logger, 1)
  debDEF(f"""The user aborted code execution.""", debugVal, py_logger, 4)
  print(f'{red}[!] {loc["15"]}...')
except Exception as err:
  err_count = [].append({'Downloading KeyboardInterrupt'})
  site_ = [].append({'Downloading KeyboardInterrupt'})
  err_info = [].append({'Downloading KeyboardInterrupt'})
  debDEF(f"""[Main] Error: {err}""", debugVal, py_logger, 4)

print(white)

endTime = time.time()

print(f"{loc['28']}: {str(timedelta(seconds = (endTime - startTime))).split('.')[0]}")


debDEF(f"""{'='*15}- Files Statistics -{'='*15}""", debugVal, py_logger, 1)
# ff = os.getcwd()
# d = os.getcwd()#.split(dir_pref)[-1]
starting_script_time2 = starting_script_time.replace('-','_').replace(' ','_').replace(':','_')
# os.mkdir(starting_script_time2)
os.chdir(working_directory + dir_pref + 'Statistics')
try:
  os.mkdir(starting_script_time2)
  perm_error = False
  debDEF(f"Created a new directory named [{starting_script_time2}], perm_error = False.", debugVal, py_logger, 1)
except FileExistsError:
  debDEF(f"A directory with the same name [{starting_script_time2}] was found.", debugVal, py_logger, 2)
  pass
except PermissionError:
  debDEF(f"An error occurred while creating a new directory [{starting_script_time2}].", debugVal, py_logger, 2)
  perm_error = True
  name_dir = ""
  pass

if perm_error == False:d = working_directory + dir_pref + 'Statistics'  + dir_pref + starting_script_time2
else:d = working_directory + dir_pref + 'Statistics'  + dir_pref + ''
os.chdir(d)

#print(os.getcwd(), d)

if len(err_count) != 0:
    try:
      with open(f"{file_name_errors}", "w") as outfile:
        json.dump(err_count, outfile, indent=4)
      debDEF(f"""File created [{file_name_errors}]""", debugVal, py_logger, 1)
    except TypeError as err:
      debDEF(f"""TypeError: The file [{file_name_errors}] would not be created for a reason: {err}""", debugVal, py_logger, 3)
    except Exception as err:
      debDEF(f"""Exception: The file [{file_name_errors}] would not be created for a reason: {err}""", debugVal, py_logger, 3)

if len(site_) != 0:
    try:
      with open(f"{file_name_site}", "w") as outfile:
        json.dump(site_, outfile, indent=4)
      debDEF(f"""File created [{file_name_site}]""", debugVal, py_logger, 1)
    except TypeError as err:
      debDEF(f"""TypeError: The file [{file_name_site}] would not be created for a reason: {err}""", debugVal, py_logger, 3)
    except Exception as err:
      debDEF(f"""Exception: The file [{file_name_site}] would not be created for a reason: {err}""", debugVal, py_logger, 3)

if len(err_info) != 0:
    try:
      with open(f"{file_name_err_info}", "w") as outfile:
        json.dump(err_info, outfile, indent=4)
      debDEF(f"""File created [{file_name_err_info}]""", debugVal, py_logger, 1)
    except TypeError as err:
      debDEF(f"""TypeError: The file [{file_name_err_info}] would not be created for a reason: {err}""", debugVal, py_logger, 3)
    except Exception as err:
      debDEF(f"""Exception: The file [{file_name_err_info}] would not be created for a reason: {err}""", debugVal, py_logger, 3)

if len(ext_list) != 0:
    try:  
      with open('info.json', 'w') as file:
        json.dump(ext_list, file, indent=4)
      debDEF(f"""File created [info.json]""", debugVal, py_logger, 1)
    except TypeError as err:
      debDEF(f"""TypeError: The file [info.json] would not be created for a reason: {err}""", debugVal, py_logger, 3)
    except Exception as err:
      debDEF(f"""Exception: The file [info.json] would not be created for a reason: {err}""", debugVal, py_logger, 3)

debDEF(f"""Catalog: {os.getcwd()}""", debugVal, py_logger, 1)

os.chdir(working_directory)
# except NameError as err:
#   print(err)
#   pass
# except Exception as err:
#   print(err)




debDEF(f"""The database download was completed in [{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]""", debugVal, py_logger, 1)
print(f"""{'='*15}- Скачивание Завершено -{'='*15}""")

# try:
#   from module_res_def import res_def
#   ch = input(f'\n{red}[!] {loc["16"]} (Y/n) >>> {white}')
#   py_logger.info(
#     f"""The meaning of calling the image processing function:  {ch}.""")
#   if ch == "Y": res_def(name_dir)
#   else: pass
# except KeyboardInterrupt:
#   py_logger.info(
#     f"""The user has canceled an image encoding call request (KeyboardInterrupt)."""
#   )
# except Exception as err:
#   py_logger.info(
#     f"""The script has canceled an image encoding call request ({err}).""")




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



val = True
