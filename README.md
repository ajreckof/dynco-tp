# DynCo-tp

TP réalisé par Timothé Bonhoure et Christophe Martinez.

## Dépot GitHub extrait

https://github.com/pchampin/sophia_rs

## Validation SHACL

Initialement, nous avions une erreur sur la `s:endDate` des `ex:ClosedIssue` qui n'était pas de type `xsd:dateTimeStamp`.  
Après correctif, plus aucune erreur.

## Archive

- `context.json` : contient le contexte pour générer le graphe RDF
- `out.json` : la trace brute
- `rdf.ttl` : le graphe RDF généré
- `export2rdf.py` : le script pour générer le graphe RDF