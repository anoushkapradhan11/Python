import random
def game():
    score=random.randint(1,101)
    with open("Hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print("Your score:",score)
    if(score>hiscore):
        with open("Hiscore.txt","w") as f:
            f.write(str(score))
    return score
game()