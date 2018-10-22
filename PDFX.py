import pdfx
import re

#will use PDFX to get the data it can from a PDF.
def getPDFData(fileName):
    if (fileName.endswith(".pdf")):
        next
    else:
        fileName += ".pdf"
    print("Parsing PDF file...")
    pdf = pdfx.PDFx(fileName)
    print(pdf)
    # metadata = getMetadata(pdf)
    # references = pdf.get_references_as_dict()
    # fullText = pdf.get_text()
    # paper = {'metadata':metadata,'fullText':fullText}
    # return paper

#formats the useful metadata
def getMetadata(pdfObject):
    metadata = pdfObject.get_metadata()
    paper_metadata = {}
    if 'doi' in metadata:
        paper_metadata['doi'] = metadata['doi']
    if 'dc' in paper_metadata:
        if 'creator' in paper_metadata['dc']:
            paper_metadata['authors'] = metadata['dc']['creator']
        if 'subject' in paper_metadata['dc']:
            paper_metadata['keywords'] = metadata['dc']['subject']
    if 'Title' in metadata:
        paper_metadata['title'] = metadata['Title']
    if 'CreationDate' in paper_metadata:
        paper_metadata['pubDate'] = int(metadata['CreationDate'][2:6])
    return paper_metadata

#cleans the text.
def cleanText(text):
    # will initally remove newlines to get rid of weird formatting
    text = text.replace('\r', '').replace('\n', '')
    #splitting on "." splits the work into sentences
    return text.split(".")
    ##Need to do more on cleaning figures.
