def accept_user_input():
    temp_user_input = input()
    list_temp_user_input = temp_user_input.split(' ')

    if len(list_temp_user_input) == 3:
        list_temp_user_input[1] = list_temp_user_input[1].lower()

        if list_temp_user_input[1] == 'rel':
            return list_temp_user_input
        else:
            list_temp_user_input[1] = list_temp_user_input[1].replace('major', 'ionian')
            list_temp_user_input[1] = list_temp_user_input[1].replace('minor', 'aeolian')
            return list_temp_user_input

    if len(list_temp_user_input) == 2:
        return list_temp_user_input
    if list_temp_user_input[0] in ['modes', 'exit']:
        return list_temp_user_input

    else:
        list_temp_user_input = ["Invalid Instruction"]
        return list_temp_user_input


def check_user_input(user_input, keys, modes):
    if user_input[0] not in keys:
        print('Invalid Key\n')
        return False
    if user_input[1] not in modes and user_input[1] != 'rel':
        print('Invalid Mode/Command\n')
        return False
    if len(user_input) == 3:
        if user_input[1] == 'rel' and user_input[2] not in ['major', 'minor']:
            print('Input after rel should be major or minor\n')
            return False
        if user_input[1] != 'rel' and user_input[2] not in ['#', '##', 'b', 'bb']:
            print('# or b Required as the last input\n')
            return False
    return True


def cl_option_output(user_input, modes, cl_option_list):
    index = cl_option_list.index(user_input)

    match index:
        case 0:
            print(f'{user_input}\n')
        case 1:
            print(*modes, sep='\n')
            print()
        case default:
            print("\n>?<\nsomething went wrong..\nplease try again >w<\n")
    return None
