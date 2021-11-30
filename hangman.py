import random

name = input("Enter your name : ")

print(f"Good Luck! {name}")

words = ['rainbow', 'computer', 'science', 'programming',
        'python', 'mathematics', 'player', 'condition',
        'reverse', 'water', 'board', 'garden', 'football', 'gaming', 'tennis', 'fire', 'ice', 'thor', 'birthday', 'captain', 'tolerate']

word = random.choice(words)

print("Guess the characters of the word!")

guesses = ''
turns = 12

while turns > 0 :
    failed = 0

    for char in word :
        if char in guesses :
            print(char)
        else :
            print('_')
            failed += 1

    if failed == 0 :
        print('You Win, Congratulations!')
        break
    
    guess = input("Guess the character : ")

    guesses += guess

    if guess not in word :
        turns -= 1
        print('Wrong')
        print(f'You have {turns} guesses left')

        if turns == 0 :
            print('You Lose, Better luck next time!')