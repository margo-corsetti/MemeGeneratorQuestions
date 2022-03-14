from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTImporter(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str): #--> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        file_ref = open(path, "r")
        quotes = []

        first = True
        for line in file_ref.readlines():
            #print(line)
            line = line.strip('\n\r').strip()
            if first == True:
                line = line[3:]
            #print(line)
            #line = line.split(' - ')
            #print(line)
            first = False

            if len(line) > 0:
                parse = line.split(' - ') #maybe should be '-' to separate quote and author


                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
