BONHOURE Timothé et MARTINEZ Christophe

Lien du sujet : [champin.net](https://perso.liris.cnrs.fr/pierre-antoine.champin/2023/m2ia-tp-jsonld/part3.html)

1. Indiquez la requête SPARQL envoyée pour insérer cette information dans le dataset.

```
PREFIX ex: <http://example.com/ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
INSERT DATA {
    ex:OpenIssue rdfs:subClassOf ex:Issue .
    ex:ClosedIssue rdfs:subClassOf ex:Issue .
}
```

2. Indiquez la requête SPARQL envoyée.

```
PREFIX ex: <http://example.com/ns#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT (COUNT(?x) AS ?count)
WHERE {
  ?x rdf:type ex:Issue.
}
```

3. Indiquez le résultat obtenu.  
`"109"^^xsd:integer`

4. Indiquez la requête SPARQL envoyée.

```
PREFIX ex: <http://example.com/ns#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?x
WHERE {
  ex:Issue rdf:type ?x.
}
```

5. Indiquez le résultat obtenu.  

```
1	rdfs:Class
2	rdfs:Resource
3	owl:Thing
```

6. Expliquez à quoi correspondent les différents types, et comment ils ont été obtenus.  

`ex:Issue` est la classe des instances de `ex:ClosedIssue` et `ex:OpenIssue` donc est de type `rdfs:Class` et `rdfs:Class` est une sous-classe de `owl:Thing`, donc `ex:Issue` est de type `owl:Thing`. Comme `rdf:type` a pour `rdfs:domain` `rdfs:Resource` donc `ex:Issue` est une `rdfs:Resource`.

7. Indiquez la requête SPARQL envoyée pour insérer ces informations dans le dataset.

```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ex: <http://example.com/ns#>

INSERT DATA {
    ex:comment rdfs:domain ex:Issue.
    ex:comment rdfs:range ex:Comment.
    ex:label rdfs:domain ex:Issue.
    ex:label rdfs:range ex:Label.
    ex:issue rdfs:domain ex:Repository.
    ex:issue rdfs:range ex:Issue.
}
```

8. Indiquez les requêtes SPARQL envoyées.

```
PREFIX ex: <http://example.com/ns#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?x (Count(?y) as ?count)
WHERE {
   ?y rdf:type ?x.
   FILTER (?x IN (ex:Label, ex:Issue, ex:Comment))
} GROUPBY ?x
```

9. Indiquez les résultats obtenus.

```
ex:Label	"17"^^xsd:integer
ex:Issue	"109"^^xsd:integer
ex:Comment	"634"^^xsd:integer
```

10. Indiquez la requête SPARQL envoyée pour insérer cette information dans le dataset.

Nous avons tout d'abord essayer de réaliser cela en utilisant `SubClassOf` comme ci-dessous. 

```
PREFIX ex: <http://example.com/ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

INSERT DATA {
    ex:Label owl:disjointWith ex:Issue.
    ex:ClosedIssue owl:disjointWith ex:OpenIssue.
    ex:VisitorIssue rdfs:subClassOf ex:Issue;
                    owl:onProperty         ex:authorAssociation ;
                    owl:hasValue "NONE" .
    ex:VisitorOpenIssue owl:intersectionOf (ex:VisitorIssue ex:OpenIssue) .
}
```

Cependant, le problème est qu'owl utilisait les deux derniers triplet sans prendre en compte le `SubClassOf`. Ainsi il donnait le type de `ex:VisitorIssue` a des instances qui n'était pas des `ex:Issue`. Pour forcer que ce soit bien des `ex:Issue` nous avons utilisé `owl:intersectionOf` avec un blank node comme ci-dessous.

```
PREFIX ex: <http://example.com/ns#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

INSERT DATA {
    ex:Label owl:disjointWith ex:Issue.
    ex:ClosedIssue owl:disjointWith ex:OpenIssue.
    ex:VisitorIssue owl:intersectionOf (ex:Issue [
                    owl:onProperty 	ex:authorAssociation ;
                    owl:hasValue    "NONE"
    ]).
    ex:VisitorOpenIssue owl:intersectionOf (ex:VisitorIssue ex:OpenIssue) .
}
```


11. Indiquez la requête SPARQL envoyée pour insérer cette information dans le dataset.

```
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX s: <http://schema.org/>
    INSERT DATA {
        s:url a owl:InverseFunctionalProperty.
    }
```

12. Indiquez la requête SPARQL envoyée pour insérer cette information dans le dataset.

```
PREFIX ex: <http://example.com/ns#>
PREFIX s: <http://schema.org/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

INSERT DATA {
    s:contributor owl:propertyChainAxiom (ex:comment s:creator) 
}
```

13. Requêtez le dataset pour connaître le nombre de contributeurs qui ont commenté des tickets « visiteurs ».

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.com/ns#>
PREFIX s: <http://schema.org/>

SELECT (count(?x) as ?count) where { 
	?i rdf:type ex:VisitorIssue .
    ?i s:contributor ?x .
}
```

14. Indiquez le résultat obtenu.

`"48"^^xsd:integer`

15. Indiquez les requêtes SPARQL envoyées.

```
PREFIX ex: <http://example.com/ns#>
PREFIX s: <http://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

Select (Sample(?name) as ?names) (Count(Distinct(?comment)) as ?comments) (Count(Distinct(?contributor)) as ?contributors)
WHERE {
    ?issue s:name ?name;
    	   ex:comment ?comment;
           s:contributor ?contributor;
           rdf:type ex:VisitorOpenIssue
} GROUPBY ?issue
```

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ex: <http://example.com/ns#>
DELETE {
    ?x rdf:type ex:OpenIssue
} WHERE {
    ?x rdf:type ex:ClosedIssue
}
```



16. A l’aide de votre tableur préféré, construisez un graphique sur lequel vous ferez figurer, à chaque étape, les différents tickets et les nombres de commentateurs pour chacune d’eux.



17. Eventuellement, vous pouvez vous fendre d’une conclusion que vous inspirent ces graphiques.


