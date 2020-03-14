#Ask for favorite number.
favnum = int(input("What is your favorite whole number? ").strip())

#Divisible by 2.
if (favnum/2 == int(favnum/2)) and (not(favnum/3 == int(favnum/3))) :
    print("Divisible by 2 but not by 3.")

#Divisible by 3.
elif (not(favnum/2 == int(favnum/2))) and (favnum/3 == int(favnum/3)) :
    print("Divisible by 3 but not by 2.")

#Divisible by 2 and 3.
elif (favnum/2 == int(favnum/2)) and (favnum/3 == int(favnum/3)) :
    print("Divisible by both 2 and 3.")

#Divisible by neither 2 nor 3.
elif (not(favnum/2 == int(favnum/2))) and (not(favnum/3 == int(favnum/3))) :
    print("Divisible by neither 2 nor 3.")

#Other option.
else :
    print("Programmer missed something.")
