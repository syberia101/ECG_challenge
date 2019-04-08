import pandas as pd

def french_name_to_dataFrame(file):
    df = pd.read_csv(file)
    sex = {1:'Male',2:'Female'}
    df['sexe']=[sex[item] for item in df['sexe']]
    df = df.drop_duplicates(keep="first", inplace=False)
    df = df[df['preusuel'].str.len()>1]
    df = df.rename(index=str,columns={'sexe':'sex','preusuel':'prenom'})
    df['prenom'] = [x.title() for x in df['prenom']]
    df = df.reindex(sorted(df.columns),axis=1)
    df_female=df[df['sex']=='Female']
    df_male=df[df['sex']=='Male']
    print(df_female)
    return df_female,df_male


def processed_csv_name(file):
    df = pd.read_csv(file)
    df = df[df['Name'].str.len()>1]
    df['Name'] = [x.title() for x in df['Name']]
    df.drop(['years.appearing','upper','lower','count.male','count.female','obs.male','est.male'],axis=1,inplace=True)
    df.rename(index=str,columns={'prob.gender':'sex','Name':'prenom'},inplace=True)
    df = df.reindex(sorted(df.columns),axis=1)
    df_female=df[df['sex']=='Female']
    df_male=df[df['sex']=='Male']
    #print(df)
    return df_female,df_male

def concact_all_dataframe(fileExit,*args):
        frames = []
        for i in args:
            frames.append(i)
        df = pd.concat(frames,axis=0, sort=False, ignore_index=True)
        df.to_csv(fileExit)
        return df


