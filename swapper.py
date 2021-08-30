def swapFile():
    fileFirst=input('Name of File 1:')
    fileSecond=input('Name of File 2:')
    
    with open(fileFirst, 'r') as a:
        dataA = a.read()

    with open(fileSecond, 'r') as b:
        dataB = b.read()

    with open(fileFirst, 'w') as a:
        a.write(dataB)

    with open(fileSecond, 'w') as b:
        b.write(dataA)

swapFile()
        
    