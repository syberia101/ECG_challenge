import analyse_data.read_csvForName as readCSV
import predict_name_gender.name_file_transform as predictName
import analyse_data.create_publication_dataframe as dataframePub
import analyse_data.analyse_gender as analyseG
import dblp_extraction.read_DBLP_dump as dblpE
import dblp_extraction.extract_from_dblp as dblpExtract



path_root='/Users/derib/PycharmProjects/EGCDefi/data/'
path_data_process=''
path_export_plot=''
path_dblp_dump_xml=''
path_male_female_files=''



#Needed when we don't have the list of name clenead, but when all that is done once, doesn't need to do it more
def clean_names_csv():
    dfname_france_female,dfname_france_male = predictName.french_name_to_dataFrame(path_root+'male_female_name/names_raw_data/france_name.csv')
    df_nameUK_female,df_nameUK_male = predictName.processed_csv_name (path_root+'male_female_name/names_raw_data/ukprocessed.csv')
    df_nameUS_female,df_nameUS_male = predictName.processed_csv_name (path_root+'male_female_name/names_raw_data/usprocessed.csv')
    predictName.concact_all_dataframe(path_root+'male_female_name/allNameConcatMale.csv',dfname_france_male,df_nameUK_male,df_nameUS_male)
    predictName.concact_all_dataframe(path_root+'male_female_name/allNameConcatFemale.csv',dfname_france_female,df_nameUK_female,df_nameUS_female)
    read = readCSV.ReadCSV_forName(path_root+"male_female_name/allNameConcatFemale.csv",path_root+"male_female_name/allNameConcatMale.csv")
    allName = read.create_both_sex_name_file()
    read.drop_same_name_bothGender_male(allName,path_root+'male_female_name/onlyMale.csv')
    read.drop_same_name_bothGender_female(allName,path_root+'male_female_name/onlyFemale.csv')
    read.concat_all_nameFile(path_root+"male_female_name/bothSexFileClean.csv",path_root+"male_female_name/onlyMale.csv",path_root+"male_female_name/onlyFemale.csv")

#change the name of the fileName for changing the corpus to analyse
def prepare_dataframe_publication(file_name):

    dataframePublication = dataframePub.merge_dataframe_publication_with_names_on_prenom(path_root+'dblp_processed/'+file_name+'.csv',path_root+'male_female_name/bothSexFileClean.csv')
    #print(dataframePublication)
    return dataframePublication

def prepare_dataframe_publication_without_Sex(file_name):

    dataframePublication = dataframePub.csv_to_dataframe\
        (path_root+'dblp_processed/'+file_name+'.csv')
    #print(dataframePublication)
    return dataframePublication

def read_dblp(conf_name, file_name):
    ##/Users/derib/PycharmProjects/EGCDefi/data/dblp_dump/dblp.xml
    ##read the dblp

    dblp=dblpE.read_DBLP_dump(path_root)
    ##prepare the json file

    dblp.parse_dblp('dblp_dump/dblp.xml',conf_name,'dblp_processed/'+file_name)
    ##read the json_file

    dblpExtract.readJsonFile_createDataFrameFromCSV(path_root+'dblp_processed/'+file_name+".json",path_root+'dblp_processed/'+file_name+'.csv',path_root+'dblp_processed/'+file_name+'onlyPrenom.csv')


def main():
    conf_name='mldm'
    read_dblp('conf/'+conf_name+'/','conf_'+conf_name)
    df = prepare_dataframe_publication('conf_'+conf_name)
    df_without_sex = prepare_dataframe_publication_without_Sex('conf_'+conf_name)
    print(df_without_sex)
    #print(df)
    #mesure the number of women man in a conference
    analyseG.all_female_male_authorV2(df,path_root+"export_plot/allFemaleMaleAuthors_"+conf_name+".png")
    #mesure the percentage first author, women man
    analyseG.first_author_female_male(df,path_root+"export_plot/FirstFemaleMaleAuthors_"+conf_name+".png")
    #mesure the nb of times of one author
    analyseG.get_author_nbTimes_publish_without_sex(df_without_sex,1,
    path_root+"export_plot/nb_authorPublication_without_sex"+conf_name+".png",path_root+"dblp_processed/nb_authorPublication_without_sex_"+conf_name+".csv")




if __name__ == '__main__':
    main()
