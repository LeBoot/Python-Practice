#Ask user for name.
name = input("Hi there.  What's your name? ")

#Reply to user.
reply_string_1 = "Good to meet you, {}. "
output1 = reply_string_1.format(name)
print(output1)

#Ask user for first hobby.
hobby1 = input("What is your favourite hobby? ")

#Reply to user.
reply_string_2 = "You know, {}, {} can be dangerous.  It is fun, though, so I'll give you that!"
output2 = reply_string_2.format(name, hobby1)
print(output2)

#Ask user for another hobby.
hobby2 = input("What else do you enjoy? ")

#Reply to user.
reply_string_3 = "Gee, {}.  {} and {}... that's quite the adventure.  We should meet up!"
output3 = reply_string_3.format(name, hobby1, hobby2)
print(output3)

#Hang out?
response = input("What do you say we hang out next weekend? ")
