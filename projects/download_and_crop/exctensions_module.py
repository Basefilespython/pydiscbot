import json







def sizing_dict(dict_):
    dict_exctensions = list()
    ur = dict_

    i = 0
    for url in ur:
            
            try:
                qazw = list((ur[i][f'imgs']).keys())
                gif = ur[i][f'imgs'][f"{qazw[0]}"]
                mp4 = ur[i][f'imgs'][f"{qazw[1]}"]
                for url in list(gif):
                  zn = {f'{url}': '.gif'}

                  dict_exctensions.append(zn)  
                for url in list(mp4):
                  zn = {f'{url}': '.mp4'}
                  dict_exctensions.append(zn)  

            except:
                url = url.replace(" ", "%20")
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

                zn = {f'{url}': f'{exten}'}
                dict_exctensions.append(zn)

            i = i + 1
    return dict_exctensions






if __name__ == '__main__':
  pass