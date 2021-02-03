weather = input("How is the weather to day?: ")
if weather == "Rainy" or weather == "Snow":
    print("Prepare your umbrella\n")
elif weather == "Sand storm":
    print("Wear your mask\n")
else:
    print("Have a nice day :)\n")

temp = int(input("Temperature: "))
if 30 <= temp:
    print("So hot today. Stay at home.\n")
elif 10 <= temp: # and temp < 30
    print("What a nice day.\n")
elif 0 <= temp: # and temp < 10
    print("Put on your padding before you leave.\n")
else:
    print("Too cold! Stay at home.\n")