#Ask about milage each day.

mon = float(input("How many miles did you run on Monday? ").strip())
tue = float(input("How many miles did you run on Tuesday? ").strip())
wed = float(input("How many miles did you run on Wednesday? ").strip())
thu = float(input("How many miles did you run on Thursday? ").strip())
fri = float(input("How many miles did you run on Friday? ").strip())
sat = float(input("How many miles did you run on Saturday? ").strip())
sun = float(input("How many miles did you run on Sunday? ").strip())


#Total milage for week.

total = mon + tue + wed + thu + fri + sat + sun
output_total = "Your total milage for the week was {} miles, and".format(round(total, 2))


#Average milage for each day.

average = total/7
output_average = "you ran an average of {} miles per day.".format(round(average, 2))


#Congratulations

output_congratulations = "Great job!! Keep up the good work :)"


#Suggestion for next week.

suggestion_total = 1.1 * total
suggestion_average = suggestion_total/7

output_suggestion_total_pt1 = "If you are trying to increase by 10% each week,"
output_suggestion_total_pt2 = "you should aim for {} total miles next week,".format(round(suggestion_total, 2))
output_suggestion_total_pt3 = "which would be an average of {} miles per day.".format(round(suggestion_average, 2))


#Print output(s).

print(" ")
print(output_total)
print(output_average)
print(" ")
print(output_congratulations)
print(" ")
print(output_suggestion_total_pt1)
print(output_suggestion_total_pt2)
print(output_suggestion_total_pt3)

