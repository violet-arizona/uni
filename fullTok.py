"""
This module is used for spliting text into words a.k.a. tokens.
"""
import unicodedata

class Token:
    """
    Creates Token with 2 parameters:
    :param pos: position of the first symbol in token
    :param word: alphabetical sequence named token
    """
    def __init__(self, pos, word):
        self.pos = pos
        self.word = word

class TokenCat:
    """
    Creates TokenCat with 3 parameters:
    :param pos: position of the first symbol in token
    :param tok: sequence named token
    :param cat: type of token
    """
    def __init__(self, pos, tok, cat):
        self.pos = pos
        self.tok = tok
        self.cat = cat
    

class Tokenizer(object):
    """
    Class Tokenizer provides two methods for text-tokenization.
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
        
        tokens = []
        for i, item in enumerate(text):  
            nowLetter = item.isalpha()
            
            if(nowLetter and (i==0 or not lastIsLetter)):
                wordStart = i
            elif(i!=0 and not nowLetter and lastIsLetter):
                token = Token(wordStart, text[wordStart:i])
                tokens.append(token)
                
            if(i+1==len(text) and nowLetter):
                token = Token(wordStart, text[wordStart:i+1])
                tokens.append(token)
                
            lastIsLetter = nowLetter         
        return tokens

    def checkCategory(self, item):
        """
        Reads an input symbol and defines its type: alphabetical("word"), numerical("digit"), "space", "punctuation" or "other".
        :param item: input symbol
        :return: type of symbol
        """
        if(item.isalpha()):
            return "word"
        elif(item.isdigit()):
            return "digit"
        elif(item.isspace()):
            return "space"
        else:
            itemType = unicodedata.category(item)
            # unicodedata returns ‘P’ for punctuation marks
            if(itemType[0] == 'P'):
                return "punctuation"
            else:
                return "other"

    def tokenizeCat(self, text):
        """
        Reads an input string symbol by symbol and defines its type. Breaks the input string into substrings of same-category symbols 
        (tokens), records the position of the first symbol and type of token.
        :param text: input string
        :return: list of tokens
        """
        if not isinstance(text, str):
            raise TypeError('Input must be string type')

        tokens = []
        text = text.lower()
        for i, item in enumerate(text):
            # defines type of current symbol
            nowCat = Tokenizer().checkCategory(item)
            # if it's first symbol in string, remembers its position
            if(i==0):
                tokStart = i

            # if types of previous and current symbols aren't equal, creates token and remembers starting position of the new one
            elif(nowCat != lastCat or (i+1==len(text) and nowCat != lastCat)):
                token = TokenCat(tokStart, text[tokStart:i], lastCat)
                tokens.append(token)
                tokStart = i

            # if it's last symbol in string, creates token
            if(i+1==len(text)):
                token = TokenCat(tokStart, text[tokStart:i+1], nowCat)
                tokens.append(token)

            # type of current symbol is now type of previous symbol
            lastCat = nowCat
        return tokens

if __name__ == '__main__':
    t = Tokenizer()
    myTokens = t.tokenize("-Мама, помой раму! - сказала дочь.")
    for token in myTokens:
        print(token.pos, token.word, sep=' ', end=';\n')

    myTokensCat = t.tokenizeCat("-Мама, помой раму! - сказала дочь.")
    for token in myTokensCat:
        print(token.pos, token.tok, token.cat, sep=' ', end=';\n')

