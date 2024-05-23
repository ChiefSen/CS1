print("Alarm")


while True:
    snooze = str.lower(input("Snooze?"))

    if snooze == "yes":
        print("Sleep for 5 more minutes.")
    elif snooze == "no":
        print("Wake up loser!")
        break
    else:
        print("invalid")

print("Go shower")

while True:
     shower = str.lower(input("Turn on water?"))

     if shower == "yes":
         print("You smell good.")
         break
     elif shower == "no":
        print("You smell bad.")
     else:
         print("invalid")

print("Go to wardrobe")
while True:
    dressed = str.lower(input("Get dressed?"))
    if dressed == "no":
        print("Cannot go to school.")
    elif dressed == "yes":
        print("Can go to school!")
        break
    else:
        print("invalid")

print("Go outside")
while True:
    rain = str.lower(input("It's raining. Grab an umbrella?"))

    if rain == "yes":
        print("Grab umbrella and have a GREAT DAY at school!")
        break
    elif rain == "no":
        print("It actually is raining dummy!")
    else:
        print("invalid")
        
        
    
        
    

                
