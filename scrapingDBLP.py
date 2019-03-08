from readFromJsonDBLN.dblp_python_me import *

from readFromJsonDBLN.load_readJsonDBLP import *
import pandas as pd
import json

COL_NAME_AUTHOR_TABLE = ['year_pub','author_name','author_prenom','title']
def transform_in_pandas():

    df = pd.DataFrame(columns=COL_NAME_AUTHOR_TABLE)





def get_author_form_json(pathFile):
    listAuthor=readJsonFile(pathFile)
    dict={}
    for l in listAuthor:
        if type(l) is list:
            for a in l:
                a.split()

        else:
            print(l.split())



def main():
    #get_author_form_json('/Users/derib/Desktop/ecg_conf_2001.json')
    #jsonF=readJsonFileOnly('/Users/derib/Desktop/ecg_conf_2001.json')



    listAuthor=readJsonFile_createDataFrame('/Users/derib/PycharmProjects/EGCDefi/ECG_Challenge/dblpFile/procedessing_icse.json')
    # print(type(listAuthor))
    # word = []
    # for a in listAuthor:
    #     if type(a) is list:
    #         try:
    #             for a_l in a:
    #
    #                 author_dble=search(str(a_l))
    #
    #             if len(author_dble)>0 :
    #                     nameA=author_dble[0]
    #                     print(a_l," author",nameA.name)
    #                     print(len(nameA.publications))
    #                     publicationA = nameA.publications
    #                     try:
    #                         if(len(publicationA)>0):
    #                             for p in publicationA:
    #                                 print(p.title)
    #                                 word.append(p.title.split())
    #                     except:
    #                         print('erooro')
    #
    #         except:
    #                 print('error ',p.title)
    #
    #     else:
    #         author_dble=search(str(a))
    #         try:
    #             if len(author_dble)>0:
    #                 nameA=author_dble[0]
    #                 print(nameA," author tout seul ",nameA.name)
    #                 print(len(nameA.publications))
    #
    #         except:
    #             print('error ',author_dble)
    #
    # print ('list mot '+word)





    #author =  search('Hélène de Ribaupierre')
    #ecg = search_ecg()
    #print(ecg[0])
    # helene = author[0]
    # print("author ",helene.name)
    # print(len(helene.publications))
    # print(helene.publications[2].title)
    # print(helene.publications[2].journal)
    # print(helene.publications[2].ee)
    # print("publisher",helene.publications[2].publisher)
    # print("citations ",helene.publications[2].citations)

if __name__ == '__main__':
    main()

