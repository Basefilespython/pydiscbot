import time
import os
from os import DirEntry, system
import sys

try:
  import requests
except ModuleNotFoundError:
  system('pip install requests')
  import requests

try:
  from tqdm import tqdm
except ModuleNotFoundError:
  system('pip install tqdm')
  from tqdm import tqdm

# url_main = f"https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/{file_name}"
# url_files = f"https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/{file_name}"
# url_loc = f'https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/localization/{file_name}'

file_names = ['random_neko_list.py', 'main.py', 'setup.py', 'exctensions_module.py','pythonanywhere.py']
file_names_main = ['LICENSE', 'README.md', 'about_the_creator.md']
file_names_loc = ['EN.py', 'RU.py']


if str(os.name) == "nt":dir_pref = "\\"
else:dir_pref = "/"

def download_file_from_github(url, WorkingDirectory=os.getcwd(), logger=None):
  local_filename = url.split("/")[-1]

  try:
    if WorkingDirectory != os.getcwd():
      if logger != None: logger.info(f"[Downloading file] Name: {local_filename} [WorkingDirectoryECT]: {WorkingDirectory}")
      else: print(f"[Downloading file] Name: {local_filename} [WorkingDirectoryECT]: {WorkingDirectory}")
    else:
      if logger != None: logger.info(f"[Downloading file] Name: {local_filename}")
      else: print(f"[Downloading file] Name: {local_filename}")

    orig = os.getcwd()

    do, WorkingDirectory, dir_name = DownloadingPath(local_filename)
    print(f'''
DO: {do}
WorkingDirectory: {WorkingDirectory}
Dir_Name: {dir_name}''')
    if not os.path.exists(WorkingDirectory):
      try:os.mkdir(dir_name)
      except FileExistsError:dir_name = ''
      except:dir_name = ''

    os.chdir(WorkingDirectory)

    with requests.get(url, stream=True, allow_redirects=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
          # try:
          #   for data in tqdm(r.iter_content()):f.write(data)
          # except Exception as err:
          #   print(err)
          for chunk in r.iter_content(chunk_size=8192*64):f.write(chunk)

          print('\t')
          print(local_filename)
    os.chdir(orig)
    return "ok"

  except requests.exceptions.HTTPError as err:

    if "404" in str(err):
      return "не найдено"
    return err
  except Exception as err:
    # raise
    print(err)
    # return err

def check_installed_files(directory):
    in_folder = []
    with os.scandir(directory) as listOfEntries:
        i = 0
        for entry in listOfEntries:
          if entry.name == sys.argv[0]:
            i = i + 1
            if entry.is_file():
                if entry.name == 'main.py':
                    in_folder.append(entry.name)
            
            if entry.is_dir():
                if entry.name == 'modules':
                    with os.scandir(directory + dir_pref + entry.name) as listOfEntries:
                        for entry in listOfEntries:
                            if entry.is_file():
                                if entry.name == 'random_neko_list.py':in_folder.append(entry.name)
                                elif entry.name == 'pythonanywhere.py':in_folder.append(entry.name)
                                elif entry.name == 'inn.py':in_folder.append(entry.name)
                                elif entry.name == 'exctensions_module.py':in_folder.append(entry.name)
                                else:pass
                elif entry.name == 'localization':
                    with os.scandir(directory + dir_pref + entry.name) as listOfEntries:
                        for entry in listOfEntries:
                            if entry.is_file():
                                if entry.name == 'RU.py':in_folder.append(entry.name)
                                elif entry.name == 'EN.py':in_folder.append(entry.name)
                                else:pass

        if i == 0:
          for file in ['random_neko_list.py', 'pythonanywhere.py', 'inn.py', 'exctensions_module.py', 'RU.py', 'EN.py']:in_folder.append(file)
    return in_folder


def DownloadingPath(file_name):
        if (file_name == 'about_the_creator.md') or (file_name == 'README.md'): dir_name = 'about'
        if (file_name == 'random_neko_list.py') or (file_name == 'setup.py') or (file_name == 'exctensions_module.py') or (file_name == 'pythonanywhere.py'): dir_name = 'modules'
        if (file_name == 'EN.py') or (file_name == 'RU.py'): dir_name = 'localization'
        if file_name == 'LICENSE.txt': dir_name = 'LICENSE'
        print(file_name)

        do = str(str(os.getcwd()) + str(dir_pref))
        posle = str(os.getcwd() + dir_pref + dir_name + dir_pref)
        return do, posle, dir_name

def DownloadingSetupFilesFunction(path=os.getcwd()):
  in_folder = check_installed_files(path)
  print(len(in_folder))
  for file in in_folder:
    if file in  file_names:url = f"https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/{file}"
    elif file in file_names_loc:url = f'https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/localization/{file}'
    else:url = None

  if url != None: download_file_from_github(url, WorkingDirectory = path)


if __name__ == '__main__':
    DownloadingSetupFilesFunction()
  


