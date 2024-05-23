'''
Author: Seneca Greenwood
Date:4/22/24
Description: Code creates multiple actions of printing and returning codes involving strings and variables with functions and calls each one at the end of the code
Bugs: None
Challenges: None
Sources: Samantha Marciano, Eli Murphy
'''

import random#allows the use of random coding

def chorus():#defines the code inside as a function
    print("Baa, baa, black sheep, Have you any wool?")#prints chorus of the song
    print("Yes, sir, yes, sir, Three bags full!")#prints chorus of the song

def sing():
    chorus()#uses chorus from first line of code inside "def chorus"
    print("One for my master, And one for my dame,")#prints lyrics of the song
    print("and one for the little boy who lives down the lane.")#prints lyrics of the song
    chorus()#uses chorus from first line of code inside "def chorus"


def add(num1, num2):#defines the code inside as a function and creates a variable
    print("Number 1:", num1)#prints the variable as an integer
    print("Number 2:", num2)#prints the second variable as an integer
    print(num1 + num2)#adds the two integers together

def print_list(my_list):#defines the code inside as a function
    for element in my_list:#in the list of desserts, 
        print(element)#print each item in the list         
def contains_element(my_list, element):#defines the code inside as a function and creates variables
    if element in my_list:#if the specific element that it askes is in the list
        return True#accept it as a true statement
    else:#if not
        return False#deny it as a false statement
def is_numeral(integer):#defines the code inside as a function
    if integer.isnumeric():#if this variable is a number
        return True#accept it as a true statement
    else:#if not
        return False#deny it as a false statement
def random_numeral():#defines the code inside as a function
    while True:#puts code in a while loop
        num3 = input("enter number 1:")#gives input to enter an integer
        num4 = input("enter number 2:")#gives input to enter another integer
        if is_numeral(num3) and is_numeral(num4):#if theses variables are integers
            print(random.randint(int(num3), int(num4)))#print a random number between them
            break#ends code
        else:#if not
            print("please enter a number:")#asks for an integer again
            continue#continues code 
def replacing(string, old_character,new_character):#defines the code inside as a function and relates variables to the function
    new_string = ""#creates a new letter
    for s in string :#for the new string in the old string
        if s == old_character:#if the code gets to the old string
            new_string += new_character#replace the old string with the new string
        else:#if not
            new_string += s#keep going until it finds specific string
    return new_string#returns new string to code
def main():#calls every function
    sing()#ends function
    add(5,3)#prints the solution
    desserts = ["pie", "cookie", "pudding", "ice cream", "cake",]#creates a list of desserts

    print_list(desserts)#ends function
    games = ["Minecraft", "Roblox", "Clash Royale", "Candy Crush"]#creates a list of games
    element = "Minecraft"#defines the specific element
    print(contains_element(games, element))#print specific element to define the true or false statements
    integer = "7"#defines the variable
    print(is_numeral(integer))#prints the new integer
    random_numeral()#ends function
    print(replacing("lateral", "l","s"))#prints the new string
    
main()#ends the calling of functions

          
