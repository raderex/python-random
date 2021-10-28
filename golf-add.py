# python-random
import math

# initializing variables
par = 0
slope = 0
score = 0
totalRounds = 0
diff = 0
handicapp = 0.0
totalRounds = 0
exit = False
name = ""
diffList = []


# Take the names
while not name:
    print("\nPLEASE ENTER YOUR NAME PLEASE\n")
    name = input("Player's name: ")

print("\nYOU MUST ENTER DATA FOR AT LEAST THREE LOCATION :")

# returns the list of scores of top 3, top 6, or top 10 best games
def get_calulating_list(diffList):
    diffList.sort()
    if len(diffList) < 15:
        diffList = diffList[-3:]
    elif 15 <= len(diffList) < 20:
        diffList = diffList[-6:]
    elif len(diffList) >= 20:
        diffList = diffList[-10:]
    return diffList

#actually calculate and print the handicapp by truncating the hadicapp to 1 decimal point
def calculate_hadicapp(diffList):
    calculating_list = get_calulating_list(diffList)

    required_rounds = len(calculating_list)
    print("YOUR", required_rounds, "BEST ROUNDS ARE", calculating_list)

    totalDiff = 0.0
    for diff in calculating_list:
        totalDiff += diff

    handicapp = ((totalRounds/required_rounds)*0.96)
    # so that value truncates at 1 decimals
    handicapp = math.trunc(handicapp*10)/10

    print(f"HELLO {name} YOUR HANDICAPP IS:\t{handicapp}")

    if handicapp <= 0:
        print("\nHANDICAPP LEVEL: Championship")
    elif 0 < handicapp <= 5:
        print("\nHANDICAPP LEVEL: Duffer")
    elif 5 < handicapp <= 10:
        print("\nHANDICAPP LEVEL: Average")
    elif handicapp > 10:
        print("\nHANDICAPP LEVEL: Hacker")


# until the user doesn't want to exit
while not exit:

    # check the condition weather there are at least 3 locations
    if totalRounds < 3:
        print("\nENTER THE DATA FOR THE NEW LOCATION\n")
    else:
        # yes then ask then out choice to fill the data
        choice = input(
            "\nENTER 'y' FOR ENTERING DATA FOR MORE LOCATIONS, 'n' TO EXIT AND PRINT THE HANDICAPP: ")
        if choice.lower() == "y":
            print("HERE YOU GO")
        elif choice.lower() == "n":
            # make it exit from the while loop
            exit = True
            continue
        else:
            print("YOU MUST ENTER EITHER 'y' OR 'N'")
            continue

    try:
        par = int(input("Enter the par:\t\t"))
        if not (72 <= par <= 76):
            print("INVALID PAR(SHOULD BE WITHIN 72 AND 76): ENTER EVERYTHING AGAIN")
            continue

        slope = int(input("Enter the slope:\t\t"))
        if not (122 <= slope <= 126):
            print("INVALID SLOPE(SHOULD BE WITHIN 122 AND 126): ENTER EVERYTHING AGAIN")
            continue

        score = int(input("Enter the score:\t\t"))
        if not (59 <= score <= 120):
            print("INVALID SCORE(SHOULD BE WITHIN 59 AND 120): ENTER EVERYTHING AGAIN")
            continue
    
    except ValueError:
        print("\nPLEASE ENTER THE NUMERIC VALUE FOR PAR, SLOPE AND SCORE")
        continue

    diff = ((score-par)*113)/slope
    diffList.append(round(diff,4))
    totalRounds += 1

    print(f"\nYOU'VE SUCCESFULLY ADDED {totalRounds} ROUND(S)\n")


calculate_hadicapp(diffList)
    
