fib = [1, 1]

print("This program is all about the Fibonacci Sequence.")
print("To list n terms, type LIST")
print("To evaluate term n, type EVAL")
print("To search for a number, type FIND")
print(" ")

while True :
    choice = input("What would you like to do? ").strip().upper()

    if choice == "LIST" :
        n = int(input("How many terms would you like to have listed? ").strip())

        while len(fib) < n :
            fib_next = fib[-1] + fib[-2]
            fib.append(fib_next)

        output_list = fib[:n]

        print(*output_list, sep = "\n")


    elif choice == "EVAL" :
        nn = int(input("What term would you like to evaluate? ").strip())

        while len(fib) < nn :
            fib_next = fib[-1] + fib[-2]
            fib.append(fib_next)

        print(fib[nn-1])


    elif choice == "FIND" :
        nnn = int(input("What number would you like to search for? ").strip())

        n_max = 10000

        while len(fib) <= n_max :
            fib_next = fib[-1] + fib[-2]
            fib.append(fib_next)

        if nnn == 1 :
            print("1 is term 1 and term 2 of the Fibonacci Sequence.")
                
        elif (nnn in fib) and (nnn != 1) :
            output = fib.index(nnn) + 1
            print("{} is term {} of the Fibonacci Sequence.".format(nnn, output))

        else:
            print("Sorry, but {} is not one of the first {} terms of the Fibonacci Sequence.".format(nnn, n_max))

    else:
        print("Sorry, but that wasn't an option.")
