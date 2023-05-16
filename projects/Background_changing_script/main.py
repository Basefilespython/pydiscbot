###CODE by https://vk.com/id435600030



REDIR_URL_NO_TOKEN = 'https://oauth.vk.com/authorize?client_id=51630220&scope=501198815&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1'


class InputURLError(Exception):
     pass

class VKresponseCodeEror(Exception):
    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        if self.error_code == 5:
            self.message = 'Неправильный токен.'
        elif self.error_code == 7:
            self.message = 'Нет прав для выполнения этого действия.'
        else:
            pass
        return f'''{inc('SERV')} SERVER OUT MESSAGE: {self.message}'''



black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"


import requests, subprocess, webbrowser, json, socket


phot = ''
url = ''


links_file_name = 'links.json'
config_file_name= 'url_json.json'
token_file = 'config.json'


def inc(id):
    if id == 'INF':
        out = f'{yellow}[-]'
    if id == 'INF2':
        out = f'{turquoise}[-]'
    if id == 'SERV':
        out = f'{yellow}[-]'
    if id == '?':
        out = f'{red}[?]'
    if id == '!':
        out = f'{red}[!]'
    return out

def cls():
    try:
        subprocess.call("clear")
    except:
        subprocess.call("cls", shell=True)


def is_connected():
    #hostname = "www.google.com"
    try:
        socket.create_connection((socket.gethostbyname('www.google.com'), 80), 2)

        return True
    except Exception:
        print(f"{inc('!')} Вы не подключены к интернету!")
        return False
    


def bad_token():
    
    TOKEN_SPLIT = input(f'{violet}{inc("!")} Введите ваш актуальный токен {turquoise}>>> ')
    VK_TOKEN  = TOKEN_SPLIT.split('#')[1].split('&expires_in')[0].replace('access_token=','')
    member_id = TOKEN_SPLIT.split('#')[1].split('&user_id=')[1].split('&email')[0]
    return VK_TOKEN,member_id

def get_album_id(VK_TOKEN,phot_msg):
        api = requests.get("https://api.vk.com/method/photos.getById", params={
            'photos': phot_msg,
            'extended' : 1,
            'access_token': VK_TOKEN,
            'offset': 0,
            'count': 20,
            'photo_sizes': 0,
            'v': 5.103
        })
        return json.loads(api.text)


cls()


conf_file = []
try:
  with open(f"{token_file}", "r") as file:
    data = json.loads(file.read())
    VK_TOKEN,member_id = data[0]['vk_token'], data[1]['member_id']
    print(f'{inc("INF2")} токен и member_id были успешно импортированы.{white}')
except Exception as err:
  print(f'{inc("!")} Конфигурационный файл не бы найден.{white}')
  print(f'''{violet}[-] Ссылка должна быть в формате:
https://oauth.vk.com/blank.html#access_token=[token]&expires_in=0&user_id=[user_id]&email=[email]{white}

Ссылка на приложение доступа:
{REDIR_URL_NO_TOKEN}

{green}[!] Инструкция:
    1. Перейдите по ссылке.
    2. Скопируйте ссылку.
    3. Введите её сюда.{white}''')
  VK_TOKEN,member_id = bad_token()

  conf_file.append({'vk_token': f'{VK_TOKEN}'})
  conf_file.append({'member_id': f'{member_id}'})
  with open(f"{token_file}", "w") as outfile:
      json.dump(conf_file, outfile, indent=4)



# VK_TOKEN,member_id = bad_token()



def stop_token(VK_TOKEN,member_id):
    while validable_token(VK_TOKEN,member_id,'0') != True:
        print(f'''{inc('!')} Your TOKEN: {VK_TOKEN}
{violet}[-] Ссылка должна быть в формате:
https://oauth.vk.com/blank.html#access_token=[token]&expires_in=0&user_id=[user_id]&email=[email]{white}

Ссылка на приложение доступа:
{REDIR_URL_NO_TOKEN}

{green}[!] Инструкция:
    1. Перейдите по ссылке.
    2. Скопируйте ссылку.
    3. Введите её сюда.{white}''')
        VK_TOKEN,member_id = bad_token()
    print(f'STOP_TOKEN - VKTOKEN: {VK_TOKEN}')
    return VK_TOKEN,member_id




