import os
path = rf'{os.getcwd()}' 
def cleaning_text(text):
    '''
    Clean the text, replacing some characters and deleating
    the white spaces at the begining and the end.

    recieves: an string 
    Return: An String without come special characters
    '''
    clean_text =  text.replace('-','').replace('\n','').replace('\t','').replace('•', '').replace('|','').replace(':','')
    clean_text = clean_text.strip()
    if clean_text == '' or clean_text == ' ':
        pass
    else:
        return clean_text

def fix_list(lista):
    '''
    ignore the elements with None 
    Recieves: List of elements
    Returns: List of elements without 'None' elementes
    '''
    fixed_list = []
    for element in lista:
        if element == None:
            continue
        else:
            fixed_list.append(element)
    return fixed_list

def cleaning_form_data(data):
    '''
    Proccess the data and clean the strings
    Recieve: A list of strings
    Return: A list of cleaned data
    '''
    list_importance_data = []
    for dato in data:
        list_importance_data.append(cleaning_text(dato))

    return fix_list(list_importance_data)    

def organice_information(all_data):
    '''
    Organice the data in a dictionary
    Recieve: All the cleaned data
    Return: a dictionary in wich each key is a section of the requiered_data file
    '''
    organiced_info = {'personal_info':[], 'family_info':{'mother':[], 'father':[],
                     'brother':[], 'sister':[]} }
    
    #I use slicing to take the information required by each section
    #The +1 is to only take the information required
    personal_data = all_data[all_data.index('Personal data')+1:all_data.index('Family data')] 
    family_data_mother = all_data[all_data.index('Mother')+1:all_data.index('Father')]
    family_data_father = all_data[all_data.index('Father')+1:all_data.index('Brother')]
    family_data_brother = all_data[all_data.index('Brother')+1:all_data.index('Sister')]
    family_data_sister = all_data[all_data.index('Sister')+1:]

    #Add the information to a dictionary
    organiced_info['personal_info'] = personal_data
    organiced_info['family_info']['mother'] = family_data_mother
    organiced_info['family_info']['father'] = family_data_father
    organiced_info['family_info']['brother'] = family_data_brother
    organiced_info['family_info']['sister'] = family_data_sister
    
    return organiced_info

def has_family(family_member):
    '''
    Used to know if the applicant has member family
    recieve: a string
    Return : A boolean
    '''
    if family_member =='Y':
        return True
    elif family_member == 'N':
        return False

def family_members():
    '''
    Ask the user if he has mother, father, brother or sister
    Return: a tuple of 4 boolean in the same order describer above
    '''
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
        

def capturing_information(dict_form):
    '''
    take all the information of the user in the required_data file
    Recive: a dictionary where each key is a section of the form and each value 
            is a required data
    return: a dictionary where each key is a section of the required data and ech value
            is a list of tuples with (required_data, data given by the user)
    '''
    dict_filled_information = {}
    
    personal_info = []
    family_info_mother = []
    family_info_father = []
    family_info_brother = []
    family_info_sister = []
    has_mom, has_dad, has_bro, has_sis = family_members()
    print('Please enter the following personal information:')
    for personal in dict_form['personal_info']:
        info = input(f'{personal}: ')
        if info == '' and '*' in personal: #if the information is empty and the required info has a '*' we fill that info with 'unknow'
            personal_info.append((personal,'unknow'))
        else:
            personal_info.append((personal,info))
    if has_mom:
        print('Mother information'.center(50,'-'))
        for mother in dict_form['family_info']['mother']:
            info = input(f'{mother}: ')
            #if the information is empty and the required info has a '*' we fill that info with 'unknow'
            if info == '' and '*' in mother:
                family_info_mother.append((mother,'unknow'))
            else:
                family_info_mother.append((mother, info))
    else:
        #if the applicant dosen´t have the family member we fill all the data with None
        for mother in dict_form['family_info']['mother']:
            family_info_mother.append((mother,'None'))
    
    if has_dad:
        print('Father information'.center(50,'-'))
        for father in dict_form['family_info']['father']:
            info = input(f'{father}: ') 
            #if the information is empty and the required info has a '*' we fill that info with 'unknow'
            if info == '' and '*' in father:
                family_info_father.append((father, 'unknow'))
            else:
                family_info_father.append((father, info))
    else:
        #if the applicant dosen´t have the family member we fill all the data with None
        for father in dict_form['family_info']['father']:
            family_info_father.append((father, 'None'))


    if has_bro:
        print('Brother information'.center(50,'-'))
        for brother in dict_form['family_info']['brother']:
            info = input(f'{brother}: ')
            #if the information is empty and the required info has a '*' we fill that info with 'unknow'
            if info == '' and '*' in brother:
                family_info_brother.append((brother, 'unknow'))
            else:
                family_info_brother.append((brother, info))
    else:
        #if the applicant dosen´t have the family member we fill all the data with None
        for brother in dict_form['family_info']['brother']:
            family_info_brother.append((brother, 'None'))
    
    if has_sis:
        print('Sister information'.center(50,'-'))
        for sister in dict_form['family_info']['brother']:
            info = input(f'{sister}: ')
            #if the information is empty and the required info has a '*' we fill that info with 'unknow'
            if info == '' and '*' in sister:
                family_info_sister.append((sister, 'unknow'))
            else:
                family_info_sister.append((sister, info))
    else:
        #if the applicant dosen´t have the family member we fill all the data with None
        for sister in dict_form['family_info']['brother']:
            family_info_sister.append((sister, 'None'))
    
    #Adding all the captured information in a dictionary
    dict_filled_information['personal'] = personal_info
    dict_filled_information['fam_mom'] = family_info_mother
    dict_filled_information['fam_dad'] = family_info_father
    dict_filled_information['fam_bro'] = family_info_brother
    dict_filled_information['fam_sis'] = family_info_sister
    return dict_filled_information

