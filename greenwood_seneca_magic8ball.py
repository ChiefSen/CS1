import random 

print("Hello lucky soul. I have the ability to tell your future in the blink of an eye! YOU WILL ONLY GET 3 ANSWERS!")

B = 0

while B < 3: 
    input("What is your question?" + str(B+1) + ": ")

    a = ["yes", "no", "maybe", "doubtful", "most likely"], ["per chance", "possible", "of course", "perhaps", "impossible"], ["Truthfully no", "Truthfully yes", "minimal chance", "high chance"]
    print(random.choice(a[B]))
    B += 1
    