def validable_token(VK_TOKEN,member_id, id):
    if is_connected() == True:


        api = requests.get("https://api.vk.com/method/users.get", params={
                    'user_ids': member_id,
                    'access_token': VK_TOKEN,
                    'v': 5.103
                })
        data = json.loads(api.text)
        if list(data.keys())[0] == 'error':
            code = data['error']['error_code']
            descr = data['error']['error_msg']
            cls()
            if id != '1':
                try:
                    raise VKresponseCodeEror(error_code=code,message=descr)
                except VKresponseCodeEror as err:
                    print(err)
                    pass
            with open(f"{config_file_name}", "w") as outfile:
                json.dump(data, outfile, indent=4)

            return False

        else:
            if id != '1':
                cls()
                print(f'''{'='*10}- INFORMATION about USER -{'='*10}''')
                print(f"{inc('INF')} Name: {data['response'][0]['first_name']}")
                print(f"{inc('INF')} Surname: {data['response'][0]['last_name']}")

            return True
    else:
        pass




if validable_token(VK_TOKEN,member_id, '1') != True:
    webbrowser.open_new(REDIR_URL_NO_TOKEN)
    VK_TOKEN,member_id = stop_token(VK_TOKEN,member_id)

def valid_url(url):
    if url == '':
        return False
    elif url == 'eblan':
        return False

    elif url == 'ymnec':
        return False   
    
    else:
        try:       
                phot = url.split('/')[3].split('photo')[1].split('%2')

                short_id = url.split('/')[3].split('?z')[0]
                owner_id = phot[0].split('_')[0]
                wall_id = phot[1].replace('Fwall','').replace(owner_id,'').replace('_','')
                phot_id = phot[0].split('_')[1]

                return True
        except IndexError:
                print(f'''{inc("?")} Вы ввели не корректную ссылку ({url}).''')
                return False
        

