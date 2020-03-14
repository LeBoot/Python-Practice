a = 1
b = [5, 6, 7]

def f1() :
    a = 2
    print(a)

    print(b)

def f2() :   
    print(a)
    b[0]=9
    print(b)

f1()
f2()
print(a)
print(b)
