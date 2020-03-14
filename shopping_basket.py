Savailable_food = {
    "FIG":[1,1],
    "APPLE":[12,1],
    "DATE":[20,.5],
    "CABBAGE":[5,3],
    "BANANA":[10,2],
    "CUCUMBER":[10,1]
    }

while True :

    choice = input("What food would you like to purchase? ").strip().strip("s").upper()
    
    if (choice in available_food) and (available_food[choice][0] == 1) :
        buy1 = input("We have only 1 {} in stock right now, and it costs {} dollar(s).  Would you like to purchase it? (y/n)? ".format(choice, available_food[choice][1])).strip().lower()

        if buy1 == "n" :
            print("No problem!")

        elif buy1 == "y" :
            print("Okie dokie! You've purchased 1 {}".format(choice))
            available_food[choice][0] = (available_food[choice][0] - 1)
        
    elif (choice in available_food) and (available_food[choice][0] > 0) :
        quantity = int(input("We have {} {}S in stock right now at {} dollar(s) each.  How many would you like to purchase? ".format(available_food[choice][0], choice, available_food[choice][1])).strip())

        if quantity == 0 :
            print("No problem!")

        elif quantity > 0 :
            
            if (quantity > available_food[choice][0]) and (quantity != 0) :
                print("Sorry, but we only have {} {}S in stock right now.".format(available_food[choice][0], choice))

            elif ((quantity <= available_food[choice][0]) and (quantity != 1)) and (quantity != 0) :
                print("Great! You've purchased {} {}S.".format(quantity, choice))
                available_food[choice][0] = (available_food[choice][0] - quantity)

            elif ((quantity <= available_food[choice][0]) and (quantity == 1)) and (quantity != 0) :
                print("Great! You've purchased 1 {}.".format(choice))
                available_food[choice][0] = (available_food[choice][0] - 1)

            else :
                print("The coder has overlooked something.")

        elif quantity < 0 :
            print("You cannot purchase a negative amount of food.")

    else :
        print("Sorry, but we don't have any {}S in stock.".format(choice))
