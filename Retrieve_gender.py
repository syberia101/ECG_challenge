import pandas as pd
import retrieve_gender_dbpedia as rgd
import matplotlib.pyplot as plt
import numpy as np
import unidecode as unidecode
desired_width = 300
pd.set_option("display.max_columns", 9)
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)




def look_both_gender_name(femaleNameFile, maleNameFile,exitFile):
    female_dataframe = pd.read_csv(femaleNameFile)
    male_dataframe = pd.read_csv(maleNameFile)
    df=pd.merge(female_dataframe, male_dataframe, on=['prenom'], how='inner')
    df.drop('Unnamed: 0_x', axis=1, inplace=True)
    df.drop('Unnamed: 0_y',axis=1, inplace=True)
    df['sex'] = 'bothSex'
    df.drop('sex_x',axis =1 , inplace=True)
    df.drop('sex_y',axis =1 , inplace=True)
    df.to_csv(exitFile)


def drop_name_bothGender(bothSexFile,oneSexFile,exitFile):
    bothSexdataFrame = pd.read_csv(bothSexFile)
    oneSexdataFrame = pd.read_csv(oneSexFile)
    oneSexdataFrame=oneSexdataFrame[~oneSexdataFrame.prenom.isin(bothSexdataFrame.prenom)]
    oneSexdataFrame.drop('Unnamed: 0',axis=1, inplace=True)
    print(oneSexdataFrame)
    oneSexdataFrame.to_csv(exitFile)

def concat_all_nameFile(fileExit,*args):
    frames = []
    for i in args:
        print('file',i)
        df = pd.read_csv(i)
        frames.append(df)
    df = pd.concat(frames,axis=0, sort=False, ignore_index=True)
    df.to_csv(fileExit)

#merge the data_frame from DBLP to the data_frame with the name (prenom, sex)
#normalizing the name with accent
def retrieve_gender_fromfile(dataFrameDBLP,allNameConcat):
    allNameConcat_dataFrame = pd.read_csv(allNameConcat)
    allNameConcat_dataFrame.drop('index',axis=1, inplace=True)
    #print('lenght of the len allNameConcat_dataFrame ',len(allNameConcat_dataFrame))
    #print(allNameConcat_dataFrame.columns.values)
    allNameConcat_dataFrame['prenom']=allNameConcat_dataFrame['prenom'].apply(lambda x:unidecode.unidecode(x))
    dataFrameDBLP['prenom']=dataFrameDBLP['prenom'].apply(lambda x:unidecode.unidecode(x))
    df=dataFrameDBLP.merge(allNameConcat_dataFrame, left_on="prenom", right_on="prenom")
    df=df.sort_values(by=['authors'])
    df = df.drop_duplicates(keep="first", inplace=False)
    return df

#pourcentage of women/man being part of a paper in a year
def all_female_male_author(df,namePlot):
    dfYear=df.groupby(['sex','year']).count()
    print(dfYear['authors'])
    dfYearAuthor=pd.DataFrame()
    dfPourcentageFemale=dfYear.loc['Female']/(dfYear.loc['Female']+dfYear.loc['Male'])
    dfPourcentageMale=dfYear.loc['Male']/(dfYear.loc['Female']+dfYear.loc['Male'])
    dfYearAuthor['female_Author'] = dfPourcentageFemale['authors']
    dfYearAuthor['Male_Author'] = dfPourcentageMale['authors']
    #print(dfYearAuthor)
    dfYearAuthor.reset_index(drop=True)
    fig=dfYearAuthor.plot.bar().get_figure()
    plt.ylim(0, 1)
    #plt.ylabel('Y Axis limit is (-0.5,100)')
    plt.show()
    fig.savefig(namePlot)
    plt.close()

#save a csv with the name_author in a list
def authorList_dataframe(df,pathFile):
    df['first_author_sex']=df['sex'][df['rank_author']==1]
    dfAuthorListAll=df.groupby(['title']).agg(lambda x: x.tolist())
    dfAuthorListAll.to_csv(pathFile)

#pourcentage of women writing as first author
def first_author_female_male(df,namePlot):
    df['first_author_sex']=df['sex'][df['rank_author']==1]

    dfFirstAuthor=df.dropna()
    print('dfFirstAuthor')
    print(dfFirstAuthor)

    dfYearAuthorFirst=dfFirstAuthor.groupby(['first_author_sex','year']).count()
    df_percentage_author=pd.DataFrame()
    dfPourcentageFemaleFirstAuthor=dfYearAuthorFirst.loc['Female']/(dfYearAuthorFirst.loc['Female']+dfYearAuthorFirst.loc['Male'])
    dfPourcentageMaleFirstAuthor=dfYearAuthorFirst.loc['Male']/(dfYearAuthorFirst.loc['Female']+dfYearAuthorFirst.loc['Male'])
    # print(dfPourcentageFemaleFirstAuthor)
    df_percentage_author['Percentage_female_first_Author'] = dfPourcentageFemaleFirstAuthor['authors']
    df_percentage_author['Percentage_Male_first_Author'] = dfPourcentageMaleFirstAuthor['authors']
    print(df_percentage_author)
    # df_percentage_author.reset_index(drop=True)
    fig=df_percentage_author.plot.bar().get_figure()
    plt.ylim(0, 1)
    fig.savefig(namePlot)
    plt.show()


