def count(): 
    fileName = input('Enter the file name bastard - ')
    wordNumber=0
    file = open(fileName, 'r')
    for f in file:
        words=f.split()
        wordNumber = wordNumber+len(words)
    print(wordNumber)

count()