'''
Author: Seneca Greenwood
Date:5/13/24
Description: Allows user to input websites, usernames, and passwords, to then either print them all or print the specific set of a website's username and password and stores them into the code
Bugs: None
Challenges: Options can generate a stronger password or can encrypt a password into different characters
Sources: Samantha Marciano, Eli Murphy
'''


import random#allows the use of random coding 

def password_encrypt(message, old_alphabet, new_alphabet):#def password_encrypt(message, old_alphabet, new_alphabet)
#switches characters of message from old_alphabet to the new_alphabet
#Agrs:
    #message(input) asks user for a password to encrypt   Returns: message to list
    #old_alphabet(str) the list that contains regular alphabet and numbers   Returns: message to new list
    #new_alphabet(str) the list that contains encrypted alphabet and numbers   Returns: the old message into an encrypted message
    
    #Prints:
    #new encrypted message based on letters and numbers in that user's input
    new_message = ''#new message that will be encrypted(used as a placeholder)

    for m in message:#for every letter and number in the password
        for letter in old_alphabet:#for every letter and number that matches the list
            if m == letter:#if each letter equals each letter and number in the list
                new_message += new_alphabet[old_alphabet.index(letter)]#add new message to equal each letter and number to the new list's index
    return new_message#returns the new message from the function
def technology(websites, usernames, passwords, password_encrypt, i):#def technology(websites, usernames, passwords, password_encrypt, i)
    #connects empty list to let user's input replace emty list
    #Args:
        #websites(list) acts as an empty list to hold for user's websites   Returns: List that user enters
        #usernames(list) acts as an empty list to hold for user's usernames   Returns: List that user enters
        #passwords(list) acts as an empty list to hold for user's passwords   Returns: List that user enters
        #prints lists that user enters also is connected to if and elif statements that print all websites, usernames, and passwords or just prints a specific set
    print(f'{websites[i]}, {usernames[i]}, {passwords[i]}, {password_encrypt}')#prints every website in websites, every username in usernames, and every password in passwords
def add_entry(websites, usernames, passwords):#add_entry(websites, usernames, passwords)
    #contains all empty list to put in code when it is started
    #Args:
        #websites(list) acts as an empty list to hold for user's websites   Returns: List that user enters
        #usernames(list) acts as an empty list to hold for user's usernames   Returns: List that user enters
        #passwords(list) acts as an empty list to hold for user's passwords   Returns: List that user enters
    #adds the list to the beginning of code
    websites.append(input("Enter a website: "))#add website to websites list 
    usernames.append(input("Enter a username: "))#add username to usernames list
    passwords.append(input("Enter a password: "))#add password to password list
def main():
    websites = []#defines the variable as an empty list
    usernames = []#defines the variable as an empty list
    passwords = []#defines the variable as an empty list
    alphabet = list(" abcdefghijklmnopqrstuvwxyz012345679")#list for regular alphabet
    secret_alphabet = list(" #^6@!~$4-+>?/:;|%{[9)03&7,Q*8X`LzT=jrf")#list for encrypted alphabet
    
    add_entry(websites, usernames, passwords)#applies the empty list to code
    
    while True:#creates a true loop
        settings = input("Which option would you like: 1. Add entry 2. Print all 3. Print specific 4. Encrypt password 5. Generate secure password 6. End program")#promts user to either apply all lists that were made into code, print all websites, usernames, and  passwords or print a seperate one or generate a strong password or encrypt a password or end code
        
        if settings == "6":#If user inputs 6
            break#ends code
        elif settings == "1":#If user inputs 1
            add_entry(websites, usernames, passwords)#adds the entries of the user's inputs
        elif settings == "2":#If user inputs 2
            for i in range(len(websites)):#for every websites in the list
                technology(websites, usernames, passwords, password_encrypt(passwords[i], alphabet, secret_alphabet), i)#Print every index of the websites 
        elif settings == "3":#If user inputs 3
            website = input("Enter a website:")#user enters a website

            if website in websites:#if users website is in the websites list
                technology(websites, usernames, passwords, password_encrypt(passwords[websites.index(website)], alphabet, secret_alphabet), websites.index(website))#prints only one full index of website, username, and password
        elif settings == "4":#If user inputs 4
            message = str.lower(input("Enter password: "))#When user enters a password
            print(password_encrypt(message, alphabet, secret_alphabet))#prints the new password based on the encrypted alphabet
        elif settings == "5":#If user inputs 5
            print(random.choice(["QtK$eT$1V|&zf;f5", "W3lc0m3t0th3W0rld!", "~W3lc0me&#%1@Pq", "&Fr33D@mTw33n7y9", "dE11tAG@mM@&", "m#P52s@ap$V@5S", "4baT20%en$CA?qU3", "YKYf*o|mDrk;;AAF", "U%/tSm11`3xj~!2g.", "MD4r5@??Fa'CQ5AH", "D=i\C%PF!iaJ79E@"]))#prints a random choice from the list
            
main()                   
            
            




