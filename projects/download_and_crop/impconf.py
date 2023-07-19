import json



def conf(file_name_config, debugVal, autoload_VAL_, py_logger, working_dir_, cls, debDEF):

        conf_file = []
        try:
            with open(f"{file_name_config}", "r") as file:
                data = json.loads(file.read())
                localization = data[0]['localization']
                conf_file.append({'localization': localization})
        except Exception as err:
            print(err)
            if debugVal == False:cls()

            localization = input(f"Выберите локализацию (ru) / Select localization (en) >>> ").upper()


            if (localization != "RU"):
                if (localization != "EN"):localization = "EN"

            zn = str(localization).lower().replace(" ", "")
            conf_file.append({'localization': zn})

        try:
            with open(f"{file_name_config}", "r") as file:
                data = json.loads(file.read())
                working_dir = data[0]['working_dir']
        except:
            if debugVal == False:cls()

            working_dir = working_dir_
            conf_file.append({'working_dir': working_dir})
    

        # with open(f"{file_name_config}", "w") as outfile:
        #     json.dump(conf_file, outfile, indent=4)
        #     debDEF(f"""File created [{file_name_config}]""", debugVal, py_logger, 1)
        

        # try:
        #     with open(f"{file_name_config}", "r") as file:
        #         data = json.loads(file.read())
        #         autoload_VAL = data[0]['autoload_VAL']
        # except:
        if debugVal == False:cls()
            
        autoload_VAL = autoload_VAL_
        conf_file.append({'autoload_VAL': autoload_VAL})
    

        with open(f"{file_name_config}", "w") as outfile:
            json.dump(conf_file, outfile, indent=4)
            debDEF(f"""File created [{file_name_config}]""", debugVal, py_logger, 1)
            
        return localization, working_dir, autoload_VAL
