#Ask for full name without spaces.
question = "Type your first and last name (without spaces) to see how it is spelled backwards: "

namein = input(question).strip()

#Reverse name.
backwards_name = namein[::-1]
output = backwards_name.upper()

#Print output.
print(output)
