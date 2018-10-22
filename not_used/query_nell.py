import requests
import json
import xml.etree.ElementTree as ET
import re

def query_nell():
    resp = requests.get("http://rtw.ml.cmu.edu/rtw//api/json0?ent1=&lit1=Obama&predicate=*&ent2=*&lit2=&agent=KI%2CCKB%2COPRA&format=raw")
    results = resp.json()
    print(results)
    #print("ttototoototo"+str(r['type']) for r in results['data'])
    #return [str(r['id']) for r in results['data']]



query_nell()



