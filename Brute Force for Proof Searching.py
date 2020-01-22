import itertools
import time

#This is basically a list of all the different characters that will be tried.
Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*=+?/<>")

inputString = input("What is your input string?\n")

#This sets the start time so that it can be used later on in the program to calculate how long the program took.
start = time.time()

#This tells us how many combinations are used.
counter = 1


#This stops the program once it gets to the number you edit here in code (most people would run out of patience WAY before that
#But if you feel the need you can increase the number.
##################
CharLength = 4
#for CharLength in range(25):
if CharLength==4:
    #This finds all of the possible combinations of characters that are of the correct length.
    stringg = (itertools.product(Alphabet, repeat = CharLength))

    #This prints three blank lines.
    print("\n \n")

    #These print information for the user on the progress of the crack.
    print("currently working on string with ", CharLength, " chars")
   # print("We are currently at ", (counter / (time.time() - start)), "attempts per seconds")
    print("It has been ", time.time() - start, " seconds!")
    print("We have tried ", counter, " possible strings!")

    #This is the way to print the products of generators.
    for i in stringg:

        #This increases the number of combinations tried by one to show that one more has been tried.
        counter += 1

        #As the itertools.products() returns a tuple, it has to be converted into a sting.
        i = str(i)

        #The parts that were added as a result of conversion from tuple have to be removed.
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        i = i.replace(",", "")
        i = i.replace("(", "")
        i = i.replace(")", "")

        #This checks if the inputString created by the user was correct.
        if i == inputString:

            #This takes the time at which the program finished.
            end = time.time()

            #This works out the time it took to find the inputString.
            timetaken = end - start

            #This tells the user how long it took to find the inputString as well as how many attempts it took.
            print("Found it in ", timetaken, " seconds and ", counter, "attempts")

            #This tells the user how many attempst were made per second.
            print("That is ", counter / timetaken, " attempts per second!")

            #This prints the inputString to confirm for the user that the program was sucessful.
            print(i)

            #This stops the program from exiting until the user presses enter.
            input("Press enter when you have finished")

            #This exits the program
            exit()

