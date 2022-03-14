from .IngestorInterface import IngestorInterface

class QuoteModel():
    def __init__(self, body, author):
        self.body = body
        self.author = author

    #def speak(self):
        #print(f'rrr"')

    def __repr__(self):
        return f'<{self.body}, {self.author}>'
'''
from .IngestorInterface import IngestorInterface

class QuoteModel():
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

    #def speak(self):
        #print(f'rrr"')

    def __repr__(self):
        return f'<{self.quote}, {self.author}>'
'''
