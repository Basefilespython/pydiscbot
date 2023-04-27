
def pythonanywhere_def():
    import requests
    username = 'BAZEOFNEKOARTS'
    token = '09cc0a15fff58e5f3b129735c75e913cd182a3e2'
    path = '/home/BAZEOFNEKOARTS/mysite/template/static/'



    def download(path):
        response = requests.get(f'https://www.pythonanywhere.com//api/v0/user/{username}/files/path{path}',headers={'Authorization': 'Token {token}'.format(token=token)})
        if response.status_code == 200:

            from tqdm import tqdm

            name_file  = (path.split('/')[-1])
            
            if name_file != '':
                with open(name_file, "wb") as handle:
                    
                    for data in tqdm(response.iter_content()):
                        handle.write(data)




    response = requests.get(f'https://www.pythonanywhere.com//api/v0/user/{username}/files/tree/?path={path}',headers={'Authorization': 'Token {token}'.format(token=token)})

    eee = (response.content).decode("utf-8").replace('[','').replace(']','').replace(' ','').replace('''"''','''''')
    for url_file in eee.split(','):
        download(url_file)
