import os
import random
from ImportEngine import IngestorInterface as Ingestor
from ImportEngine import QuoteModel
import MemeEngine
import argparse

# @TODO Import your Ingestor and MemeEngine classes


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path#[0]
    print("path")
    print(img)

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
        print("body")
        print(quote)

    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)
    print("quote")
    print(type(quote))
    print(quote)

    meme = MemeEngine.MemeEngine('./tmp')
    print(img)
    print(quote.body)
    print(quote.author)
    path = MemeEngine.MemeEngine.make_meme(img, quote.body, quote.author)
    #path = meme.make_meme(img, quote.body, quote.author)
    print(path)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    my_parser = argparse.ArgumentParser(description = 'meme generator')
    my_parser.add_argument('--path', metavar='path', type=str, help='the path to list')
    my_parser.add_argument('--body', metavar='body', type=str, help='the body to list')
    my_parser.add_argument('--author', metavar='author', type=str, help='the author to list')

    args = my_parser.parse_args()
    #args = None
    generate_meme(args.path, args.body, args.author)
    #print(generate_meme(args.path, args.body, args.author))
