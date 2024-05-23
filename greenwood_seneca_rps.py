'''
Author: Seneca Greenwood
Date:11/28/23
Description: Starts a game under the command of either yes or no to play rock, paper, scissors. Coding will randomly select a choice to either win, lose, or tie. The game will end whenever you want, keeping the user's score until the end of the game where it reveals all points from those games.
Challenges: Both challenges were only on coding:
str.lower creates all responses from user lowercase automatically
comp and user is what keeps the score for the code and the user while you play
Sources: Eli Murphy, Ms. Marciano 
'''




import random #imports the code called random
RPSlist = ["paper", "rock", "scissors"] #creates a variable list consisting of words
comp_point = 0 #score for comp starts at 0
user_point = 0 #score for user starts at 0

while True: #keeps code in a loop
    print("computer score is", comp_point)#every time comp wins adds one point
    print("user score is", user_point) #every time user wins adds one point
  
    comp = (random.choice(RPSlist))#code chooses an option ramdomly from the list
    play = input("Do you want to play Rock, Paper, Scissors?")#code types comment in quotations
    if play == "no": #if user types no ...
        break #ends code
    elif play == "yes":#when user types yes 
        user = str.lower(input("rock, paper, scissors ...enter option..."))#creates all user responses in lowercase and gives user to enter one of three variable options
        if user == "rock" and comp == "paper": #if the user enters a variable and the code enters another variable ...
            print("You lose!") #code types comment in quotations
            comp_point += 1 #adds one point
        elif user == "rock" and comp == "scissors": #if the user enters a variable and the code enters another variable ...
            print("You win!") #code types comment in quotations
            user_point += 1 #adds one point
        elif user == "rock" and comp == "rock": #if the user enters a variable and the code enters another variable ...
            print("You Tie!") #code types comment in quotations
        elif user == "paper" and comp == "scissors": #if the user enters a variable and the code enters another variable ...
            print("You lose!") #code types comment in quotations
            comp_point += 1 #adds one point
        elif user == "paper" and comp == "rock": #if the user enters a variable and the code enters another variable ...
            print("You win!") #code types comment in quotations
            user_point += 1 #adds one point
        elif user == "paper" and comp == "paper": #if the user enters a variable and the code enters another variable ...
            print("You tie!") #code types comment in quotations
        elif user == "scissors" and comp == "rock": #if the user enters a variable and the code enters another variable ...
            print("You lose!") #code types comment in quotations
            comp_point += 1 #adds one point
        elif user == "scissors" and comp == "paper": #if the user enters a variable and the code enters another variable ...
            print("You win!") #code types comment in quotations
            user_point += 1 #adds one point
        elif user == "scissors" and comp == "scissors": #if the user enters a variable and the code enters another variable ...
            print("You tie!") #code types comment in quotations

    else:
      print("invalid")# any other response will not work in code
        


