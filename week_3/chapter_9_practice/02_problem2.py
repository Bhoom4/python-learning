import random
def game():
    print("you are playing a game")
    score=random.randint(1,56)
# fetch the highscore
    with open("week_3/chapter_9_practice/hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    print(f"your score: {hiscore}")
    if(score>hiscore):
        with open("week_3/chapter_9_practice/hiscore.txt","w")as f:
            f.write(str(score))
    return score

game()