def fill_ubication(line, personal_data, mother_data, father_data, brother_data, sister_data):
    '''
    To know in wich part of the required_data file is the writing prograam
    Recieve: a Line of the file and 5 boolean initialiced
    Return: a tuple of 5 boolean Where only one is 'True' and indicates in wich part of the file
            if filling the information
    '''
    if 'Personal data' in line:
        personal_data = True
        mother_data = False
        father_data = False
        brother_data = False
        sister_data = False
    
    elif 'Mother' in line:
        personal_data = False
        mother_data = True
        father_data = False
        brother_data = False
        sister_data = False

    elif 'Father' in line:
        personal_data = False
        mother_data = False
        father_data = True
        brother_data = False
        sister_data = False
    elif 'Brother' in line:
        personal_data = False
        mother_data = False
        father_data = False
        brother_data = True
        sister_data = False
    elif 'Sister' in line:
        personal_data = False
        mother_data = False
        father_data = False
        brother_data = False
        sister_data = True
    else:
        pass
    
    return personal_data, mother_data, father_data, brother_data, sister_data

with open(rf'{path}\required_data.txt', 'r', encoding='utf-8') as file:

    list_form_text = file.readlines() 

clean_data = cleaning_form_data(list_form_text) #Clean data
organiced_data = organice_information(clean_data)#Organice information

full_information_filled = capturing_information(organiced_data)# fill the information previulsy organiced

name = full_information_filled['personal'][0][1] #Name of the applicant to use as name of the new file
per_section = '''
 -----------------------------------------------------------
|                     Personal data                         |
 -----------------------------------------------------------
'''
fam_section = '''
 -----------------------------------------------------------
|                       Family data                         |
 -----------------------------------------------------------
'''
with open(rf'{path}\required_data.txt', 'r') as f:
    with open(rf'{path}\{name}_required_data.txt', 'a') as out:
        personal_section, mom_section, dad_section, bro_section, sis_section = False, False, False, False, False 
        p,m,d,b,s = True, True, True, True, True # to control the text that are only write once
        for line in f:
            #To know in wich section of the file we are, personal information section, mother information section
            # father information section, etc...
            personal_section, mom_section, dad_section, bro_section, sis_section = fill_ubication(line, personal_section, mom_section, dad_section, bro_section, sis_section)
            
            if personal_section:
                if p: # this conditional is to write at the begining of teh section only once
                    print(per_section, file=out)
                    p=False
                #Taking the data from the dict, it came as a list of tuples (required info, data)
                # ex, ('Full name*', 'Pablo tamayo')
                for item, data in full_information_filled['personal']: 
                    if item in line: # to match the information asked withe the data
                        item_line = line.strip('\n')
                        print(item_line, data, file=out) #adding the required data + data to the new file
                    else:
                        pass
            elif mom_section:
                if m:# this conditional is to write at the begining of teh section only once
                    print(fam_section, file=out)
                    print('• Mother:', file=out)
                    m=False
                #Taking the data from the dict, it came as a list of tuples (required info, data)
                # ex: ('Full name*', 'Pablo tamayo')
                for item, data in full_information_filled['fam_mom']: 
                    if item in line: # to match the information asked withe the data
                        item_line = line.strip('\n')
                        print(item_line, data, file=out)#adding the required data + data to the new file
                    else:
                        pass
            elif dad_section:
                if d:# this conditional is to write at the begining of teh section only once
                    print('', file=out)
                    print('• Father:', file=out)
                    d=False
                #Taking the data from the dict, it came as a list of tuples (required info, data)
                # ex: ('Full name*', 'Pablo tamayo')
                for item, data in full_information_filled['fam_dad']:
                    if item in line: # to match the information asked withe the data
                        item_line = line.strip('\n')
                        print(item_line, data, file=out) #adding the required data + data to the new file
                    else:
                        pass
            elif bro_section:
                if b:# this conditional is to write at the begining of teh section only once
                    print('', file=out)
                    print('• Brother:', file=out)
                    b=False
                #Taking the data from the dict, it came as a list of tuples (required info, data)
                # ex, ('Full name*', 'Pablo tamayo')
                for item, data in full_information_filled['fam_bro']:
                    if item in line: # to match the information asked withe the data
                        item_line = line.strip('\n')
                        print(item_line, data, file=out) #adding the required data + data to the new file
                    else:
                        pass
            elif sis_section:
                if s:# this conditional is to write at the begining of teh section only once
                    print('', file=out)
                    print('• Sister:', file=out)
                    s = False
                #Taking the data from the dict, it came as a list of tuples (required info, data)
                # ex, ('Full name*', 'Pablo tamayo')
                for item, data in full_information_filled['fam_sis']:
                    if item in line: # to match the information asked withe the data
                        item_line = line.strip('\n')
                        print(item_line, data, file=out) #adding the required data + data to the new file
                    else:
                        pass