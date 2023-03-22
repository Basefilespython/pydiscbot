from time import sleep
import http
from PIL import Image
import sys
import os
import json
from urllib.request import HTTPError
import urllib.request
from os import system
import random
s_version = "2.1.13"


black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"


def logo():
    try:
        from colorama import Fore
        colors = [Fore.RED, Fore.GREEN, Fore.YELLOW,
                  Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
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
    import requests
except:
    system("pip install requests")
    import requests


try:
    from alive_progress import alive_bar
    alive_a = True
except:
    system("pip install alive-progress")
    try:
        from alive_progress import alive_bar
        alive_a = True
    except ModuleNotFoundError:
        alive_a = False
        print(f'{red}[!] ModuleNotFoundError: alive_progress.{white}')

try:
    import PIL
except:
    system("pip install Pillow")
    import PIL

try:
  do = os.getcwd()
except OSError:
     raise OSError(f'{red}[!] ПЕРЕЗАПУСТИТЕ СРЕДУ ВЫПОЛНЕНИЯ СКИПТА.')


if '/content' in os.getcwd():
    try:
        system('!mkdir data && wget https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/setup.py')
    except:
        pass
    print(f'''{white}{'='*15}- {red}WARNING!{white} -{'='*15}''')
    print(f"{red}Ваша OS похожа на Colab. Все скачанные файлы будут скачиваться в ваш Google Drive. А точнее в подпапку где сохранен данный файл.{white}")
    from google.colab import drive
    try:
        print(f'''{white}{'='*15}- {green}Connecting...{white} -{'='*15}''')
        drive.mount("/content/MyDrive", force_remount=True)
    except:
        print(f'''{white}{'='*15}- {red}Connecting Failed...{white} -{'='*15}''')
        raise SystemError(f'{red}[!] Error to connecting to drive...{white}')
    print(f'''{white}{'='*15}- {green}Connecting OK...{white} -{'='*15}''')

    try:
      per1 = os.getcwd()
      os.chdir('/content/MyDrive/MyDrive/Colab Notebooks')
      per2 = os.getcwd()
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
except ModuleNotFoundError:
    posle = os.getcwd()
    os.chdir(do)
    download_file_from_github('random_neko_list.py')
    os.chdir(posle)
    try:
        try:
            # import sys
            sys.path.insert(1, '../Dand_Crop')
            from random_neko_list import *
        except NameError:
            try:
                from random_neko_list import *
            except:
                raise SystemExit('\n[!] База не обнаружена!')
    except ImportError:
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


black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"


def old(nversion):
    print(f"{violet}[*] OLD-VERSION: {s_version}, NEW-VERSION: {nversion}")
    print(
        f'''{yellow}[*] У вас установлена устаревшая версия скрипта!{white}''')
    ch = input(f"{green}[!]{white} Установить новую версию? (Y/N) >>> ")
    if ch == "Y":
        check("main.py")
        raise SystemError("")
    else:
        pass

print(f'''{'='*15}- OS -{'='*15}
{yellow}[*] OS Name: {os.name.upper()}{white}''')



def check_version(sversion):
    nversion = json.loads(requests.get(
        "https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/version.json").text)['ver']

    s1, s2, s3, n1, n2, n3 = str(sversion).split('.')[0], str(sversion).split('.')[1], str(sversion).split(
        '.')[2], str(nversion).split('.')[0], str(nversion).split('.')[1], str(nversion).split('.')[2]
    print(f'''{'='*15}- VERSION -{'='*15}''')
    if s1 >= n1:
        if s2 >= n2:
            if s3 >= n3:
                print(f'''{violet}[*] VERSION: {s_version}''')
                print(
                    f'''{green}[*] У вас установлена самая актуальная версия скрипта!{white}''')

            else:
                old(nversion)
        else:
            old(nversion)
    else:
        old(nversion)


check_version(s_version)


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
- 526 - Блокировка сертификата/ом (скорее разное время, или родительский контроль)''')


if str(os.name) == 'nt':
    dir_pref = "\\"
else:
    dir_pref = "/"

print(f'''{white}{'='*15}- PATH -{'='*15}
{green}[*] Работающий каталог: {os.getcwd()}
[*] Скачивание в :      {os.getcwd() + dir_pref +str(name_dir)}''')




def main():
    
    ur = imgs18

    print(f'''{white}{'='*15}- Количество изображений - {len(ur)} -{'='*15}''')

    err = []
    vk_403_err = []
    err_info = []
    def download():
        i = 1
        if alive_a == True:
            with alive_bar(len(ur)) as bar:

                for url in ur:

                    url = str(url)
                    url = url.replace(" ", "%20")

                    def ww1(i):

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
                            if '?size=' in url:
                              ind =  url.find('?size=')
                            else:
                                if '?extra=' in url:
                                   ind =  url.find('?extra=') 
                                else:
                                    ind = len(url)  
    
                             


                            try:
                                urllib.request.urlretrieve(str(url), name_file)
                                print(f"{green}[+] 200: {blue}{name_file}{white}  URL: {url[0:ind]}")
                            except HTTPError as err_code:
                                #if err_code.code == 400:print(f"{red}[-] {red}400: {blue}{name_file}{white}  URL: {url}")
                                #if err_code.code == 401:print(f"{red}[-] {red}401: {blue}{name_file}{white}  URL: {url}")
                                #if err_code.code == 402:print(f"{red}[-] {red}402: {blue}{name_file}{white}  URL: {url}")
                                #if err_code.code == 403:print(f"{red}[-] {red}403: {blue}{name_file}{white}  URL: {url}")
                                #if err_code.code == 404:print(f"{red}[-] {red}404: {blue}{name_file}{white}  URL: {url}")
                                #else:                   print(f"{red}[-] {red}{err_code.code}: {blue}{name_file}{white}  URL: {url}")
                                #  pass
                                print(f"{red}[-] {red}{err_code.code}: {blue}{name_file}{white}  URL: {url[0:ind]}")

                                err.append(f"{url}")
                                err_info.append({f'{name_file}': f'{err_code.code}'})
                                if 'userapi.com' in url and err_code.code == 403:vk_403_err.append(f'{url}')
                                break
                            
                            except urllib.error.URLError as err_code:
                                if "[WinError 10054]" in str(err_code):
                                  print(f"{red}[-] {red}522 : {blue}{name_file}{white}  URL: {url[0:ind]}")
                                  err_info.append({f'{name_file}': "522"})
                                if "[Errno 99]" in str(err_code):
                                    print(f"{red}[-] {red}524: {blue}{name_file}{white}  URL: {url[0:ind]}")
                                    err_info.append({f'{name_file}': "524"})
                                if "[SSL: WRONG_VERSION_NUMBER]" in str(err_code):
                                    print(f"{red}[-] {red}526: {blue}{name_file}{white}  URL: {url[0:ind]}")
                                    err_info.append({f'{name_file}': "526"})
                                else:pass

                                err.append(f"{url}")
                                if 'userapi.com' in url:vk_403_err.append(f'{url}')
                                break

                        if url not in err:
                            src = one_path + dir_pref + name_file
                            os.chdir(one_path)
                            dest = f'{os.getcwd()}{dir_pref}{name_dir}{dir_pref}{name_file}'
                            try:
                                os.rename(src, dest)
                            except FileExistsError:
                                os.chdir( f'{os.getcwd()}{dir_pref}{name_dir}{dir_pref}')
                                os.remove(name_file)
                                os.chdir(one_path)
                                os.rename(src, dest)
                            except FileNotFoundError:
                                pass
                        bar()

                    ww1(i)
                    i = i + 1
        if alive_a == False:
                for url in ur:

                    url = str(url)
                    url = url.replace(" ", "%20")

                    def ww2(i):

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
                                print(f"{green}[+] 200: {blue}{name_file}{white}  URL: {url}")
                            except HTTPError as err_code:
                                #if err_code.code == 400:print(f"{red}[-] {red}400: {blue}{name_file}{white}  URL: {url}")
                                #if err_code.code == 401:print(f"{red}[-] {red}401: {blue}{name_file}{white}  URL: {url}")
                                #if err_code.code == 402:print(f"{red}[-] {red}402: {blue}{name_file}{white}  URL: {url}")
                                #if err_code.code == 403:print(f"{red}[-] {red}403: {blue}{name_file}{white}  URL: {url}")
                                #if err_code.code == 404:print(f"{red}[-] {red}404: {blue}{name_file}{white}  URL: {url}")
                                #else:                   print(f"{red}[-] {red}{err_code.code}: {blue}{name_file}{white}  URL: {url}")
                                #  pass
                                print(f"{red}[-] {red}{err_code.code}: {blue}{name_file}{white}  URL: {url}")

                                err.append(f"{url}")
                                err_info.append({f'{name_file}': f'{err_code.code}'})
                                if 'userapi.com' in url and err_code.code == 403:vk_403_err.append(f'{url}')
                                break
                            
                            except urllib.error.URLError as err_code:
                                if "[WinError 10054]" in str(err_code):
                                  print(f"{red}[-] {red}522 : {blue}{name_file}{white}  URL: {url}")
                                  err_info.append({f'{name_file}': "522"})
                                if "[Errno 99]" in str(err_code):
                                    print(f"{red}[-] {red}524: {blue}{name_file}{white}  URL: {url}")
                                    err_info.append({f'{name_file}': "524"})
                                if "[SSL: WRONG_VERSION_NUMBER]" in str(err_code):
                                    print(f"{red}[-] {red}526: {blue}{name_file}{white}  URL: {url}")
                                    err_info.append({f'{name_file}': "526"})
                                else:pass

                                err.append(f"{url}")
                                if 'userapi.com' in url:vk_403_err.append(f'{url}')
                                break

                        if url not in err:
                            src = one_path + dir_pref + name_file
                            os.chdir(one_path)
                            dest = f'{os.getcwd()}{dir_pref}{name_dir}{dir_pref}{name_file}'
                            try:
                                os.rename(src, dest)
                            except FileExistsError:
                                os.chdir( f'{os.getcwd()}{dir_pref}{name_dir}{dir_pref}')
                                os.remove(name_file)
                                os.chdir(one_path)
                                os.rename(src, dest)
                            except FileNotFoundError:
                                pass
                        

                    ww2(i)
                    i = i + 1
    download()
    return err, vk_403_err,err_info


try:
    err_count, vk_403_err,err_info = main()
except KeyboardInterrupt:
    print(f'{red}[!] Вы прервали выполнение кода...')

try:
  with open("errors.json", "w") as outfile:
      json.dump(err_count, outfile, indent=4)
  with open("vk403.json", "w") as outfile:
      json.dump(vk_403_err, outfile, indent=4)
  with open("vk403.json", "w") as outfile:
      json.dump(err_info, outfile, indent=4)
except NameError:
    pass

def res_def(name_dir):

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

    with open("baza.json", "w") as outfile:
        json.dump(img_resize, outfile, indent=4)

    import time
    # from progress.bar import IncrementalBar
    try:
        from alive_progress import alive_bar
    except ImportError:
        system("pip install alive-progress")

    with alive_bar(len(img_resize)) as bar:
        for data in img_resize:

            try:
                img = Image.open(str(data).split("'")[1])
                (width, height) = im.size
                new_image = img.resize((height*4, width*4))
                new_image.save(str(str(data).split("'")[1]))
                img.close()
            except PIL.UnidentifiedImageError:
                pass
            bar()


if input(f'\n{red}[!] Откадрировать изображения в базе? (Y/n) >>> ') == 'Y':
    res_def(name_dir)
else:
    pass

print(f"\n{white}")


def in_the_papka(dir_pref):  # перемещение файлов в их папки
    os.chdir(f'{os.getcwd()}/')
    path_one = os.getcwd()

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


sleep(30)
