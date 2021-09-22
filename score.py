score = input("Enter Score: ")

try:
    grade = float(score)
except:
    print("Please enter a valid number")
    quit()

if grade >= 0 and grade <= 1 :
    if grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("You didn't enter a number between 1.0 and 0.0!")
    quit()
