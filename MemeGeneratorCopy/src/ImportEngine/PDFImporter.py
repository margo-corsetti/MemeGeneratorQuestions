from typing import List
import os
import subprocess
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFImporter(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str): #--> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        #print(path)
        #print(type(path))
        #path_edit = f"r'{path}'"
        #print(path_edit)
        #print(type(path_edit))
        tmp = f'./{random.randint(0,1000)}.txt'
        call = subprocess.call(['pdftotext', 'W:/Udacity/Intermediate Python/Meme Generator/src/_data/DogQuotes/DogQuotesPDF.pdf', tmp])

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            #print(line)
            line = line.strip('\n\r').strip()
            line = line.replace(' "', ' - "')
            line = line.replace('"','')

            if len(line) > 0:

                #print(line)
                parse = line.split(' - ') #maybe should be '-' to separate quote and author
                #print(parse)

                n = 0
                while n<len(parse):
                    i = n
                    j = n+1
                    new_quote = QuoteModel(parse[i], parse[j])
                    n = n+2
                    quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
