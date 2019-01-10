"""
Indexer module is used for creating a database of words and numbers with their starting indexes in text.
"""
import shelve
import fullTok
from os import path


class Database(object):
    """
    Class Database provides a method for creating a database out of a text file.
    """
    def toDB(self, fileDB, fileTxt):
        """
        Reads an input file and tokenizes it.
        If a token's type is alphabetical or numerical, records it into a database.
        :param fileDB: name of database files that will be created
        :param fileTxt: name of an input text file
        """
        # database is opened for operations
        db = shelve.open(fileDB, writeback=True)
        # input file is opened for reading
        myFile = open(fileTxt, "r", encoding="UTF-8")
        toTok = myFile.read()
        myFile.close()
        # input file is tokenized
        data = fullTok.Tokenizer().tokenizeCat(toTok)

        # checks type of each token
        for token in data:
            # if token is alphabetical or numerical, puts it into the database
            if(token.cat == "digit" or token.cat == "word"):
                # if same token is already in the database, adds new position
                db.setdefault(token.tok, {}).setdefault(path.basename(fileTxt), []).append(token.pos)

        print(dict(db))
        # database is closed
        db.close()

if __name__ == '__main__':
    d = Database()
    myDB = d.toDB("mydb", "text.txt")

