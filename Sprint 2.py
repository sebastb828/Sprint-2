#Sebastian Bonilla-Diaz
#This is basic quiz that you can take
print ("Welcome to the annual quiz show!")
print ("You will be asked questions that vary in difficulty")
print ("Make sure to keep a tally of how many questions you get correct")
print ("Lets begin!")


def question1():
    print ("------Easy Questions------")
    print ("You have unlimited attempts")
    print ("Name the biggest USA state by size ")
    #I used .lower() so that way someone doesn't need to worry about capitalization
    answer1 = input( "Enter your answer:").lower()
    while  answer1 != "alaska":
        print ("Wrong answer",)
        print ("Try again")
        answer1 = input( "Enter your answer:").lower()
    print ("Correct answer")


def question2():
    print ("What is 2+2 (Enter answer as a numeric value)")
    answer2 = input( "Enter your answer:")
    while  answer2 != "4":
        if not answer2.isdigit():
            print ("You enter an invalid input. Please enter a number")
        else:
            print ("Wrong answer",)
            print ("Try again")
        answer2 = input( "Enter your answer:")
    print ("Correct answer")


def question3():
    print("-------Medium Questions------")
    print("You only get one attempt")
    print ("What is the highest point on earth")
    answer3 = input("Enter your answer:").lower()
    if answer3 == "mount everest":
        print ("Correct answer")
    else:
        print ("Wrong answer")

def question4():
    print ("Name a number between 2 and 5 (Enter answer as a numeric value)")
    answer4 = (input("Enter your answer:"))
    while  not answer4.isdigit():
        print("You enter an invalid input. Please enter a number")
        print ("Try again")
        answer4 = input( "Enter your answer:")

    answer4 = int(answer4)
    if answer4 < 2 or answer4 > 5:
        print("Wrong answer")
    elif answer4 == 3 or answer4 == 4:
        print("Correct answer")
    else:
        print ("Wrong answer")



def question5():
    print("-------Hard Questions------")
    print("These questions are much harder")
    print ("Name the color's that when mixed create the color coral")
    answer5= input( "Enter your answer:").lower()
    if "orange" not in answer5  or "pink" not in answer5:
        print ("Wrong answer")
    else:
        print ("Correct answer")

def question6():
    print ("What are the two largest planets in our solar system?")
    answer6 = input( "Enter your answer:").lower()
    if "jupiter" in answer6 and  "saturn" in answer6:
        print ("Correct answer")
    else:
        print ("Wrong answer")

def question7():
    print("-------Extreme Questions------")
    print("What is the chemical symbol of Tungsten")
    answer7 = input( "Enter your answer:").lower()
    if answer7 == "w":
        print ("Correct answer")
    else:
        print ("Wrong answer")

def question8():
    print("What is the largest language in South Africa")
    answer8 = input( "Enter your answer:").lower()
    if answer8 == "isizulu":
        print ("Correct answer")
    else:
        print ("Wrong answer")


def Correct_answers(score):
    if score == 8:
        print("Perfect score good job!")
    elif score > 4:
        print ("You did well!")
    elif score ==4:
        print ("Not to bad! You got half right")
    else:
        print ("Better luck next time!")

def main():
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
    question8()
    print("Congratulations you've answered every question!")
    print("Now tell me how many questions did you get correct?")
    correct_answers = int(input("Enter how many questions you got correct:"))
    Correct_answers(correct_answers)


main()


print ("Now heres a little present before you go!")
Celebration  = "You did it!"
for x in range(5):
    print(Celebration)



