from jsgame_pkg import api_trivia, trivia, game_def
import sys

cur_player = ''
# scores = [] < ---- couldnt figure out how to keep score with multiple users

while True:

    while True:
        game_def.user_menu()
        option = input('Please make a selection: ')
        if option == '1':
            cur_player = game_def.new_user()
            if cur_player == None:
                continue
            break

        elif option == '2':
            cur_player = game_def.login()
            if cur_player == None:
                continue
            break

        elif option == '3':
            if cur_player == '':
                print('\nYou must be registered or logged in to play!\n ')
            else:
                game_def.game_menu()

        elif option == '4':
            game_def.exit_game()

        # Was not able to get this to work for 1 game let alone two.
        # elif option == '5':
        #     game_def.show_scores(scores)

        else:
            print('Invalid Selection. ')

    while True:
        game_def.game_menu()
        option = input('\nMake a selection: ').lower()
        if option == '1' or option.startswith('t'):
            api_trivia.api_triva()
        elif option == '2' or option.startswith('20'):
            trivia.music_tivia()
        elif option == '3' or option.startswith('e'):
            break
        else:
            print("\n\033[31m" + 'Invalid selection' + "\033[0m\n")
