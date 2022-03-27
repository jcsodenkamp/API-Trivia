

import time
import sys

name = input('To play this game please enter you name? ')
print(
    f'\nHello {name} and welcome to 2000\'s Music Trivia: Which Singer Am I?\n')
print('In order to win you must correclty answer 7 our of 10 questions to win.\n')

time.sleep(4)


answer = input('Are you ready to play? Enter: Yes or No? ')
if answer.lower().startswith('y'):
    print('\nOk, let\'s get started\n')
elif answer.lower().startswith('y') != 'y' or answer.lower().startswith('n') != 'n':
    print('Goodbye')
    sys.exit()
elif answer.lower().startswith('n'):
    print('Goodbye')
    sys.exit()

time.sleep(2)

# Trivia question pulled from https://www.funtrivia.com/quizzes/music/music_by_year/2000s_music.html
questions = {
    'I am a young female soul/R&B singer and songwriter who became the best-selling R&B artist in 2001. My debut album, "Songs In A Minor", was an instant success and catapulted me to fame. What is my name?': ['a. Kandi Burrus', 'b. Alicia Keys', 'c. Lauryn Hill', 'd. Queen Latifah', 'b'],
    'I cannot remember my name, but I know that I started out as a member of The Mickey Mouse Club. I contributed a song, "Reflection", to the soundtrack of Disney film "Mulan", and have created several fragrances. Who am I?': ['a. Linda Perry', 'b. Mariah Carey', 'c. Samantha Mumba', 'd. Christina Aguilera', 'd'],
    'I have been told my real name is very extravagant. My brother Rollo is a member of British electronica band Faithless, and he has helped produce my own albums. A sample of one of my songs was used on Eminem\'s song: Stan. Which singer am I?': ['a, Dido', 'b. Sister Bliss', 'c. Ricky Martin', 'd. Sarah McLachian', 'a'],
    'I am a pop-rock chick, and released my first album when I was only 17. I have appeared in films such as "Over The Hedge" and "Fast-Food Nation". I thought I had found my "Sk8er Boi" in punk singer Deryck Whibley, but it wasn\'t to be. Who am I?': ['a, Avril Lavigne', 'b. Abbey Dawn', 'c. Britney Spears', 'd, Shania Twain', 'a'],
    'I was relatively unknown until the release of my second album, which I did under a new name. I became famous for songs such as "I Kissed A Girl" and "Hot N Cold", but I can\'t remember my adopted stage name! What is it?': ['a. Madonna', 'b. Katy Perry', 'c. Lily Allen', 'd. Cheryl Cole', 'b'],
    'I had many hits with a well-known American boyband before going solo. I am famous for my hits such as "SexyBack" and I once had a relationship with Britney Spears. I\'d like to remember my name - can you tell me what it is?': ['a. JC Chasez', 'b. Curtis Jackson', 'c. Lance Bass', 'd. Justin Timberlake', 'd'],
    'I have a very colorful stage name. I am famous for songs such as "Get The Party Started" and "Stupid Girls", and was one of the singers on the 2001 hit "Lady Marmalade". I can\'t remember my name, but can you?': ['a. Blu Cantrell', 'b. Maroon 5', 'c. Green Day', 'd. Pink', 'd'],
    'I auditioned for British talent show "The X Factor" twice, winning the show in its fifth series in 2008. My mother is famous musically. My songs include a cover of Leonard Cohen\'s "Hallelujah", and "Bad Boys" featuring Flo Rida. Who am I?': ['a. Diana Vickers', 'b. Leona Lewis', 'c. Alexandra Burke', 'd. Eoghan Quigg', 'b'],
    'I don\'t know my name! I thought it was Hannah Montana, until someone told me that that\'s the character I play on the TV show of the same name! My father is well-known for his song "Achy Breaky Heart". My songs include "Best of Both Worlds" and "The Climb". What\'s my name?': ['a. Hilary Duff', 'b. Dolly Parton', 'c. Joe Jonas', 'd. Miley Cyrus', 'd'],
    'How could anyone talk about 2000s singers and not include me? I cannot recall my stage nickname, but I know that I am one of the greatest pop singers the decade has ever produced! Just listen to my hits such as "Poker Face" and "Paparazzi", and who could forget "Bad Romance"? Before I was releasing songs myself, I was behind the scenes writing hits for other famous singers such as Britney Spears and The Pussycat Dolls. Who am I?': ['a. Gwen Stefani', 'b. Akon', 'c. Lady Gaga', 'd. Amy Winehouse', 'c']
}

score = 0
for question_number, question in enumerate(questions):
    print('Question', question_number+1)
    print(question)
    for options in questions[question][:-1]:
        print(options)
    user_choice = input('\nMake your choice: ')
    if user_choice == questions[question][-1]:
        print('\nCorrect!\n')
        score += 1
    else:
        print(
            f'\nSorry that is incorrect, the correct answer was: {questions[question][-1]}\n')


if score >= 7:
    print(f'Your final score is {score} out of 10 you win')
else:
    print(f'Your final score was {score} out of 10 better luck next time')
