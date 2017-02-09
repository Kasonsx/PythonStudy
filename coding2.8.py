# -*- coding:utf-8 -*-
import requests
params = {'firstname':'Kason','lastname':'Sun'}
r = requests.post("http://pythonscraping.com/files/prcessing.php",data=params)
print(r.text)