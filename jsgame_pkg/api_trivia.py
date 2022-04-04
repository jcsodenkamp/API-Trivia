from jsgame_pkg import game_def
from pip._vendor import requests
import json
import random
import html
import time


def api_triva():
    name = input('\nWhat is your name? ')
    print(f'\nHello {name}!\nWelcome to API Triva ')
    print('\nGame rules are easy, select a difficulty and category.\nIf you answer 4 out of 10 quesitons incorreclty, the game will end.\nAll questions are multipule choice, do you best and good luck!')

    answer = input("\033[32m" + '\nTap enter on your keyboard when you are ready to play.' + "\033[0m")
  

    if answer.startswith(''):
        print('\nOk, let\'s get started!\n')

    time.sleep(2)
    # https://opentdb.com/api_config.php
    while True:
        # Select Difficulty
        game_def.difficulty()
        Option = input("\nSelect Difficulty ").lower()
        if Option == '1' or Option.startswith('e'):
            print("You chose: Easy ")
            # Select Category
            while True:
                game_def.category()
                Option = input("Select category ").lower()
                if Option == '1' or Option.startswith('s'):
                    print("\nYou chose: Sports")
                    trivia_url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=easy&type=multiple"
                elif Option == '2' or Option.startswith('m'):
                    print('\nYou chose: Music ')
                    trivia_url = "https://opentdb.com/api.php?amount=10&category=12&difficulty=easy&type=multiple"
                elif Option == '3' or Option.startswith('m'):
                    print('\nYou chose: History ')
                    trivia_url = "https://opentdb.com/api.php?amount=10&category=23&difficulty=easy&type=multiple"
                else:
                    print('Invalid selection')
                break

        elif Option == '2' or Option.startswith('m'):
            print("You chose: Medium ")
            # Select Category
            while True:
                game_def.category()
                Option = input("Select category ").lower()
                if Option == '1' or Option.startswith('s'):
                    print("\nYou chose: Sports")
                    trivia_url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=medium&type=multiple"
                elif Option == '2' or Option.startswith('m'):
                    print('\nYou chose: Music ')
                    trivia_url = "https://opentdb.com/api.php?amount=10&category=12&difficulty=medium&type=multiple"
                elif Option == '3' or Option.startswith('m'):
                    print('\nYou chose: History ')
                    trivia_url = "https://opentdb.com/api.php?amount=10&category=23&difficulty=medium&type=multiple"
                else:
                    print('Invalid selection')
                break
        elif Option == '3' or Option.startswith('h'):
            print("You chose: Hard ")
            # Select Category
            while True:
                game_def.category()
                Option = input("Select category ").lower()
                if Option == '1' or Option.startswith('s'):
                    print("\nYou chose: Sports")
                    trivia_url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=hard&type=multiple"
                elif Option == '2' or Option.startswith('m'):
                    print('\nYou chose: Music ')
                    trivia_url = "https://opentdb.com/api.php?amount=10&category=12&difficulty=medium&type=multiple"
                elif Option == '3' or Option.startswith('m'):
                    print('\nYou chose: History ')
                    trivia_url = "https://opentdb.com/api.php?amount=10&category=12&difficulty=hard&type=multiple"
                else:
                    print('Invalid selection')
                break
        elif Option == '4' or Option.startswith('q'):
            print(f'Goodbye {name}')
            break
        else:
            print('Invalid selection ')

        trivia_api = requests.get(trivia_url)
        trivia_json = json.loads(trivia_api.content)
        score = 0
        wrong_score = 0
        for trivia_question in trivia_json['results']:
            category = trivia_question['category']
            difficulty = trivia_question['difficulty']
            question = trivia_question['question']
            answer = trivia_question['correct_answer']
            choices = trivia_question['incorrect_answers'] + [answer]

            # Remove HTML encodings from question and choices
            question = html.unescape(question)
            answer = html.unescape(answer)
            choices = [html.unescape(choice) for choice in choices]

            # trivia_json is now a Python dictionary containing 10 random trivia questions requested from the trivia API. The questions can be accessed such as this:
            # randomize the choices
            random.shuffle(choices)
            # Display question and choices
            answer_map = {'1': choices[0], '2': choices[1],
                          '3': choices[2], '4': choices[3]}

            print(f"{category}\tDifficulty: {difficulty}")
            print(f'Your current score is: {score}')
            print(f"\n{question}")
            print(answer)

            for key, choices in answer_map.items():
                print(f"{key}. {choices}")
            user_choice = input('Select your answer ')

            print(f'You chose: {user_choice}')
            if user_choice == answer or (user_choice in answer_map and answer_map[user_choice] == answer):
                print("Correct\n")
                if difficulty == 'easy':
                    score += 1
                elif difficulty == 'medium':
                    score += 2
                else:
                    score += 3
            else:
                print("\nSorry that is" + "\033[31m" + " incorrect" +
                      "\033[0m" + ", the correct answer is: {0}\n".format(answer))
                wrong_score += 1
                if wrong_score == 4:
                    print('You have answered 4 questions incorrectly')
                    break

        if difficulty == 'easy' and score > 7:
            print(f'Your final score is {score} out of 10 points you win')
        elif difficulty == 'medium' and score > 14:
            print(f'Your final score is {score} out of 20 points you win')
        elif difficulty == 'hard' and score > 21:
            print(f'Your final score is {score} our of 30 points you win')
        else:
            print(
                f'Your final score was {score}, better luck next time.')

        play_again = input("\nIf you would like to play again, please type:" +
                           "\033[32m" + " Y" + "\033[0m" + " or" + "\033[31m" + " N: " + "\033[0m").lower()
        if play_again == 'yes' or play_again.startswith('y'):
            continue
        elif play_again == 'no' or play_again.startswith('n'):
            print(f'Goodbye {name}, have a great day!')
            break
        else:
            print('Invale selection')