#extract paper with only one author
def only_one_author(df,name_plot):
    #print('only one author')
    #dfAuthorListAll=df.groupby(['title']).count().reset_index()
    df_oneAuthor=df.groupby(['title'])['authors'].count().reset_index()
    #df_i=df_oneAuthor[df_oneAuthor['title']=='Une nouvelle approche de la programmation DC et DCA pour la classification floue.']
    df.reset_index()
    #print(df_i)
    #print(df_oneAuthor)
    df_oneAuthor=df_oneAuthor[df_oneAuthor['authors'] == 1]
    df_oneAuthor.rename(columns={'authors': 'nb_authors'},inplace=True)
    df_oneAuthor.reset_index()

    #print(df_oneAuthor)
    df1=pd.merge(df_oneAuthor,df,on="title",how='outer').dropna()
    print(df1)
    dfC=df1.groupby(['sex','year']).count().unstack()
    dfC=dfC.fillna(0)
    #print(dfC.index)
    print(dfC)
    only_one_author_df = pd.DataFrame()
    dfc_women = dfC.loc['Female']
    dfc_man = dfC.loc['Male']
    print('dfcowmen ',dfc_women['title'])
    only_one_author_df['woman']=dfc_women['title']
    only_one_author_df['man']=dfc_man['title']
    print(only_one_author_df)
    #fig=dfC['title'].T.plot.bar().get_figure()
    fig = only_one_author_df.plot.bar().get_figure()
    plt.show()
    fig.savefig(name_plot)


def get_author_nb_pub(df):
    print(df)
    df=df.groupby(['authors','sex','rank_author']).count()
    df=df.sort_values(by=['authors'])
    print(df['title'])








    # df_pourcentage_women = dfC.loc['Female']
    # df_pourcentage_women.index.rename('year')
    # df_pourcentage_women['sex']='Female'
    # df_pourcentage_women.reset_index(inplace=True)
    #
    # df_pourcentage_male = dfC.loc['Male']
    # df_pourcentage_male.index.rename('year')
    # df_pourcentage_male['sex']='Male'
    # df_pourcentage_male.reset_index(inplace=True)
    # #df_pourcentage_women.set_names(["year"], inplace=True)
    # print(df_pourcentage_women)
    #
    # df_percentage_author_onlyOneAuthor=pd.merge(df_pourcentage_women,df_pourcentage_male,how='outer')
    # df_percentage_author_onlyOneAuthor.drop(['title','nb_authors','nom','prenom','rank_author'],axis=1,inplace=True)
    # print("df_percentage_author_onlyOneAuthor")
    #print(df_percentage_author_onlyOneAuthor)
    # df_percentage_author_onlyOneAuthor['Percentage_female_first_Author'] = df_pourcentage_women['authors']
    # df_percentage_author_onlyOneAuthor['Percentage_Male_first_Author'] = df_pourcentage_male['authors']
    # print (df_percentage_author_onlyOneAuthor)
    #fig, ax = plt.subplots()

    #ax = df_pourcentage_male['title'].plot(kind='bar')
    #df_pourcentage_women['title'].plot(ax=ax)
    # df_pourcentage_male.plot(ax=ax, kind='bar')
    # df_pourcentage_women['title'].plot(ax=ax,kind='bar')
    # df_pourcentage_male['title'].plot(ax=ax,kind='bar')
    #plt.show()



    # df2=pd.DataFrame(dfC['nb_authors']).reset_index()
    # print(df2)
    # fig, ax = plt.subplots()
    # df2.groupby('sex').plot(x='year',y='nb_authors',ax=ax,kind='bar')
    # plt.show()


    #dfAuthorListAll = dfAuthorListAll['title','authors']
    #df_oneAuthor.merge(df, left_on="title", right_on="title")
    #df['age'] > 50
    #print(df_oneAuthor)

    #print(df)
    #print(df['authors'].groupby(df['sex','year']))
    #print('title',df['rank_author'].groupby(df['sex']).count())
    #print(df.groupby(['sex','year']).count().add_prefix('_count'))
    #print(df['year'].groupby(df['sex','title']).count())
    #combien de titre sont écrit par des Femmes vs des Male
    #print('print dfffff',df['title'][df['sex'] == 'Male'].count())
    #print(len(df.groupby(['sex','year']).groups.keys()))
    #print(len(df.groupby(['sex','year']).groups['Female']))
    #print(len(df.groupby(['sex']).groups['Male']))
    #print(df.groupby('year').count())
    #dfYear['total']=df.groupby('year').count()
    #dfYear.drop(['nom','title','prenom','rank_author'],axis=1,inplace=True)

    #print(df.groupby(['sex','year']).describe())
    #print(dfYear)
    #dfYear['average']=dfYear['authors']
    #print(df.groupby(['sex','rank_author']).describe())
    #group_by_rankAuthor=df.groupby(['sex','rank_author']).describe()
    #group_by_rankAuthor.to_csv('/Users/derib/Desktop/rank_author.csv')
    # df['authorss']=df.loc[df.groupby('sex').count()/df.groupby(['year']).count()]
    # print(df.loc['authorss'])
    #print(len(df))
    #df.to_csv('/Users/derib/Desktop/allConcatNameRetrieveName.csv')




