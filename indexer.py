"""
Indexer module is used for creating a database of words and numbers with their starting indexes in text.
"""
import shelve
import fullTok

class Database(object):
    """
    Class Database provides a method for creating a database out of a text file.
    """
    def toDB(self, fileDB, fileTxt):
        """
        Reads an input file and tokenizes it. If a token's type is alphabetical or numerical, records it into a database.
        :param fileDB: name of database files that will be created
        :param fileTxt: name of an input text file
        """
        # database is opened for operations
        db = shelve.open(fileDB)
        # input file is opened for reading
        myFile = open(fileTxt, "r", encoding="UTF-8")
        toTok = myFile.read()
        # input file is tokenized
        data = fullTok.Tokenizer().tokenizeCat(toTok)
        # list of token's positions
        l = list()

        # checks type of each token
        for token in data:
            # if token is alphabetical or numerical, puts it into the database
            if(token.cat == "digit" or token.cat == "word"):
                key = token.tok
                # if same token is already in the database, adds new position to the list of its positions
                if key not in db:
                    l.clear()
                else:
                    l = db[key]
                l.append(token.pos)
                db[key] = l

        print(dict(db))
        # database is closed
        db.close()

if __name__ == '__main__':
    d = Database()
    myDB = d.toDB("mydb", "text.txt")

