#Ask for favorite number.
num = int(input("What is your favorite whole number? ").strip())

#Square num.
numsq = num * num

#Cube num.
numcb = num * num * num

#Generate output.

output1 = "Your favorite number is {}.".format(num)
output2 = "Its square is {}, and its cube is {}.".format(numsq, numcb)

print(output1)
print(output2)
