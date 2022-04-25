def countWordsFromFive():
    fileName = input('Enter the file name')
    numberOfWords = 0
    file = open(fileName,'r')
    for line in file :
        words = line.split()
        numberOfWords =  numberOfWords+len(words)
    print ('number of words are ',numberOfWords)
countWordsFromFive()