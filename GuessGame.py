import random
print('welcome to the game ')
lvl = int(input('enter the level: ' ))
numToGuess = random.randint(0,lvl*50)
print(f'range is between 0 to {lvl*50} ')
score = 10
# print(f'the number is {numToGuess}')
print(f'start guessing the number you have 10 chances')
GuessedNum = int(input('what is your first guess : '))
if GuessedNum == numToGuess :
    print('you have guessed in the first go')
    print(f'you have scored {score} points')
#    score = 10
else :
    while GuessedNum != numToGuess  and score > 0:
        if GuessedNum > numToGuess :
            print('too big ')
        else :
            print('too small')
        score = score - 1
        if score == 0 :
            print('you have lost the game')
            break
        GuessedNum = int(input(' enter your guess '))

    print(f'your score is {score}')


