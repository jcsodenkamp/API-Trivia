from jsgame_pkg import game_def
from pip._vendor import requests
import json
import random
import html
import time


def api_triva():
    # Welcome and game rules string.
    print(f'\nWelcome to API Triva\n1. Game rules are easy, select a difficulty and category.\n2. If you answer 4 out of 10 quesitons incorreclty, the game will end.\nAll questions are multipule choice, do your best and good luck! ')

    # Will allow user ability to first read the welcome and game rules before moving on.
    answer = input(
        "\033[36m" + '\nTap enter on the keyboard when you are ready to play.' + "\033[0m")

    # Transition pause
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

            # If the user selects an easy difficulty.
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
                elif Option == '4' or Option.startswith('e'):
                    print(f'Goodby ')
                else:
                    print('Invalid selection')
                break

        # Select Difficulty
        elif Option == '2' or Option.startswith('m'):
            print("You chose: Medium ")

            # if the user selects an medium difficulty.
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
                elif Option == '4' or Option.startswith('e'):
                    print(f'Goodby')
                else:
                    print('Invalid selection')
                break

        # Select Difficulty
        elif Option == '3' or Option.startswith('h'):
            print("You chose: Hard ")

            # Select Category is the user selects an hard difficulty.
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
                elif Option == '4' or Option.startswith('e'):
                    print(f'Goodby')
                else:
                    print('Invalid selection')
                break
        # Exit
        elif Option == '4' or Option.startswith('q'):
            print(f'Goodbye')
            # This will break out of this while loop and go back to the game menu.
            break
        # Invalid condition
        else:
            print('Invalid selection ')

        # assigns values for API
        trivia_api = requests.get(trivia_url)
        trivia_json = json.loads(trivia_api.content)

        # Stores user score
        score = 0

        # Stores wrong answers
        wrong_score = 0

        # iterate through API responce_code
        for trivia_question in trivia_json['results']:
            category = trivia_question['category']
            difficulty = trivia_question['difficulty']
            question = trivia_question['question']
            answer = trivia_question['correct_answer']
            choices = trivia_question['incorrect_answers'] + [answer]

            # Remove HTML encodings from question and choices. example: &quot - &&quot
            question = html.unescape(question)
            answer = html.unescape(answer)
            choices = [html.unescape(choice) for choice in choices]

            # trivia_json is now a Python dictionary containing 10 random trivia questions requested from the trivia API. The questions can be accessed such as this:

            # randomize the choices
            random.shuffle(choices)

            # Display question and choices
            answer_map = {'1': choices[0], '2': choices[1],
                          '3': choices[2], '4': choices[3]}
            print(
                "\033[36m"+"+------------------------+-----------------------+"+"\033[0m")
            print(f"{category}\tDifficulty: {difficulty.capitalize()}")
            print(f'Current score: {score}')

            print(f"\n{question}")

            # iterate through answer_map above code
            for key, choices in answer_map.items():
                print(f"{key}. {choices}")

            user_choice = input('\nMake your choice ')

            # shows user they have selected the correct answer.
            print(f'You chose: {user_choice}')
            if user_choice == answer or (user_choice in answer_map and answer_map[user_choice] == answer):
                print(
                    "\033[36m"+"+------------------------+-----------------------+"+"\033[0m")
                print("                  \033[36m"+"=== Correct ==="+"\033[0m")

                # scoring system.
                if difficulty == 'easy':
                    score += 1
                elif difficulty == 'medium':
                    score += 2
                else:
                    score += 3
            # shows user they have incorrectly answered the question.
            else:
                print(
                    "\033[36m"+"+------------------------+-----------------------+"+"\033[0m")
                print("\nSorry that is" + "\033[31m" + " incorrect" +
                      "\033[0m" + ", the correct answer is: {0}\n".format(answer))
                wrong_score += 1

                # when the user has answered 4 questions incorrectly.
                if wrong_score == 4:
                    print('You have answered 4 questions incorrectly')
                    break

        # Once the game has iterated through all question this will be displayed depending on difficulty level.
        if difficulty == 'easy' and score > 7:
            print(f'Your final score is {score} out of 10 points you win\n')
        elif difficulty == 'medium' and score > 14:
            print(f'Your final score is {score} out of 20 points you win\n')
        elif difficulty == 'hard' and score > 21:
            print(f'Your final score is {score} out of 30 points you win\n')
        else:
            print(
                f'Your final score was {score}, better luck next time.\n')
        # Allows user to play again else will loop back to game menu. 
        play_again = input("\nIf you would like to play again, please type:" +
                           "\033[32m" + " Y" + "\033[0m" + " or" + "\033[31m" + " N: " + "\033[0m").lower()
        if play_again == 'yes' or play_again.startswith('y'):
            continue
        elif play_again == 'no' or play_again.startswith('n'):
            print(f'Goodbye, have a great day!')
            break
        # Invalid condition. 
        else:
            print('Invalid selection')
