def findCustomer():
    right = "Chris"
    person = "Unknown"
    
    while True:
        print(f"\nHere's the menu you ordered, {right}.\n")
        person = input("What is your name, sir?: ").capitalize()
        if person != right:
            print(f"Sorry, This menu is for {right}")
        else:
            print("Thanks. Enjoy your meal.\n")
            break

findCustomer()