import json
import pandas as pd
import re




def readJsonFile_createDataFrameFromCSV(pathFile,full_file_cvs_allData, onlyPrenomfromDBLP):
    row_list =[]
    with open(pathFile, encoding='utf-8') as f:
        j = json.load(f)
        for a in j:
            #print(str(a['author']))
            print(type(a['title']))

        for a in j:
            a_data=a['author']
            #a_data=a['info']['authors']['author']
            if type(a_data) is list:
                for index,author_in_list in enumerate (a_data):
                    dicto=creatDic(author_in_list,a,index+1)
                    print(dicto)
                    row_list.append(dicto)
                    #print(dicto)
            else:
                dicto=creatDic(a['author'],a,1)
                row_list.append(dicto)
                #print(dicto)
    df=pd.DataFrame(row_list)
    df.to_csv(full_file_cvs_allData)
    df_small=df.loc[:,['prenom']]
    df_small=df_small.drop_duplicates(keep="first", inplace=False)
    df_small.index.name = 'index'
    df_small.to_csv(onlyPrenomfromDBLP)
    #print(df)
    return df

def creatDic(author,other,rank_author):
    dicto={}
    authorS = author.split()
    #dicto['year']=other['year']
    for y in other['year']:
        dicto['year']=y
    dicto['authors']=author
    if len(authorS)>1:
        print('in the if', len(dicto), dicto)
        dicto['prenom']=str(authorS[0])
        dicto['nom']=str(authorS[1])
        dicto['rank_author']=rank_author
    else:
        print('in the else')
        dicto['prenom']=authorS[0]
        dicto['rank_author']=rank_author
    #dicto['title']=other['title']
    for t in other['title']:
        dicto['title']=t
    return dicto
