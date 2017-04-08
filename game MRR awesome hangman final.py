# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):    
   
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    y=secretWord
    z=len(y)
    x=0
    i=-1
    while x!=z:           
           if i==z-1:
               return bool(False)
               break
           for i in range (0,z):                         
               if y[i] in lettersGuessed:
                     x=x+1      
                   
   
    if x==z:
       return   bool(True)
# FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    y=list(secretWord)
    z=len(y)
    x=0
    i=0
    c=list('_'*z)
    a=' '
    while i!=z:     
        
        
        while i>=0 and i<z:                       
            if y[i] in lettersGuessed:                     
                    c[i]=y[i]
                    a+=c[i]+' '
            else:
                a+='_ '
            i=i+1
    return a               
   # FILL IN YOUR CODE HERE...



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s=list('abcdefghijklmnopqrstuvwxyz')
    x=lettersGuessed
    y=len(lettersGuessed)
    z=0
    a=''
    
    for i in range (0,y):
            z=s.index(x[i])
            s[z]=''
            
            
        
    u=len(s)
    k=list(' '*26)
    for h in range (0,u) :
        a+=s[h]+k[h] 
    return ' '+ str(a)    
     # FILL IN YOUR CODE HERE...
    

def hangman(secretWord):
    print ''
    print 'GAME BY MRRGAMES LTD.  # COPYRIGHT 2013 '
    print ''
    print 'Welcome to the game, Hangman!'
    print '' 
    y=raw_input('Type your Name:')
    print ''
    print '-----------'
    print ''
    print 'I am thinking of a word that is %s letters long' % str(len(secretWord))
    g = 10  #max no. guesses
    b = 'You have %s guesses left.'
    print ''
    print b % str(g)
    print ''
    print 'Available letters:'+' a b c d e f g h i j k l m n o p q r s t u v w x y z '
    m=1
    k=''
    j= 1
    x=''
    lettersGuessed=list('')
    while g!=0:
      print ''  
      x=raw_input('Please guess a letter:')
      x=x.lower()
      if len(x) == len(secretWord):
          lettersGuessed=list(x)
          if (isWordGuessed(secretWord, lettersGuessed)):
            print ''
            print '-----------'
            print ''
            print str('Congratulations, you won!,you got 5 score Bonus !!!')
            g = g + 5
            break
          else:
               print ' '
               print 'Wrong guess Try Again. Penalty of 5 guesss......'
               g=g-5
               print ''
               print 'Sorry but you have %s guesses left now' % str(g) 
               
      if len(x)>1:
        print ''  
        print 'Type a single letter.Try Again'
        
      if len(x)==1:   
        if j==1:
          k=x
          lettersGuessed=list(k)
          j=0
            
                
        if (x in lettersGuessed)and m==0:     
                print ''              
                print 'Oops! You \'ve already guessed that letter:'+ str(getGuessedWord(secretWord, lettersGuessed))
        if (x not in lettersGuessed) and m==0:
            k+=x
        if (x in secretWord):
                if (x  in lettersGuessed)and m==1:
                    lettersGuessed=list(k)+list(x)
                    print ''
                    print 'Good guess:'+str(getGuessedWord(secretWord, lettersGuessed))
                    lettersGuessed=list(k)
                    g=g+1
                if (x not in lettersGuessed) and m==0:
                    lettersGuessed=list(k)+list(x)
                    print ''
                    print 'Good guess:'+str(getGuessedWord(secretWord, lettersGuessed))
                    lettersGuessed=list(k)
                    g=g+1
        else:        
                 
            if (x in lettersGuessed)and m==1:
                    print ''
                    print 'Oops! That letter is not in my word:'+ str(getGuessedWord(secretWord, lettersGuessed))
                    g = g-1
            if (x not in lettersGuessed)and m==0:
                       print '' 
                       print 'Oops! That letter is not in my word:'+ str(getGuessedWord(secretWord, lettersGuessed))
                       g = g-1
            
        
        
        if (isWordGuessed(secretWord, lettersGuessed)):
            print ''
            print '-----------'
            print ''
            print str('Congratulations, you won!')
            break
        print ' '
        print '-----------'
        lettersGuessed=list(k)
        if g>0 :
            print b % str(g)
            print ' '
            print 'Available letters:'+str(getAvailableLetters(lettersGuessed))
        
        m=0       
              
    if  g<=0:
       print '' 
       print 'Sorry, you ran out of guesses. The word was %s.' % str(secretWord)     
        
    print '__________________________________________________________'
    print ' '
    print '======================'+'Hangman is :'+ str(y) +'========================='
    print ''
    print 'Player Name:'+ str(y) 
    print ' '
    print 'your score is:'+str(g)
    print ' '
    print 'GAME BY \"M.R.RAKESH\" ---- MRRGAMES LTD. # copyrighted 2013 '
    print ''
    z=raw_input('To close game, Press Enter')
    
    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#secretWord = 'rakesh'
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
