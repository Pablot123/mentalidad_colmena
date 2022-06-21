def coding(message_to_encode):
    '''
    Encode a given text
    Recieve: A String with all the message
    Return : A String with the encoded message
    '''
    coded_message_list =[]
    for char in message_to_encode:
        if char.isdigit(): #We only chage the numeric values, the methos isdigit helps whit that
            int_char = int(char)
            #I foun that to encode the numer we only need tu sustract the number to 10, except
            # with 0 and 5
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
    '''
    Decode a message
    Recieve: A String with the encoded message
    Return : A string with the decoded message
    '''
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

def menu():
    menu =  '''
        Select an option:
        1. Encoding message
        2. Decoding message
        3. Exit
        '''
    return menu


def option_control(chosen_option):
    '''
    To control the opcion of the menu
    Recieve: an int with the chosen option from the user
    Return: a Bollean to know if the program continue or not
    '''
    if chosen_option ==1:
        message = input('Enter the message to encode: ')
        encoded_message = coding(message)
        print(f'Encoded Message: {encoded_message}')
        
        return True

    elif chosen_option ==2:
        cod_message = input('Enter the message to decode: ')
        decoded_message=decoding(cod_message)
        print(f'Decoded Message: {decoded_message}')
        return True
        
    elif chosen_option == 3:
        return False
    else:
        print('¡¡¡WRONG OPTION, enter a value between 1-3!!! ')
        return True
    
def main():
    '''
    Run the program
    '''
    flag = True
    while flag:
        print(menu())
        chosen_option = int(input('Option number: '))
        flag = option_control(chosen_option)

main()


