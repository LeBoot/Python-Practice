#Ask user for email address.
email = input("What is your email address? ").strip()

#Slice username (by using index function) and make username uppercase.
username = email[:email.index("@")].upper()

#Slice domain (by using index function) and make domain uppercase.
domain = email[email.index("@")+1:].upper()

#Create output.
output = "Your username is {} and the domain that you are using is {}.".format(username, domain)

#Print output.
print(output)
