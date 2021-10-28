#!/usr/bin/env python3
#Handicap Calculator created by Aashutosh Pantha
#September 18 2021

#INitializing varirables
Par = 0
Slope = 0
Score = 0
Diff = 0
TotalDiff= 0.0
AverageDiff = 0.0
Handicap = 0.0
Round_count=0
repeat=True


#welcome message for viewers
print("Welcome to Golf Handicap Calculator")
print("Aashutosh Pantha        100242069          September 18 2021")
print()


#Displaying Name and Round count
GolferName = input("Enter the Golfer's name:\t")
print("You need to enter at least three Roundcount")

while repeat:

    #Cheking whether there are more than 3 Roundcount
    if Round_count < 3:
        repeat=True
    else:
        choice = input("Enter whether you want to input another Roundcount. Enter (y/n)")
        if choice.lower()=="n":
            repeat=False
            continue
        elif choice.lower()=="y":
            repeat=True
        else:
            print("Please only enter y or n")
            continue

    #Inputing value of par, slope, score
    Par = int(input("Enter the Par of the course:\t"))
    if Par<72 or Par>76:
        continue

    Slope = int(input("Enter the Slope of the course:\t"))
    if Slope<122 or Slope>126:
        continue

    Score = int(input("Enter the Round score:\t"))
    if Score<59 or Score>120:
        continue

    Round_count += 1
    print("\nYou have succesfully entered", Round_count, "Roundcount.")

    #calculating Differential 
    Diff = (( Score - Par) * 113) /  Slope
    TotalDiff += Diff




# Calculating AverageDifferential and Handicap
AverageDiff = TotalDiff / Round_count
Handicap = round((AverageDiff * 0.96),2)


#Outcome of the Statement
print("Handicap is:\t ", Handicap)
print("AverageDiff is :\t" + str(round(AverageDiff)))
    








