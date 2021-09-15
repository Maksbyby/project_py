def balanced(expression):
    stak = []
    for x in expression:
        if x == '(':
            stak.append(x)
    if len(stak)>0:
        for x in expression:
            if x == ')':
                stak.pop()
    else:
        print('False')
    print (stak)
#print(balanced(input()))


balanced(')))')