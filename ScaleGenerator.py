from ScaleGenFunc import user_io
from ScaleGenFunc import gen

flat_keys = ('A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab')
all_flat_keys = ('A', 'Bb', 'Cb', 'C', 'Db', 'D', 'Eb', 'Fb', 'F', 'Gb', 'G', 'Ab')

sharp_keys = ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#')
all_sharp_keys = ('A', 'A#', 'B', 'B#', 'C#', 'D', 'D#', 'E', 'E#', 'F#', 'G', 'G#')

all_keys = (
    'A', 'A#', 'Ab', 'B', 'B#', 'Bb', 'C', 'C#', 'Cb', 'D', 'D#', 'Db', 'E', 'E#', 'Eb', 'F', 'F#', 'Fb', 'G', 'G#',
    'Gb')

modes = ('ionian', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian', 'locrian')
mode_sequence = (2, 2, 1, 2, 2, 2, 1)

cl_option_list = ('Invalid Instruction', 'modes')

print('''Key Mode Scale_Type:    Ab Locrian #
                        C lydian b
                        Bb minor ##   --to get the scale you want for Key.
                        
                        ##, bb will make notes #,b wherever possible:
                        For example D cannot be # or b of another note:
                        C##, Ebb is just stupid.
                        
Key rel major:          F# rel minor
    rel minor:          G rel major
                        Eb rel minor  --to get the relative minor of Key.
                        
          
You can enter "exit" to stop the code and "modes" to get a list of them(incase you forgot)

Note: Keys are case sensitive (lower cases are reserved for further features), modes are not.''')

flag = True
while flag:
    user_input = user_io.accept_user_input()

    if user_input[0] == 'exit':
        break
    if user_input[0] in cl_option_list:
        user_io.cl_option_output(user_input[0], modes, cl_option_list)
        continue

    if user_io.check_user_input(user_input, all_keys, modes):

        if user_input[1] == 'rel':
            match user_input[2]:
                case 'major':
                    rel_key_mode_sequence = gen.generate_mode_sequence('aeolian', modes, mode_sequence)
                    rel_generated_scale = gen.generate_scale(user_input, sharp_keys, flat_keys,
                                                            all_sharp_keys, all_flat_keys,
                                                            rel_key_mode_sequence)
                    rel = gen.generate_relative_major(rel_generated_scale)
                    print(f'{rel}\n')
                case 'minor':
                    rel_key_mode_sequence = gen.generate_mode_sequence('ionian', modes, mode_sequence)
                    rel_generated_scale = gen.generate_scale(user_input, sharp_keys, flat_keys,
                                                             all_sharp_keys, all_flat_keys,
                                                             rel_key_mode_sequence)
                    rel = gen.generate_relative_minor(rel_generated_scale)
                    print(f'{rel}\n')

        if user_input[1] in modes:
            generated_mode_sequence = gen.generate_mode_sequence(user_input[1], modes, mode_sequence)

            generated_scale = gen.generate_scale(user_input, sharp_keys, flat_keys,
                                                 all_sharp_keys, all_flat_keys,
                                                 generated_mode_sequence)
            print(*generated_scale, sep=' ')
            print()
