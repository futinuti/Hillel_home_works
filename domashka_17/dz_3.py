def update_hero(**parameters):
    with open('hero.ini', 'r+') as file:
        list_parameters = []
        text = file.readlines()

        for line in text:
            line = line.replace('\n', '')
            list_parameters.append(line.split('='))

        data_ini = dict(map(lambda x: (x[0], x[1]), list_parameters))

        data_ini.update(parameters)

    with open('hero.ini', 'w') as file:
        for new_parametr in data_ini.items():
            line_new = str(new_parametr[0])+'='+str(new_parametr[1]) + '\n'
            file.write(line_new)


update_hero(hero="Halk", power=450, Y=2.3)
