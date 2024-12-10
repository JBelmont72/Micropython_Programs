user_name = input("What is your name?")

if user_name =="Clark Kent":
    print("You are Superman!")
while user_name != "Clark Kent":
    if user_name == "Wane":
        print("you are Batman!")
        break
    else:
        print("I don't know you.")
        user_name=input("What is your name again?")
print("You are Superman!")