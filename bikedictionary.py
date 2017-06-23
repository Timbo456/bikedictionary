

biking = {"Bike" : "A metal object with two wheels to ride. ",
            "Seat" : "A leather or cloth holder for the human on the bike. ",
            "Spoke" : "A metal connector from the hub to the rim in the wheel. ",
            "Handlebar" : "A horizontal metal tube grasped by rider to steer. "}



start = "Yes"


while start == "Yes":
    choice = input("\nEnter 0 to exit.\nEnter 1 to look up a term. \nEnter 2 to add a term.\n"
            "Enter 3 to edit a term.\nEnter 4 to delete a term. \n\n\n"
            "\tPlease select an option: ")

    if choice == "0":
        start = "no"
        print("Ok, exiting now. ")


    elif choice == "1":
        term = input("Please enter a term to look up: ")
        if term in biking:
            definition = biking[term]
            print("\n",term, "means", definition)
        else:
            print("This term is not in the dictionary. ")

    elif choice == "2":
        term = input("Please enter a new term for dictionary: ")
        if term in biking:
            print("This is already in the dictionary. ")
        else:
            definition = input("What does it mean: ")
            biking[term] = definition

    elif choice == "3":
        term = input("What term would you like to edit? ")
        if term in biking:
            definition = input("The new definition of the term: ")
            biking[term] = definition
            print(term, " has been changed to: ", biking[term])
        else:
            print("This term is not in biking.")

    elif choice == "4":
        term = input("What term would you like to delete? ")
        if term in biking:
            del biking[term]
            print("\n",term," has been deleted\n")
        else: 
            print("This term is not in dictionary! ")

            


