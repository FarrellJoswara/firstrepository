#variable declaration
age = "" 


while age == "":
    try:
        age = int(input("How old are you in years? "))
    except:
        print("Numbers only please!")

print("You have lived for at least " + str(age * 365 * 24 * 60 * 60) + " seconds!")