def main():
    global VK_TOKEN
    global member_id
    url = ''

    print(f'''{white}{'='*10}- LINK -{'='*10}''')
    #print(f'''{violet}>>> {url}{white}''')

    print(f'''{violet}[-] Ссылка должна быть в формате:
    https://vk.com/[giuld_sport_name]?z=photo-[guild_id]_[photo_id]%2Fwall-[guild_id]_[wall_id]{white}

    {green}Инструкция:
    1. Перейдите в нужную вам группу.
    2. Выберите нужное вам изображение и откройте его.
    3. Скопируйте ссылку и введите её сюда.{white}''')

    print(f'''{'='*10}- INPUT -{'='*10}''')

    while ('?z=photo-' not in url):
            
            url = input(f'{turquoise}>>> ')
            if url == 'https://vk.com/[giuld_sport_name]?z=photo-[guild_id]_[photo_id]%2Fwall-[guild_id]_[wall_id]':
                print(f'{inc("?")} Ты думаешь, что ты самый умный? Тебе трудно идти по инструкции?')
                url = 'ymnec'
    
            if '?z=photo-' not in url:
                url = 'eblan'
            else:pass

            if valid_url(url) == True:
                pass
            else:
                url = ''



    phot = url.split('/')[3].split('photo')[1].split('%2')
    short_id = url.split('/')[3].split('?z')[0]

    links_file_name = f'links_{short_id}.json'

    owner_id = phot[0].split('_')[0]
    wall_id = phot[1].replace('Fwall','').replace(owner_id,'').replace('_','')
    phot_id = phot[0].split('_')[1]



    if validable_token(VK_TOKEN,member_id, '1') != True:
        VK_TOKEN,member_id = stop_token(VK_TOKEN,member_id)

    api = requests.get("https://api.vk.com/method/groups.getById", params={
                'group_id' : int(owner_id.replace('-','')),
                'access_token': VK_TOKEN,
                'offset': 0,
                'count': 1000,
                'photo_sizes': 0,
                'v': 5.103
            })
    data = json.loads(api.text)



    with open(f"{config_file_name}", "w") as outfile:
        json.dump(data, outfile, indent=4)


    print(f'''{white}{'='*10}- INFORMATION -{'='*10}''')
    print(f"{inc('INF')} GuildName: {data['response'][0]['name']}")


    if 2 == data['response'][0]['is_closed']:guild_type = 'частное'
    else:
        if 1 == data['response'][0]['is_closed']:
            guild_type = 'закрытое'
        else:guild_type = 'открытое'

    print(f'{inc("INF")} GuildType: {guild_type}')
    print(f'{inc("INF")} MemberShip: Вы подписаны.') if 1 == data['response'][0]['is_member'] else print(f'{inc("INF")} MemberShip: Вы не подписаны.  (пиздит фотокарточки и не стыдится)') 
    print(f'{inc("INF")} Adminship: Вы являетесь руководителем.') if 1 == data['response'][0]['is_admin'] else print(f'{inc("INF")} Adminship: Вы не являетесь руководителем.') 
    print(f'''{white}{'='*10}- INFORMATION -{'='*10}''')




    phot_msg =f'{owner_id}_{phot_id}'






    

    if validable_token(VK_TOKEN,member_id, '1') != True:
        VK_TOKEN,member_id = stop_token(VK_TOKEN,member_id)

    eee= get_album_id(VK_TOKEN,phot_msg)
    album_id = eee['response'][0]['album_id']

    print(f'''{inc("INF2")} ID выбранного альбома: {album_id}''')



    links = []

    with open(f"{config_file_name}", "w") as outfile:
        json.dump(eee, outfile, indent=4)

    if validable_token(VK_TOKEN,member_id, '1') != True:
        VK_TOKEN,member_id = stop_token(VK_TOKEN,member_id)

    api = requests.get("https://api.vk.com/method/photos.get", params={
                'owner_id': owner_id,
                'album_id' : album_id,
                'access_token': VK_TOKEN,
                'offset': 1,
                'count': 1000,
                'photo_sizes': 0,
                'v': 5.103
            })
    with open(f"ebal_url2.json", "w") as outfile:
        json.dump(json.loads(api.text), outfile, indent=4)


    count = json.loads(api.text)['response']['count']
    print(f'''{inc("INF2")} Количество изображений: {count}''')

    offset_ = []

    if round(count/1000) != 1:
        for off in range(1,round(count/1000)+2):
            offset_.append(off)
    else:
        offset_.append(1)


    print(f'''{white}{'='*10}- STARNING -{'='*10}''')



    if validable_token(VK_TOKEN,member_id, '1') != True:
        VK_TOKEN,member_id = stop_token(VK_TOKEN,member_id)


    for offset in offset_:
        
        api = requests.get("https://api.vk.com/method/photos.get", params={
                'owner_id': owner_id,
                'album_id' : album_id,
                'access_token': VK_TOKEN,
                'offset': offset,
                'count': 1000, #max 1000
                'photo_sizes': 1,
                'v': 5.103
            })

        eee = json.loads(api.text)





    

        

        for i in range(len(eee['response']['items'])):

            max_ = len(eee['response']['items'][i]['sizes']) - 1


            h, w = eee['response']['items'][i]['sizes'][max_]['height'],eee['response']['items'][i]['sizes'][max_]['width']
            url = eee['response']['items'][i]['sizes'][max_]['url']


            links.append(url)



    links = set(links)


    print(f'''{inc("INF")} Количество полученных ссылок: {len(links)}''')


    try:
        with open(f"{links_file_name}", "w") as outfile:
            json.dump(list(links), outfile, indent=4)
        print(f'''{green}[.] Файл {links_file_name} был успешно создан.''')
    except:
        print(f'''{inc("!")} Файл {links_file_name} НЕ был создан!''')
    print(f'''{white}{'='*10}- DONE -{'='*10}''')

if __name__ == '__main__':
    main()

    ch = 'Y'
    while ch != 'N':
        ch = input('Скачать новую ссылку? (Y/N) >>> ')
        if ch == 'Y':
            main()