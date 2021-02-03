def howToday():
    weather = input("How is the weather today?: ")
    temp = int(input("What's the temperature today?: "))

    if weather == "Rainy" or weather == "Snow":
        prepare = "Prepare your umbrella\n"
    elif weather == "Sand storm":
        prepare = "Dont forget your mask\n"
    else:
        prepare = "Have a nice day :)\n"
    
    if temp > 0 and temp < 30:
        if 10 <= temp and weather != "Rainy":
            ment = "\nWarm and cozy. " + prepare
        elif 10 <= temp and weather == "Rainy":
            ment = "\nIt's warm, but a little humid. " + prepare
        else:
            ment = "\nPut on your padding before you leave. " + prepare
    elif temp >= 30:
        ment = "\nSo hot today. Stay at home.\n"
    else:
        ment = "\nToo cold! Stay at home.\n"

    return ment

print(howToday())