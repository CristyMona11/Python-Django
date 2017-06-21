import random
def scoresGrades():
     # assure that value of score is not a decimal
    #below is all the parameters where the grades fall into
    for i in range (0,10):
        random_num = random.random()*40+61
        score = round(random_num)
        if score >= 90:
            print "Score:" + str(score) + "Your grade is A"
        elif score >= 80:
            print "Score:" + str(score) + "Your grade is B"
        elif score >= 70:
            print "Score:" + str(score) + "Your grade is C"
        elif score >= 60:
            print "Score:" + str(score) + "Your grade is D"
        else:
            print "Score:" + str(score) + "Your grade is F"


scoresGrades()
