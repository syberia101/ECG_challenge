from SPARQLWrapper import SPARQLWrapper, JSON
import json
import pandas as pd


def get_gender_name_dict_female(offs,max):
    dict_female_prenom={}
    dict_female_prenom_complete={}
    set_female_name=set()
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    start=1
    while(start<max):
        sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX dbpedia:<http://dbpedia.org/resource/>
        PREFIX dbp:<http://dbpedia.org/property/>
        PREFIX foaf:<http://xmlns.com/foaf/0.1/>
    
       select ?pn ?gl ?gen Where{
        {
       SELECT ?pn ?gl ?gen
            WHERE {
             ?person a dbo:Person.
              ?person dbp:name ?pn.
              ?person foaf:gender ?gen.
              ?person rdfs:label ?gl.
        FILTER(((lang(?gl) = "en")||(lang(?gl) = "fr")) and (?gen = "female"@en)).
        }
        order by ASC(?gl)
            }
        }
        OFFSET """+str(start)+"""
        LIMIT 1000 """
        )
        #(lang(?gl) = "en")||
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        for result in results["results"]["bindings"]:
            #print('gl ',result["gl"]["value"])
            fe=result["gl"]["value"].replace(".","").split()
            set_female_name.add(fe[0].replace(',',""))
        start=offs+start
        print('offs '+str(start))
        print(sorted(set_female_name))
        print(len(set_female_name))
    for n in set_female_name:
        if len(n)>2:
            dict_female_prenom[n]='Female'
    #     print(dict_female_prenom)
    #     dict_female_prenom_complete['name']= dict_female_prenom
    return dict_female_prenom


def get_gender_name_dict_male(offs,max):
    dict_male_prenom={}
    dict_female_prenom_complete={}
    set_male_name=set()
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    #sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    start=1
    while(start<max):
        sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX dbpedia:<http://dbpedia.org/resource/>
        PREFIX dbp:<http://dbpedia.org/property/>
        PREFIX foaf:<http://xmlns.com/foaf/0.1/>
    
       select ?pn ?gl ?gen Where{
    {
       SELECT ?pn ?gl ?gen
            WHERE {
             ?person a dbo:Person.
              ?person dbp:name ?pn.
              ?person foaf:gender ?gen.
              ?person rdfs:label ?gl.
        FILTER(((lang(?gl) = "en")||(lang(?gl) = "fr")) and (?gen = "male"@en)).
    }
    order by ASC(?gl)
        }
    }
    
    
    
    OFFSET """+str(start)+"""
     LIMIT 1000""")

        sparql.setReturnFormat(JSON)

        results = sparql.query().convert()
        #print(results)
        for result in results["results"]["bindings"]:
            #print('gl ',result["gl"]["value"])
            fe=result["gl"]["value"].replace(".","").split()
            print(fe)
            set_male_name.add(fe[0].replace(',',""))
    #print(set_female_name)
    #print(len(set_female_name))
        start=offs+start
    print(len(set_male_name))
    for n in set_male_name:
        if len(n)>2:
            dict_male_prenom[n]='Male'
        #print(dict_male_prenom)
        #dict_female_prenom_complete['name']= dict_male_prenom
    return dict_male_prenom

def saveCSV(pathFile,data):
    #print(data)
    df=pd.Series(data)
    #print(df)
    df=df.to_frame().reset_index()
    df.columns = ['prenom','sex']
    df.to_csv(pathFile)

def save_dict_json(pathFile,data):
    with open(pathFile, 'w') as fp:
        json.dump(data, fp,ensure_ascii=False)

def save_set(pathFile,data):
    with open(pathFile,'w')as fp:
        fp.write("\n".join(data))



