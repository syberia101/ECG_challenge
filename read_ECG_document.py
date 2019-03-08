import fitz as mu
import pandas as pd
import unidecode as unidecode
import unicodedata
from tika import parser
import os
import os.path
from bs4 import BeautifulSoup

class Document_ECG:

    title=""
    authors=""
    document=""
    year=""
    references=""
    def __init__(self,path_doc):
        self.path_doc=path_doc


    #from this page:https://stackoverflow.com/questions/34837707/how-to-extract-text-from-a-pdf-file
    def extractFilePdf(self):
        # tika_dir=os.path.join(os.path.dirname(__file__),'tika-app-1.19.jar')
        # os.system('java -jar '+tika_dir+' -t {} > {}'.format(fileName,filenNametxt))
        raw = parser.from_file(self.path_doc,xmlContent=True)
        #print(raw['metadata'])
        #print(raw['content'])
        soupText = BeautifulSoup(str(raw),'html.parser')
        body_tag= soupText.body
        p=[]
        para=body_tag.find_all('p')
        for pp in para:
            #print('ppppppp',pp)
            if ('Reference' or 'Reference') in pp:
                print('References ',pp)
            p.append(pp.text.replace('\\n',' '))
        #print(p)
        self.title=p[1:2]
        self.authors=p[2:3]
        for i,t in enumerate(p):
            if ('Reference' or 'Reference') in t:
                print(i,t)
        self.references=p[65:]
        self.document=p[6:]






    def extract(fileName):
        if (fileName.endswith(".pdf")):
            next
        else:
            fileName += ".pdf"

        doc = mu.open(fileName)
        pages = len(doc)
        print(doc.metadata)
        pdfText = ""
        for page in doc:
            pdfText += page.getText("xhtml")
            pdfText=pdfText.replace('&#x2019;','\'')
            pdfText=pdfText.replace('&#xb4;','')
            print (pdfText)


        #     pdfText = list(map(lambda x:unidecode.unidecode(x),pdfText))
        # print(pdfText)
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

