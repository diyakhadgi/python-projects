print("Welcome to the game!")

name = input("What is your name?: ")
age = int(input("What is your age?: "))

print("Hello", name, "you are", age, "years old")

if age >= 18:
    print("You are old enough to play")
    
    wants_to_play = input("Do you wanna play? ").lower()
    if wants_to_play == "yes":
        print("Okay lets begin")
        
        left_or_right = input("You're walking through a jungle and you see a lion coming."\
            "Will you run away from it or be brave and try petting it. Write A to run away"\
            "and B to pet: ").lower()
        if left_or_right == 'a':
            print("Smart move. You start to run as fast as you can and see a horse. ")
            
            gay_or_not = input("The horse asks you if you're gay or not. Type yes or no: ").lower() 
            
            if gay_or_not == "yes":
                print("Congratulations! You found your horse prince charming."\
                    "He fell in love with you and decided to marry you. ")
            elif gay_or_not == "no":
                print("He is disapointed in you. Now he is angry that you're not gay."\
                    "He holds you until lion arrives and leaves you to lion. Now"\
                    "you're slowly being eaten by lion. Moral is:\"Be gay until you die\" ")
            else:
                print("You're acting smart choosing out of options. So now you die bitch. ")
            
        elif left_or_right == "b":
            print("Bold of you to assume you'll pet a lion."\
                "The lion eats you and you die. ")
        else:
            print("You chose out of option so You Shall Die. ")
        
    else:
        print("Okay bye...")
else:
    print("You are not old enough to play. ")