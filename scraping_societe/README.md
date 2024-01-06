Dans ce code, des données sont extraites de pages web pour chaque entreprise listée dans `liste_url`, en utilisant les bibliothèques **requests**, **BeautifulSoup (bs)** et **pandas**. Le code a été mis à jour pour inclure une sélection aléatoire de l'en-tête User-Agent, ce qui peut aider à prévenir le blocage par certains sites web qui limitent les accès automatisés.

1. **Initialisation d'une liste pour stocker les données**  `donnees_entreprises = []`
	
2. **Boucle sur chaque URL** dans `liste_url` :
	- **Sélection aléatoire d'un User-Agent** : Un navigateur est choisi aléatoirement parmi une liste prédéfinie (`csts.BROWSERS`). Cela permet de varier l'en-tête User-Agent envoyé avec chaque requête, ce qui peut éviter de se faire bloquer par les mesures anti-scraping des sites web.
	- **Envoi d'une requête HTTP GET** : Une requête est envoyée à l'URL avec l'en-tête User-Agent spécifié.
	- **Vérification du statut de la réponse** : Le code vérifie que la réponse a un statut HTTP 200, qui indique une réponse réussie.
	- **Extraction du contenu HTML** : Le contenu HTML de la réponse est stocké.

3. **Analyse et extraction des données avec BeautifulSoup**
	-	**Analyse du contenu HTML :** Le contenu HTML est analysé à l'aide de BeautifulSoup.
	- **Extraction des informations spécifiques** : Le code extrait le nom de l'entreprise, l'adresse, et les numéros SIREN, SIRET et TVA à partir des éléments HTML spécifiés.

4. **Création d'un dataframe pour chaque entreprise** : Les informations extraites sont stockées dans un dataframe pandas.
	
5.  **Ajout du dataframe à la liste** : Le dataframe créé pour chaque entreprise est ajouté à la liste `donnees_entreprises`.

7. **Concaténation des dataframes en un seul** : Après avoir traité toutes les URLs, tous les dataframes sont combinés en un seul dataframe. Cela est fait en utilisant `pd.concat`, qui concatène les dataframes listés, avec `axis=0` pour concaténer verticalement et `ignore_index=True` pour réinitialiser les indices dans le dataframe final.