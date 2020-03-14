n = int(input("What maximum number do you want to go to? ").strip())

evens = 0
odds = 0

x = list(range(1,n+1))
for number in x :
    if number % 2 == 0 :
        evens = evens + 1
    else :
        odds = odds + 1

print("{} evens and {} odds.".format(evens, odds))
