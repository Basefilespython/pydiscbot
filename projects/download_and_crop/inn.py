import requests
import json


black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"



def d1(data):
        if list(data.keys())[0] == 'add' or list(data.keys())[1] == 'add':qq = f'{violet}[/] Было добавлено '
        if '17' in list(data["add"].keys()):qq = qq + f'{len(list(data["add"]["17"]))} ссылок в imgs'
        if len(list(data["add"].keys())) == 2:
            qq = qq + ' и было добавлено '
            if '18' in list(data["add"].keys()):qq = qq + f'{len(list(data["add"]["18"]))} ссылок в imgs18.'
        else:
            if '18' in list(data["add"].keys()):qq = qq + f'{len(list(data["add"]["18"]))} из imgs18'
            qq = qq + '.'
        return qq




def d2(data):
        if list(data.keys())[0] == 'del' or list(data.keys())[1] == 'del':
            qq = f'{violet}[/] Было удалено '
        if '17' in list(data["del"].keys()):qq = qq + f'{len(list(data["del"]["17"]))} ссылок из imgs'
        if len(list(data["del"].keys())) == 2:
            qq = qq + ' и было удалено '
            if '18' in list(data["del"].keys()):qq = qq + f'{len(list(data["del"]["18"]))} ссылок из imgs18.'
        else:
            if '18' in list(data["del"].keys()):qq =  qq + f'{len(list(data["del"]["18"]))} ссылок из imgs18'
            qq = qq + '.'
        return qq



def Getting_innovations(data=None):
    if data == None:
        try:
            data = json.loads(requests.get('https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/ver/innovations.json').text)["innv"]
        except requests.exceptions.ConnectionError as err_code:

            errs = err_code
            if "[Errno 11001]" in str(err_code):
                errs = 'You are not connected to the Internet'
            data = None
            
    else:
        data= dict(data)["innv"]

    if data is not None:
        text = ''
        try:text = text + d1(data) + '\n' + d2(data) + white
        except Exception as err:print(err)
    else:return f'{red}[!] Cause: You are not connected to the Internet.{white}'
         
        

    if text == '':return f'{red}[-] Failed: Innovation output failure.{white}'
    return text


