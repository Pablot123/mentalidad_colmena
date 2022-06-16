import os
from tkinter import N

path = rf'{os.getcwd()}' 
def cleaning_text(text):
    '''
    recive an string and clean the text, replacing some characters and deleating
    the white spaces at the begining and the end
    '''
    clean_text =  text.replace('-','').replace('\n','').replace('\t','').replace('•', '').replace('|','')
    clean_text = clean_text.strip()
    if clean_text == '' or clean_text == ' ':
        pass
    else:
        return clean_text

def fix_list(lista):
    '''
    ignore the elements with None 
    '''
    fixed_list = []
    for importance, element in lista:
        if element == None:
            continue
        else:
            fixed_list.append((importance,element))
    return fixed_list

def cleaning_form_data(data):
    '''
    Return a tuple with the importance of each imformation on the forum
    taking the imformation with * as important and the other as not-important
    '''
    tupla_importance_data = []
    for dato in data:
        if '*' in dato:
            tupla_importance_data.append(('important', cleaning_text(dato)))
        else:
            tupla_importance_data.append(('not-important', cleaning_text(dato)))

    return fix_list(tupla_importance_data)    

with open(rf'{path}\required_data_prueba.txt', 'r+', encoding='utf-8') as file:

    list_form_text = file.readlines()

clean_data = cleaning_form_data(list_form_text)

def has_family(family_member):
    if family_member =='Y':
        return True
    elif family_member == 'N':
        return False

def capturing_information():
    information_complete = False
    while not information_complete:
        mother = input('do you have mother? (y/n): ').upper()
        has_mother = has_family(mother)
        father = input('do you have father? (y/n): ').upper()
        has_father = has_family(father)
        brother = input('do you have brother? (y/n): ').upper()
        has_brother = has_family(brother)
        sister = input('do you have sister? (y/n): ').upper()
        has_sister = has_family(sister)

        #Puse varios if, en vez de elif ya que puede que ocurran varios errores al tiempo
        mom_ok, dad_ok, bro_ok, sis_ok = False, False, False, False
        if(mother != 'Y' and mother !='N'):
            print('Ups! Mother information is wrong')
        else:
            mom_ok = True

        if(father!= 'Y' and father !='N'):
            print('Ups! Father information is wrong')
        else:
            dad_ok = True

        if(brother!= 'Y' and brother !='N'):
            print('Ups! Brother information is wrong')
        else:
            bro_ok = True

        if(sister!= 'Y' and sister !='N'):
            print('Ups! Sister information is wrong')
        else:
            sis_ok = True

        if(mom_ok and bro_ok and dad_ok and sis_ok):
            information_complete = True
        else:
            print('There is missing infomation, please try again')
    return has_mother, has_father, has_brother, has_sister
        

has_mom, has_dad, has_bro, has_sis = capturing_information()

#dividir el array entre informacion personal y de la familia, subdividiendo el de la familia entre 
#cada uno de los miembros