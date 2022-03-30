from pip._vendor import requests
import json
import random
import html
import sys



name = input('\nWhat is your name? ')
print(f'Hello {name}! ')
# https://opentdb.com/api_config.php
while True:
    # Select Difficulty
    print("\n1. Easy ")
    print("2. Medium")
    print("3. Hard ")
    print("4. Quit")
    Option = input("\nSelect Difficulty ")
    if Option == '1' or Option.lower().startswith('e'):
        print("You chose Easy ")
        # Select Category
        while True:
            print("\n1. Sports ")
            print("2. Music ")
            print("3. History ")
            Option = input("Select category ")
            if Option == '1' or Option.lower().startswith('s'):
                print("\nYou chose Sports")
                trivia_url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=easy&type=multiple"
            elif Option == '2' or Option.lower().startswith('m'):
                print('\nYou Chose Music ')
                trivia_url = "https://opentdb.com/api.php?amount=10&category=12&difficulty=easy&type=multiple"
            elif Option == '2' or Option.lower().startswith('m'):
                print('\nYou Chose History ')
                trivia_url = "https://opentdb.com/api.php?amount=10&category=23&difficulty=easy&type=multiple"
            else:
                print('Invalid selection')
            break

    elif Option == '2' or Option.lower().startswith('m'):
        print("You chose Medium ")
        # Select Category
        while True:
            print("\n1. Sports ")
            print("2. Music ")
            print("3. History ")
            Option = input("Select category ")
            if Option == '1' or Option.lower().startswith('s'):
                print("\nYou chose Sports")
                trivia_url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=medium&type=multiple"
            elif Option == '2' or Option.lower().startswith('m'):
                print('\nYou Chose Music ')
                trivia_url = "https://opentdb.com/api.php?amount=10&category=12&difficulty=medium&type=multiple"
            elif Option == '2' or Option.lower().startswith('m'):
                print('\nYou Chose History ')
                trivia_url = "https://opentdb.com/api.php?amount=10&category=23&difficulty=medium&type=multiple"
            else:
                print('Invalid selection')
            break
    elif Option == '3' or Option.lower().startswith('h'):
        print("You chose Hard ")
        # Select Category
        while True:
            print("\n1. Sports ")
            print("2. Music ")
            print("3. History ")
            Option = input("Select category ")
            if Option == '1' or Option.lower().startswith('s'):
                print("\nYou chose Sports")
                trivia_url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=hard&type=multiple"
            elif Option == '2' or Option.lower().startswith('m'):
                print('\nYou Chose Music ')
                trivia_url = "https://opentdb.com/api.php?amount=10&category=12&difficulty=medium&type=multiple"
            elif Option == '2' or Option.lower().startswith('m'):
                print('\nYou Chose History ')
                trivia_url = "https://opentdb.com/api.php?amount=10&category=12&difficulty=hard&type=multiple"
            else:
                print('Invalid selection')
            break
    elif Option == '4' or Option.lower().startswith('q'):
        print(f'Goodbye {name}')
        break
    else:
        print('Invalid selection ')

    trivia_api = requests.get(trivia_url)
    trivia_json = json.loads(trivia_api.content)

    for trivia_question in trivia_json['results']:
        category = trivia_question['category']
        difficulty = trivia_question['difficulty']
        question = trivia_question['question']
        answer = trivia_question['correct_answer']
        choices = trivia_question['incorrect_answers'] + [answer]

        # Remove HTML encodings from question and choices
        question = html.unescape(question)
        choices = [html.unescape(choice) for choice in choices]

        # trivia_json is now a Python dictionary containing 10 random trivia questions requested from the trivia API. The questions can be accessed such as this:
        score = 0
        # randomize the choices
        random.shuffle(choices)
        # Display question and choices
        print(f"{category}\tDifficulty: {difficulty}")
        print(f"\n{question}")
        for index, choice in enumerate(choices):
            print(f"{index}) {choice}")
        user_choice = input('Select your answer ')
        if user_choice == answer:
            print("Correct\n")
            score + 1
        else:
            print("\nSorry that is" + "\033[31m" + " incorrect" +
                  "\033[0m" + ", the correct answer is: {0}\n".format(answer))
    if score > 7:
        print(f'Your final score is {score} out of 10 you win')
    else:
        print(
            f'Your final score was {score} out of 10, better luck next time.')

    play_again = input("\nIf you would like to play again, please type:" +
                       "\033[32m" + " Yes" + "\033[0m" + " or" + "\033[31m" + " No: " + "\033[0m")
    if play_again == 'yes' or play_again.lower().startswith('y'):
        continue
    elif play_again == 'no' or play_again.lower().startswith('n'):
        break
    else:
        print(f'Goodbye {name}, have a great day!')
