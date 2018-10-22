import json
import pandas as pd

def readJsonFile_createDataFrame(pathFile,full_file_cvs_allData, onlyPrenomfromDBLP):
    row_list =[]
    with open(pathFile, 'r') as f:
        j = json.load(f)
        for a in (j['result']['hits']['hit']):
            a_data=a['info']['authors']['author']
            if type(a_data) is list:
                for index,author_in_list in enumerate (a_data):

                    #row_list.append(dicto)
                    print(author_in_list)
    df=pd.DataFrame(row_list)
    df.to_csv(full_file_cvs_allData)
    df_small=df.loc[:,['prenom']]
    df_small=df_small.drop_duplicates(keep="first", inplace=False)
    df_small.index.name = 'index'
    #df_small.to_csv(onlyPrenomfromDBLP)
    print(df)
    return df

readJsonFile_createDataFrame('/Users/derib/Desktop/Downloads/procedessing.json','titiit','tititi')
