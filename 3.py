def main():
    input_loop = True
    while input_loop:
        input_loop = False
        grade = int(input("Enter numerical score: "))
        if grade < 0 or grade > 100:
            input_loop = True
            print("Invalid score, try again")

    if grade >= 90:
        print("Incredible")
    elif grade >= 80:
        print("Good work")
    elif grade >= 70:
        print("You're trash lol")
    elif grade >= 60:
        print("Give up")
    else:
        print("Put the fries in the bag")

main()
