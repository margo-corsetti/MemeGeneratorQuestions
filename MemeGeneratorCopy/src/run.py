from ImportEngine import DocxImporter, CSVImporter, PDFImporter, TXTImporter, QuoteModel

print(DocxImporter.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
print(CSVImporter.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
print(PDFImporter.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
print(TXTImporter.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
