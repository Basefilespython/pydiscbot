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



def tt(data=None):
    if data == None:
        data = json.loads(requests.get('https://raw.githubusercontent.com/Basefilespython/pydiscbot/main/projects/download_and_crop/ver/innovations.json').text)["innv"]
    else:
         data= dict(data)["innv"]
    #data = '''{'add': {'imgs': ['TEST1']}, 'del': {'imgs18': ['TEST4']}}'''
    

    print(data, list(data.keys()))
    
    text = ''
    if 'add' in list(data.keys()):
        ee = 'Было добавлено '
        if '17' in list(data["add"].keys()):
            #try:
                ee = ee + f'{len(list(data["add"]["17"]))} из imgs'
            #except:pass
        if len(list(data["add"].keys())) == 2:
            ee = ee + ' и было добавлено '
            if '18' in list(data["add"].keys()):
                ee = ee + f'{len(list(data["add"]["18"]))} из imgs18.'
        else:
            #if 'imgs' in list(data["add"].keys()):ee = ee + f'{len(list(data["add"]["imgs"]))} в imgs.'
            if '18' in list(data["add"].keys()):ee = ee + f'{len(list(data["add"]["imgs18"]))} в imgs18.'

            ee = ee + '.'
        text = text + ee
    else:
        return f'{red}[-] Failed: Innovation output failure.'

    if 'del' in list(data.keys()):
        ee = 'Было удалено '
        if '17' in list(data["del"].keys()):
            #try:
                ee = ee + f'{len(list(data["del"]["17"]))} из imgs'
            #except:pass
        if len(list(data["del"].keys())) == 2:
            ee = ee + ' и было удалено '
            if '18' in list(data["del"].keys()):
                ee = ee + f'{len(list(data["del"]["18"]))} из imgs18.'
        else:
            #if '17' in list(data["del"].keys()):ee = ee + f'{len(list(data["del"]["imgs"]))} из imgs.'
            if '18' in list(data["del"].keys()):ee = ee + f'{len(list(data["del"]["18"]))} из imgs18'

            ee = ee + '.'
        print(ee)
    else:
        return f'{red}[-] Failed: Innovation output failure.'
    return text







# qw = {
#     "innv": {
#         "add": {
#             "17": [
#                 "TEST1"
#             ],
#             "18": [
#                 "TEST2"
#             ]
#         },
#         "del": {
#             "17": [
#                 "TEST3"
#             ],
#             "18": [
#                 "TEST4"
#             ]
#         }
#     }
# }

# qw = {
#     "innv": {
#         "add": {
#             "imgs": [
#                 "TEST1"
#             ]
            
#         },
#         "del": {
            
#             "imgs18": [
#                 "TEST4"
#             ]
#         }
#     }
# }
tt()


# tt()
