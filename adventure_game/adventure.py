name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you cna go left or right. Which way you wanna go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around or swim accross. Type walk or swim to choose ").lower()

    if answer == "swim":
        print('You swam accross and were eaten by a crocodile.')
    elif answer == "walk":
        print('You walked for 2hrs and were paralyized.')
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come across a bridge. Do you jump or not").lower()
    
    if answer == "jump":
        print("You jumped and hit your head and died")
    elif answer == "no":
        print("You still die cause why not")
    else:
        print("Invalid option. You lose")

else:
    print("Not a valid option. You lose. ")
