"""
myToken module is used for spliting text into words a.k.a. tokens.
"""


class Token(object):
    """
    Class Token uses __init__ construction, which generates a new object.
    These objects consist of a word and it's starting position.
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
        Reads an input string symbol by symbol and defines wheather it is alphabetic or not.
        Breaks the input string into substrings of alphabetical symbols (tokens),
        records the position of the first symbol.
        :param text: input string
        :return: list of tokens
        """
        if not isinstance(text, str):
            raise TypeError('Input must be string type')
        
        # empty list of objects aka tokens
        tokens = []
        # "for" loop iterates over a sequence of symbols in string, saving a symbol and its id
        for i, item in enumerate(text):
            # true if current symbol is alphabetic
            nowLetter = item.isalpha()
            
            # if current symbol is alphabetic and previous isn't, we save index where a new word starts
            if(nowLetter and (i==0 or not lastIsLetter)):
                wordStart = i
            # if current symbol is not alphabetic and previous is, we create a new object Token
            elif(i!=0 and not nowLetter and lastIsLetter): 
                token = Token(wordStart, text[wordStart:i])
                # adds new token to the list of tokens
                tokens.append(token)
                
            # checks the last symbol in string
            if(i+1==len(text) and nowLetter):
                token = Token(wordStart, text[wordStart:i+1])
                tokens.append(token)

            # true if previous symbol is alphabetic
            lastIsLetter = nowLetter
        # returns final list of tokens 
        return tokens

# doesn't execute when importing
if __name__ == '__main__':
    t = Tokenizer()
    myTokens = t.tokenize("-Мама, помой раму! - сказала дочь.")
    for token in myTokens:
        print(token.pos, token.word, sep=' ', end=';\n')
