import random
avengers["Thor", "Captain America", "Thanos"]
while True:
    user = input("Which character am I thinking of in Avenger's Endgame(options are Thor, Thanos, Captain America): ").lower()
    comp = (random.choice(avengers))
    if user == "Thor" and comp == "Thor":
        print("Yes!")
        break
        
    elif user == "Captain America" and comp == "Thor":
        print("Wrong")
    elif user == "Thanos" and comp == "Thor":
        print("Wrong")
    elif user == "Captain America" and comp == "Captain America":
        print("Yes")
        break
    
    elif user == "Thor" and comp == "Captain America":
        print("Wrong")
    elif user == "Thanos" and comp == "Captain America":
        print("Wrong")
    elif user == "Thanos" and comp == "Thanos":
        print("Yes")
        break

    elif user == "Captain America" and comp == "Thanos":
        print("Wrong")
    elif user == "Thor" and comp == "Thanos":
        print("Wrong")
    else:
        print("Invalid character")

    
