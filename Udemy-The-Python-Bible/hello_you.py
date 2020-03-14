#Ask user for name.
name = input("What is your name? ")

#Ask user for age.
age = input("What is your age? ")

#Ask user for city.
city = input("In what city do you live? ")

#Ask user what they enjoy.
love = input("What's one thing that you love doing? ")

#Create output text.
string = "Your name is {}, and you are {} years old.  You live in {} and you love {}."
output = string.format(name, age, city, love)

string2 = "Hey, {}!  I see that you're {} years old and love {}.  I also live in {}.  We should meet up sometime!"
output2 = string2.format(name, age, love, city)

#Print output to screen.
print(output2)
