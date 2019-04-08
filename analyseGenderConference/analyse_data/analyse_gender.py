import pandas as pd


import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import seaborn as sns

#import matplotlib.pyplot as plt
import numpy as np
import unidecode as unidecode
desired_width = 300
pd.set_option("display.max_columns", 9)
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)


#pourcentage of women/man being part of a paper in a year
def all_female_male_authorV2(df,namePlot):
    dfYear =df.groupby(['sex','year']).count()
    dfYear = dfYear['authors']
    df = dfYear.unstack()
    df = df.fillna(0)
    dfPourcentageMale=df.loc['Male']/(df.loc['Female']+df.loc['Male'])
    dfPourcentageMale=dfPourcentageMale.fillna(0)
    dfPourcentageFemale=df.loc['Female']/(df.loc['Female']+df.loc['Male'])
    dfPourcentageFemale=dfPourcentageFemale.fillna(0)
    dfYearAuthor = pd.DataFrame()
    dfYearAuthor['female_Author'] = dfPourcentageFemale
    dfYearAuthor['Male_Author'] = dfPourcentageMale
    dfYearAuthor.reset_index(drop=True)
    #dfYearAuthor=dfYearAuthor.fillna(0)
    #print(dfYearAuthor)
    fig=dfYearAuthor.plot.bar().get_figure()
    plt.ylim(0, 1)
    plt.ylabel('Y Axis limit is (-0.5,100)')
    plt.show()
    fig.savefig(namePlot)
    plt.close()

#pourcentage of women writing as first author
def first_author_female_male(df,namePlot):
    #print(df[df['year']==1994].sort_values(by=['title']))
    df['first_author_sex'] = df['sex'][df['rank_author']==1]
    #dfFirstAuthor=df.dropna()
    dfYearAuthorFirst=df.groupby(['first_author_sex','year']).count()
    dfYearAuthorFirst = dfYearAuthorFirst['authors']
    df = dfYearAuthorFirst.unstack()
    df = df.fillna(0)
    dfPourcentageMale=df.loc['Male']/(df.loc['Female']+df.loc['Male'])
    dfPourcentageMale=dfPourcentageMale.fillna(0)
    dfPourcentageFemale=df.loc['Female']/(df.loc['Female']+df.loc['Male'])
    dfPourcentageFemale=dfPourcentageFemale.fillna(0)
    dfYearFirstAuthor = pd.DataFrame()
    dfYearFirstAuthor['female_Author'] = dfPourcentageFemale
    dfYearFirstAuthor['Male_Author'] = dfPourcentageMale
    dfYearFirstAuthor.reset_index(drop=True)
    print(dfYearFirstAuthor)
    fig=dfYearFirstAuthor.plot.bar().get_figure()
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
    df=df.groupby(['authors','sex','rank_author']).count()
    df=df.sort_values(by=['authors'])
    df = df['title']
    df1 = df.reset_index()
    df1 = df1.rename(index=str,columns={"authors":"authors","sex":"sex","rank_author":"rank_author","title":"nbTimes"})
    print(df1)
    return df1


def get_author_nbTimes_publish(df,nbPublication,name_plot):
    df = get_author_nb_pub(df)
    df = df.groupby(['authors','sex']).nbTimes.agg({'nbTimesSum':'sum'})
    df = df[df['nbTimesSum']>nbPublication]
    df = df.reset_index()
    df = df.groupby(['nbTimesSum','sex']).count().unstack()
    df = df.fillna(0)
    df = df.reset_index()
    print(df)
    #sex={'Male':1,'Female':2, 'UKN':3}
    #df['sex']=[sex[item] for item in df['sex']]
    df = df.rename(index=str,columns={'authors':'nbAuthors'})


    #dfMale = df[df['sex']=='Male']
    #dfFemale = df[df['sex']=='Female']

    fig1 = df.plot.bar(x='nbTimesSum',y='nbAuthors').get_figure()
    #fig2 = dfFemale.plot.bar(ax=fig1,x='nbAuthors',y=['nbTimesSum']).get_figure()

    plt.show()
    fig1.savefig(name_plot)
    return df


