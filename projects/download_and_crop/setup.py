import time
import os
from os import system

try:
    import requests
except ModuleNotFoundError:
    system('pip install requests')
    import requests


name_dir = "Dand_Crop"
first_dir = os.getcwd()

try:
    os.mkdir(name_dir)
except FileExistsError:
    pass


if str(os.name) == 'nt':
    dir_pref = "\\"
else:
    dir_pref = "/"


os.chdir(name_dir)
one_path = os.getcwd()

# , 'keep_module.py']
file_names      = ['random_neko_list.py', 'main.py', 'setup.py','exctensions_module.py']
file_names_main = ['LICENSE', 'README.md', 'about_the_creator.md']
file_names_loc  = ['EN.py', 'RU.py']


def download_file_from_github(url_id, file_name):
    url_main  = f"https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/{file_name}"
    url_files = f"https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/{file_name}"
    url_loc   = f'https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/localization/{file_name}'

    if url_id == 0:
        url = url_files
    if url_id == 1:
        url = url_main
    if url_id == 2:
        url = url_loc

    try:

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

    for file_name in file_names:
        download_file_from_github(0, file_name)

    for file_name in file_names_main:
        download_file_from_github(1, file_name)

    for file_name in file_names_loc:
        download_file_from_github(2, file_name)


update()


# try:
os.rename('LICENSE', 'LICENSE.txt')
# except:
#   pass


with os.scandir(os.getcwd()) as listOfEntries:
    os.mkdir('about')
    os.mkdir('LICENSE')
    os.mkdir('modules')
    os.mkdir('localization')
    for entry in listOfEntries:
        if entry.is_file():
            if entry.name != 'main.py':
                if (entry.name == 'about_the_creator.md') or (entry.name == 'README.md'):
                    dir_name = 'about'

                if (entry.name == 'random_neko_list.py') or (entry.name == 'setup.py') or (entry.name == 'exctensions_module.py'):
                    dir_name = 'modules'

                
                if (entry.name =='EN.py') or (entry.name =='RU.py'):
                    dir_name = 'localization'

                if entry.name == 'LICENSE.txt':
                    dir_name = 'LICENSE'

                do = str(str(os.getcwd()) + str(dir_pref) + entry.name)
                posle = str(os.getcwd() + dir_pref + dir_name + dir_pref + entry.name)
                os.rename(do, posle)
            else:
                pass


if os.name == 'nt':
    with open("start.bat", "w") as outfile:
        outfile.write(f"python main.py")
        pass

print("Установка завершена!")

os.chdir(first_dir)
try:
    time.sleep(2)
    # os.remove(__file__)
except:
    pass
