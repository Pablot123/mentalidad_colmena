def coding(message_to_encode):
    coded_message_list =[]
    for char in message_to_encode:
        if char.isdigit():
            int_char = int(char)
            if int_char == 5:
                coded_message_list.append(str(0))
            elif int_char ==0:
                coded_message_list.append(str(5))
            else:
                coded_message_list.append(str(10-int_char))
        else:
            coded_message_list.append(char)
    coded_message_str = ''.join(coded_message_list)        
    return coded_message_str
    
def decoding(coded_message):
    decoded_message_list =[]
    for char in coded_message:
        if char.isdigit():
            int_char = int(char)
            if int_char == 5:
                decoded_message_list.append(str(0))
            elif int_char ==0:
                decoded_message_list.append(str(5))
            else:
                decoded_message_list.append(str(abs(int_char-10)))
        else:
            decoded_message_list.append(char)
    decoded_message_str = ''.join(decoded_message_list)        
    return decoded_message_str

def menu(menu_chosen_option):
    menu_principal = '''
    Select an option:
    1. Encoding message
    2. Decoding message
    3. Exit
    '''
    menu_secundario = '''
    1. Main menu
    2. Exit
    '''

flag = True
while flag:
    menu = '''
    Select an option:
    1. Encoding message
    2. Decoding message
    3. Exit
    '''
    print(menu)
    chosen_option = int(input('Option number: '))
    if chosen_option ==1:
        message = input('Enter the message to encode: ')
        encoded_message = coding(message)
        print(encoded_message)
    elif chosen_option ==2:
        cod_message = input('Enter the message to decode: ')
        decoded_message=decoding(cod_message)
        print(decoded_message)
    elif chosen_option ==3:
        flag = False
    else:
        print('¡¡¡WRONG OPTION, enter a value between 1-3!!! ')


