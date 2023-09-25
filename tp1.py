from pyld import jsonld
import json

a = open("out.json")
raw_doc = json.load(a)

b = open("context.json")
ctx = json.load(b)


result =jsonld.to_rdf(raw_doc, {
    'expandContext': ctx,  # contexte à appliquer
    'format': 'application/n-quads', # format de sortie
})
print (result)