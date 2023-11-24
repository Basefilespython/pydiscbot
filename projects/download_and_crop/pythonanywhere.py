from os import system
import requests

username = 'BAZEOFNEKOARTS'
token = '09cc0a15fff58e5f3b129735c75e913cd182a3e2'
path = '/home/BAZEOFNEKOARTS/mysite/template/static/'

class ResponseCodeError(Exception):
  def __init__(self, *args):
    if args:self.message = args[0]
    else:self.message = None

  def __str__(self):
    if self.message:return self.message
    else:return "ResponseCodeError has been raised"

def download(path):
    try:
        response = requests.get(f'https://www.pythonanywhere.com//api/v0/user/{username}/files/path{path}',headers={'Authorization': f'Token {token}'})
        if response.status_code == 200:
            try:from tqdm import tqdm
            except ModuleNotFoundError:
                system('pip install tqdm')
                from tqdm import tqdm

            name_file  = (path.split('/')[-1])
                
            if name_file != '':
                with open(name_file, "wb") as handle:  
                    for data in tqdm(response.iter_content()):
                        handle.write(data)
                    return 'OK'
                
        else:raise ResponseCodeError(str(response.status_code))
    except Exception as err:raise str(err)




def pythonanywhere_def():
    response = requests.get(f'https://www.pythonanywhere.com//api/v0/user/{username}/files/tree/?path={path}',headers={'Authorization': f'Token {token}'})
    response.text
    eee = (response.content).decode("utf-8").replace('[','').replace(']','').replace(' ','').replace('''"''','''''')
    for url_file in eee.split(','):

        try:download(url_file)
        except ResponseCodeError as code:return code
        except Exception as err:raise err
