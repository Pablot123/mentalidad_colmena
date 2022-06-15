import os
path = rf'{os.getcwd()}'
with open(rf'{path}\required_data_prueba.txt', 'r', encoding='utf-8') as file:
    #lineas = file.readlines()
    #print(lineas)
    for line in file:
        if 'Personal data' in line:
            datos_personales = True
            print('DATOS PERSONLAES'.center(50,'-'))  
        elif 'Family data' in line:
            print('DATOS FAMILIARES'.center(50,'-'))
            pass
    
