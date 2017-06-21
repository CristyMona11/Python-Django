import random
def coins():
    toss = 0
    heads=0
    tails=0
    while toss < 5000:
        toss += 1 #add one for each time tossed
        coin = round(random.randint(1, 2))#rounds if a decimal for random number
        if coin == 1:
            print("'Attempt #" + str(toss) + ': Throwing a coin... It\'s a head!...Got ' + str(heads) + " so far.'")
            heads+=1
        if coin == 2:
            print ("'Attempt #" + str(toss) + ': Throwing a coin... It\'s a tail!...Got ' + str(tails) + " so far.'")
            tails+=1
    total = toss
    print("'Attempt #5000: Throwing a coin... It\'s a head!...Got " + str(heads) + ' head(s) so far and ' + str(tails) +  " tail(s) so far. Ending the program, thank you!'")

coins()
