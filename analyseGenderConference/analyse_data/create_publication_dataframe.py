import pandas as pd

import unidecode as unidecode


def merge_dataframe_publication_with_names_on_prenom(fileCSV, allNameConcat):
    conference_dataFrame = pd.read_csv(fileCSV)
    allNameConcat_dataFrame = pd.read_csv(allNameConcat)
    #allNameConcat_dataFrame['prenom'] = allNameConcat_dataFrame['prenom'].apply(lambda x: unidecode.unidecode(x))
    #print(conference_dataFrame['prenom'])
    #conference_dataFrame['prenom'] = conference_dataFrame['prenom'].apply(
    #    lambda x: unidecode.unidecode(x) if type(x) != float else x)
    df = pd.merge(allNameConcat_dataFrame, conference_dataFrame, on="prenom", how='inner')
    df = df.sort_values(by=['authors'])
    df = df.drop(['Unnamed: 0_x','Unnamed: 0_y'],axis=1)
    df = df.drop_duplicates(keep="first", inplace=False)
    df.to_csv('/Users/derib/PycharmProjects/EGCDefi/data/publication_csv_withGender/allPublicationsTest.csv')
    return df


