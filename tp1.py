

jsonld.to_rdf("out.json", {
    'expandContext': "context.json",  # contexte à appliquer
    'format': 'application/n-quads', # format de sortie
}))