#Ask user for first then last name.
namein = input("What is your full name? ").strip()

#Reverse order to be last, first.
forename = namein[:namein.index(" "):]
surname = namein[namein.index(" ") + 1 ::]

#Create output.
output = "Your name is {}, {}.".format(surname, forename)

#Print output.
print(output)
