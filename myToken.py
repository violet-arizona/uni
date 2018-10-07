"""
myToken is used for spliting text into words aka tokens.
На вход программе передается текст строкового типа (str), на выходе получаем список токенов, который выводится на экран в виде "номер позиции начала слова - слово".
Счет позиции символа в строке начинается с 0. 
"""
class Token:
    """Class Token uses __init__ construction, which generates a new object. These objects consist of a word and it's starting position."""
    def __init__(self, pos, word):
        self.pos = pos
        self.word = word

class Tokenizer(object):
    def tokenize(self, text):
        if(type(text)!= str): #checks if argument is not a string
            return "Argument must be a string!"
            
        tokens = [] #empty list of objects aka tokens
        for i, item in enumerate(text):  #"for" loop iterates over a sequence of symbols in string, saving a symbol and its id
            nowLetter = item.isalpha() #true if current symbol is alphabetic
            lastIsLetter = text[i-1].isalpha() #true if previous symbol is alphabetic
            
            if(len(text)==1 and nowLetter): #checks if string contains only 1 letter
                token = Token(i, text)
                tokens.append(token)
            elif(nowLetter and (i==0 or not lastIsLetter)): #if current symbol is alphabetic and previous isn't
                wordStart = i #saves index where new word starts
            elif(i!=0 and not nowLetter and lastIsLetter): # if current symbol is not alphabetic and previous is
                token = Token(wordStart, text[wordStart:i]) 
                #creates a new object Token, which consists of a word and its starting position
                tokens.append(token) #adds new token to the list of tokens
            elif(i+1==len(text) and nowLetter):
                token = Token(wordStart, text[wordStart:i+1])
                tokens.append(token)
        return tokens #returns final list of tokens

if __name__ == '__main__': #doesn't execute when importing
    t = Tokenizer()
    #myTokens = t.tokenize("Мама мыла раму. А я мыла пол.")
    myTokens = t.tokenize("-Мама, помой раму! - сказала дочь")
    for token in myTokens:
        print(token.pos, token.word, sep=' ', end=';')
