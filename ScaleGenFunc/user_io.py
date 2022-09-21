def accept_user_input():
    temp_user_input = input()
    list_temp_user_input = temp_user_input.split(' ')

    len_list_ui = len(list_temp_user_input)

    if len_list_ui == 3:
        list_temp_user_input[1] = list_temp_user_input[1].lower()

        if list_temp_user_input[1] == 'rel':
            return list_temp_user_input
        else:
            list_temp_user_input[1] = list_temp_user_input[1].replace('major', 'ionian')
            list_temp_user_input[1] = list_temp_user_input[1].replace('minor', 'aeolian')
            return list_temp_user_input

    if len_list_ui == 2:
        list_temp_user_input[1] = list_temp_user_input[1].lower()
        return list_temp_user_input

    if len_list_ui == 1:
        if list_temp_user_input[0] in ['modes', 'exit']:
            return list_temp_user_input

    list_temp_user_input = ["Invalid Instruction"]
    return list_temp_user_input


def check_user_input(user_input, keys, modes):
    check_list = ['rel', 'major', 'minor']

    if user_input[0] not in keys:
        print('Invalid Key\n')
        return False

    if user_input[1] not in modes and user_input[1] not in check_list:
        print('Invalid Command\n')
        return False

    if len(user_input) == 2:
        match user_input[1]:
            case 'rel':
                print('major or minor Required as the last input\n')
                return False
            case 'major':
                print('#, b, ## or bb Required as the last input\n')
                return False
            case 'minor':
                print('#, b, ## or bb Required as the last input\n')
                return False
        if user_input[1] in modes:
            print('#, b, ## or bb Required as the last input\n')
            return False

    if len(user_input) == 3:
        if user_input[1] == 'rel' and user_input[2] not in ['major', 'minor']:
            print('Input after rel should be major or minor\n')
            return False

        if user_input[1] != 'rel' and user_input[2] not in ['#', '##', 'b', 'bb']:
            print('#, b, ## or bb Required as the last input\n')
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
