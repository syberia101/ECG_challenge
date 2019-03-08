import json
import pandas as pd


def readJsonFile_createDataFrame(pathFile,full_file_cvs_allData, onlyPrenomfromDBLP):
    row_list =[]
    with open(pathFile, 'r') as f:
        j = json.load(f)
        for a in j:
            print(a)
        for a in (j['result']['hits']['hit']):
            a_data=a['info']['authors']['author']
            if type(a_data) is list:
                for index,author_in_list in enumerate (a_data):
                    dicto=creatDic(author_in_list,a,index+1)
                    row_list.append(dicto)
                    #print(dicto)
            else:
                dicto=creatDic(a['info']['authors']['author'],a,1)
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

def readJsonFile_createDataFrameFromCSV(pathFile,full_file_cvs_allData, onlyPrenomfromDBLP):
    row_list =[]
    with open(pathFile, encoding='utf-8') as f:
        j = json.load(f)
        for a in j:
            print(str(a['author']))
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

def read_json_from_xmlDump(jsonFile, full_file_csv,onlyPrenomFromDBLP):
    row_list =[]
    with open(jsonFile, 'r') as f:
        j = json.load(f)
        #for a in j[:,]['title']:
        for a in j[0:]:
            #print(a['author'])
            #if len(a['author']) > 2:
            for index,author_in_list in enumerate (a['author']):
                    dicto=creatDic_fromXMLDump(author_in_list,a,index+1)
                    row_list.append(dicto)
                    #print(dicto)
            # else:
            #     dicto=creatDic_fromXMLDump(a['authors']['author'],a,1)
            #     row_list.append(dicto)
            #     print(dicto)
    df=pd.DataFrame(row_list)
    df.to_csv(full_file_csv)
    df_small=df.loc[:,['prenom']]
    df_small=df_small.drop_duplicates(keep="first", inplace=False)
    df_small.index.name = 'index'
    df_small.to_csv(onlyPrenomFromDBLP)
    #print(df)
    return df


def creatDic(author,other,rank_author):
    dicto={}
    authorS = author.split()
    dicto['year']=other['year']
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
    dicto['title']=other['title']
    return dicto


def creatDic_fromXMLDump(author,other,rank_author):
    dicto={}
    authorS = author.split()
    for y in other['year']:
        dicto['year']=y
    dicto['authors']=author
    dicto['prenom']=authorS[0]
    dicto['nom']=authorS[1]
    dicto['rank_author']=rank_author
    for t in other['title']:
        dicto['title']=t
    return dicto

