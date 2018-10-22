import fitz as mu
import pandas as pd
import unidecode as unidecode

def extract(fileName):
    if (fileName.endswith(".pdf")):
        next
    else:
        fileName += ".pdf"

    doc = mu.open(fileName)
    pages = len(doc)
    pdfText = ""
    for page in doc:
        pdfText += page.getText()

    #pdfText = pdfText.replace('\r', '').replace('\n',
    print(pdfText)
    #print(type(pdfText))

    return "".join(pdfText)



def extract_title(csv_dataframe,pdf):
    lines = pdf.split('\n')
    authorsList = pd.read_csv(csv_dataframe, sep=',',encoding='UTF-8')
    #print(authorsList)
    #print(type(lines))
    #ist(map(lambda x: x**2, items))
    firstLine=list(map(lambda x:unidecode.unidecode(x),lines[:3]))
    print(firstLine)
    #print(str(authorsList['title']).lower())
    for title in authorsList['title']:
        for t in firstLine:
            #print(title)
            #print(t)
            if title.lower() in t.lower():
                print('titi')

    #if any(st in str(firstLine.lower()) for st in str(authorsList['title']).lower()):
        #print('hello')
    #if 'Recherche dans de grandes bases'.lower() is str(authorsList['title']).lower():

        #print('its ok')

    # for l in lines:
    #     #print(l)
    #     name=l.split(',')
    #     for n in name:
    #         print(n)
    #         print(authorsList['authors'])
    #         if 'dumitru'.lower() is str(authorsList['authors']).lower():
    #             print('titi')
    #             print(l)

