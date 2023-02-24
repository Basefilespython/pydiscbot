def module(inp):
    from os import system
    try:
        import requests
    except ImportError:
        system('pip install requests')
        try:
            import requests
        except ImportError:
            raise ImportError('Внимание!\nМодуль requests не установлен! ')


    def download_from_github(url):
        try:

            def download_file(url):
                local_filename = url.split('/')[-1]
                with requests.get(url, stream=True, allow_redirects=True) as r:
                    r.raise_for_status()
                    with open(local_filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                return local_filename

            download_file(url)
            pass
        except Exception as err:
            print(err)


    def opredelit_materik(inp = None) -> str:
        inp = inp.title()
        try:
            from countryinfo import countries
        except ImportError:
            download_from_github('https://gist.githubusercontent.com/mjrulesamrat/0c1f7de951d3c508fb3a20b4b0b33a98/raw/f5f9db4f1b287804fd07ffb3296ed0036292bc7a/countryinfo.py')
            try:
                from countryinfo import countries
            except Exception:
                raise ImportError('Модуль countryinfo.py успешно загружен!\nПерезагрузите код.')

        qwr= []
        for co in countries:
        
            if len(str(co['timezones']).split(',')) > 1:
                for qw in str(co['timezones']).split(','):
                    

                    if inp in str(qw):
                        qwr.append(qw)

        if len(qwr) == 0:
            print('Ничего не было найдено. Было заменено значение!\n')
            asd = 'Europe/Moscow'
        if len(qwr) > 0:
            asd = ''
            for qer in qwr:
                asd = str(qer).replace("'","").replace("[","").replace("]","").replace(" ","")
            #print(asd)
        return asd
    return opredelit_materik(inp)
#znachenie = module(input('Введите свой город >>>'))

    
#print(f'z: {znachenie}')
