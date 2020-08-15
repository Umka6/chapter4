word = "computer"
lives = 3
while(lives>0):
    letter = input("Letter:")
    if(letter in word):
        print("index: " + str(word.index(letter)))
    else:
        lives = lives-1
        print("wrong")
print("game over")

