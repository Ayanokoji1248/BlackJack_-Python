import random


playerCards = []
compCards=[]

isContinue = True

def randomNum():
    return random.randint(1,10)

def playerDrawCard():
    for i in range(2):
        drawCards = randomNum()
        playerCards.append(drawCards)
    print(f"Your cards are {playerCards}")

def compDrawCard():
    for i in range(2):
        drawCards = randomNum()
        compCards.append(drawCards)
    print(f"Comp cards are [{compCards[0]}, _]")


def continueHit():
    hitChoice = input("Do you want to hit? (y/n): ")
    if(hitChoice == "y"):
        additionalNum = randomNum()
        playerCards.append(additionalNum)
        print(f"Your cards {playerCards}")
        continueHit()
    else:
        playerTotal = sum(playerCards)
        compTotal = sum(compCards)
        if(playerTotal>compTotal):
            return "You Won"
        else:
            return "You Lose"

while isContinue:
    playChoice = input("Do you want to play black jack game? (y/n): ")
 
    if(playChoice=="y"):
        playerDrawCard()
        compDrawCard()
        gameResult = continueHit()
        print(gameResult)
    else:
        isContinue=False



   


