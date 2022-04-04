from jsgame_pkg import api_trivia, trivia, game_def


print('\nWelcome all!!')

while True:
    game_def.main_menu()
    option = input('\nPlease make a selection: ').lower()
    if option == '1' or option.startswith('t'):
        api_trivia.api_triva()
    elif option == '2' or option.startswith('20'):
        trivia.music_tivia()
    elif option == '3' or option.startswith('e'):
        break
    else:
        print('Invalid selection ')
