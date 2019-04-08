import read_extract_dblp.loadJsonDBLP as rj
import name_extraction.retrieve_gender_dbpedia as db
import analyse_data.Retrieve_gender as rg
#import matplotlib.pyplot as plt
import read_extract_dblp.read_ECG_document as readECG
import read_pdf.PDFX as pdfx



def main():
    # /Users/derib/PycharmProjects/EGCDefi/ECG_Challenge/dblpFile/procedessing_icse.json

    path_root='/Users/derib/PycharmProjects/EGCDefi/data/ECG_Challenge/dblpFile/'
    #listAuthor = rj.readJsonFile_createDataFrameFromCSV(path_root+'procedessing_icse.json',path_root+'procedessing_icse.csv',path_root+'only_prenom_ICSE.csv')
    listAuthor = rj.readJsonFile_createDataFrameFromCSV(path_root+'procedessing_icse.json',path_root+'procedessing_icse.csv',path_root+'procedessing_icse_onlyPrenom.csv')

    #listAuthor = rj.readJsonFile_createDataFrame('/Users/derib/PycharmProjects/EGCDefi/data/ECG_Challenge/dblpFile/procedessing_icse.json',' /Users/derib/PycharmProjects/EGCDefi/data/ECG_Challenge/dblpFile/procedessing_icse.csv',' /Users/derib/PycharmProjects/EGCDefi/data/ECG_Challenge/dblpFile/onlyPrenomICSE.csv')

    print(listAuthor['authors'])
    ##extract the name of the author from the dataFrame
    #listAuthor['prenom'].to_csv('/Users/derib/Desktop/listAuthorDBLP.cvs')
    #rj.retrieve_gender_fromdbpedia_dict('/Users/derib/Desktop/femaleName.json')
    #rj.retrieve_gender(listAuthor)
    #rj.retrieve_gender_fromfile('/Users/derib/Desktop/femaleName.txt',listAuthor)
    '''
    This is to use when need a new female list name, if not, just load the json file
    '''
    #dict_female = db.get_gender_name_dict_female(1000,100000)
    # #db.save_dict_json('/Users/derib/Desktop/femaleName.json',dict_female)
    # #db.save_set('/Users/derib/Desktop/femaleName.txt',dict_female)
    #db.saveCSV('/Users/derib/Desktop/femaleName.cvs',dict_female)
    #
    #dict_male = db.get_gender_name_dict_male(1000,100000)
    # #db.save_dict_json('/Users/derib/Desktop/femaleName.json',dict_female)
    #db.saveCSV('/Users/derib/Desktop/maleName.cvs',dict_male)
    # #db.save_dict_json('/Users/derib/Desktop/maleName.txt',dict_male)

    #rg.retrieve_gender_fromfile("toto","ttiti","/Users/derib/Desktop/maleName.cvs")
    #rg.look_both_gender_name("/Users/derib/Desktop/femaleName.cvs","/Users/derib/Desktop/maleName.cvs","/Users/derib/Desktop/bothSexName.cvs")
    #rg.drop_name_bothGender("/Users/derib/Desktop/bothSexName.cvs","/Users/derib/Desktop/femaleName.cvs","/Users/derib/Desktop/femaleCleaned.cvs")
    #rg.drop_name_bothGender("/Users/derib/Desktop/bothSexName.cvs","/Users/derib/Desktop/maleName.cvs","/Users/derib/Desktop/maleCleaned.cvs")
#
    #rg.concat_all_nameFile('/Users/derib/Desktop/allConcatName.csv','/Users/derib/Desktop/maleCleaned.cvs', '/Users/derib/Desktop/femaleCleaned.cvs',  '/Users/derib/Desktop/bothSexName.cvs')

    #df=rg.retrieve_gender_fromfile(listAuthor,path_root+'ECG_Challenge/predictionNameBayesCorrected.csv')

    #df=rg.retrieve_gender_fromfile(listAuthor,path_root+'predictionNameBayesCorrected.csv')

    # rg.all_female_male_author(df,'/Users/derib/Desktop/ECG_Challenge/plot1ECG')
    # rg.authorList_dataframe(df,'/Users/derib/Desktop/authorListAll.csv')
    # rg.first_author_female_male(df,'/Users/derib/Desktop/ECG_Challenge/plot2ECG')
    # rg.only_one_author(df,'/Users/derib/Desktop/ECG_Challenge/plot3ECG')
    #rg.get_author_nb_pub(df)

    #file=readECG.Document_ECG(path_root+'pdf/100162/1002106.pdf')
    #file.extractFilePdf()
    #print(file.references)

    #file=readECG.extractFilePdf(path_root+'pdf/100162/1002106.pdf',path_root+'pdf/4586/1000895.txt')
    #readECG.extract_title(path_root+'authorListAll.csv',file)


    # #rj.read_json_from_xmlDump('/Users/derib/Downloads/procedessingIC.json','/Users/derib/Downloads/procedessingIC.csv')
    #rj.read_json_from_xmlDump(path_root+'/procedessing_icse.json',path_root+'/procedessing_icse.csv',path_root+'only_prenom_icse.csv')
    #df = rg.retrieve_gender_fromfileV2(path_root+'/procedessing_icse.csv',path_root+'/predictionNameBayesCorrected.csv')

    #df=rg.retrieve_gender_fromfile(listAuthorIC,path_root+'/predictionNameBayesCorrected.csv')
    #print(df)

    #
    # file=readECG.extract('/Users/derib/Desktop/ECG_Challenge/4586/1000895.pdf')
    # readECG.extract_title('/Users/derib/Desktop/authorListAll.csv',file)
    #
    #
    # #rj.read_json_from_xmlDump('/Users/derib/Downloads/procedessingIC.json','/Users/derib/Downloads/procedessingIC.csv','titit')
    # listAuthorIC = rj.read_json_from_xmlDump('/Users/derib/Desktop/procedessingIC.json','/Users/derib/Desktop/procedessingIC.csv','/Users/derib/Desktop/ECG_Challenge/only_prenom_IC.csv')
    #df=rg.retrieve_gender_fromfile(listAuthorIC,'/Users/derib/Desktop/ECG_Challenge/predictionNameBayesCorrected.csv')
    #
    #rg.all_female_male_author(df,'/Users/derib/Desktop/ECG_Challenge/plot1IC')
    # #rg.authorList_dataframe(df,'/Users/derib/Desktop/authorListAllIC.csv')
    # #rg.first_author_female_male(df,'/Users/derib/Desktop/ECG_Challenge/plot2IC')
    # #rg.only_one_author(df,'/Users/derib/Desktop/ECG_Challenge/plot3IC')
    #df = rg.get_author_nb_pub(df)
    #df = rg.normalise_gender(df)

    #rg.predict_author_sex(df)
    #rg.predict_firstAuthor(df)

if __name__ == '__main__':
    main()
