"""
myToken module is used for spliting text into words a.k.a. tokens.
"""
class Token:
    """
    Class Token uses __init__ construction, which generates a new object. These objects consist of a word and it's starting position.
    """
    def __init__(self, pos, word):
        """
        Creates Token with 2 parameters:
        :param pos: position of the first symbol in token
        :param word: alphabetical sequence named token
        """
        self.pos = pos
        self.word = word

class Tokenizer(object):
    """
    Class Tokenizer provides a method for text-tokenization.
    """
    def tokenize(self, text):
        """
        Reads an input string symbol by symbol and defines wheather it is alphabetic or not. Breaks the input string into substrings of alphabetical symbols 
        (tokens), records the position of the first symbol.
        :param text: input string
        :return: list of tokens
        """
        if not isinstance(text, str):
            raise TypeError('Input must be string type')
        
        tokens = [] #empty list of objects aka tokens
        for i, item in enumerate(text):  #"for" loop iterates over a sequence of symbols in string, saving a symbol and its id
            nowLetter = item.isalpha() #true if current symbol is alphabetic
            lastIsLetter = text[i-1].isalpha() #true if previous symbol is alphabetic
            
            if(len(text)==1 and nowLetter): #checks if string contains only 1 letter
                token = Token(i, text)
                tokens.append(token)
            elif(nowLetter and (i==0 or not lastIsLetter)): #if current symbol is alphabetic and previous isn't
                wordStart = i #saves index where a new word starts
            elif(i!=0 and not nowLetter and lastIsLetter): # if current symbol is not alphabetic and previous is
                token = Token(wordStart, text[wordStart:i]) #creates a new object Token
                tokens.append(token) #adds new token to the list of tokens
            elif(i+1==len(text) and nowLetter): #checks the last symbol in string
                token = Token(wordStart, text[wordStart:i+1])
                tokens.append(token)
        return tokens #returns final list of tokens

if __name__ == '__main__': #doesn't execute when importing
    t = Tokenizer()
    myTokens = t.tokenize("-Мама, помой раму! - сказала дочь.")
    for token in myTokens:
        print(token.pos, token.word, sep=' ', end=';\n')
