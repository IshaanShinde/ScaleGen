def generate_mode_sequence(user_input, modes, mode_sequence):
    index = modes.index(user_input)
    temp_list = []
    i = index
    while i in range(0, len(modes)):
        temp_list.append(mode_sequence[i])
        i = (i + 1) % len(mode_sequence)
        if i == index:
            break
    return temp_list


def make_temp_scale(user_input, sharp_keys, flat_keys, all_sharp_keys, all_flat_keys):
    temp_list = []
    scale_type = user_input[2]
    match scale_type:
        case 'b':
            temp_list = flat_keys * 2
        case '#':
            temp_list = sharp_keys * 2
        case 'bb':
            temp_list = all_flat_keys * 2
        case '##':
            temp_list = all_sharp_keys * 2
    return temp_list


def find_index(user_input, sharp_keys, all_sharp_keys, all_flat_keys):
    key = user_input[0]
    key_len = len(key)
    key_index = 0
    match key_len:
        case 1:
            key_index = sharp_keys.index(key)
        case 2:
            match key[1]:
                case 'b':
                    key_index = all_flat_keys.index(key)
                case '#':
                    key_index = all_sharp_keys.index(key)
    return key_index


def generate_scale(user_input, sharp_keys, flat_keys, all_sharp_keys, all_flat_keys, generated_mode_sequence):
    key_index = find_index(user_input, sharp_keys, all_sharp_keys, all_flat_keys)
    temp_scale = make_temp_scale(user_input, sharp_keys, flat_keys, all_sharp_keys, all_flat_keys)

    generated_scale = []
    i_k = key_index
    for i in range(0, len(generated_mode_sequence)):
        generated_scale.append(temp_scale[i_k])
        i_k += generated_mode_sequence[i]
    generated_scale.append(temp_scale[key_index])
    return generated_scale
