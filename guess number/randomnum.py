import random
ranNum=random.randint(1,10)
guess=0
while True:
    userNum=input('enter your number ')
    if int(userNum)>ranNum:
        print('Guess a lower number')
        guess=guess+1
    elif int(userNum)<ranNum:
        print('Guess a higher number')
        guess=guess+1
    else :
        print('You guessed the number in '+str(guess)+' moves')
        break
