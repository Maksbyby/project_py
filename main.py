def balanced(expression):
    stak = []
    for x in expression:
        if x == '(':
            stak.append(x)
    print (stak)
#print(balanced(input()))


balanced('asd(asd)as())