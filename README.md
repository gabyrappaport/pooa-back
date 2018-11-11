# ITN

_**Projet réalisé pour le cours de POOA par Gabrielle Rappaport, Alix Mallard et Camille Nathan**_

### Installation

1. Rendez-vous dans le dossiers où vous avez téléchargé notre fichier _zip_.

    Si vous n'avez pas _virtualenv,_ faire dans un terminal:
    ```
    pip3 install virtualenv
    ```
2. Créer un dossier d'environnement virtuel:
    ```
    virtualenv -p python3 .venv
    ```
3. Activer l'environnement virtuel:

    **SUR LINUX** : ```source .venv/bin/activate ```

    **SUR WINDOWS** : ```.venv\Scripts\activate```

4. Installer les librairies python :
    ```
    pip3 install -r requirements.txt
    ```
5. Générer la base de données et lancer l'application
    ```
    python3 generate_db.py
    python3 run.py
    ```
6. Aller sur l'application (sur google chrome de préférence) [ici](http://127.0.0.1:5000/) _(http://127.0.0.1:5000/)_

7. Pour quitter l'environnement faites ```deactivate```.

### Applications
Cette application permet de gérer des ordres.
Un ordre est un ensemble d'informations correspondants à une commande de produits pour un client et commandée à un 
fournisseur. Chaque ordre est livré par une ou plusieures livraisons.

### Comment utiliser l'application ?

1. L'onglet _Nouvel Ordre_ permet d'ajouter une nouvelle commande avec les produits qu'elle
contient et leurs informations, le nom du client et celui du fournisseur
ainsi que les informations liées à la commande et caractéristiques à l'entreprise

2. L'onglet _Ordres_ présente le récapitulatif des ordres. Vous pouvez télécharger un excel récapitulatif de l'ordre à envoyer à vos fournisseurs
en _cliquant sur l'icône de téléchargement_ à gauche de l'ordre. En _cliquant sur un ordre_ vous avez
toutes les informations de cet ordre et vous pouvez effectuer le suivi de commande 
(livraison et paiement) ainsi qu'ajouter des expéditions relatives aux produits de l'ordre. 

3. L'onglet _Partenaires_ permet de créer des partenaires (clients ou fournisseurs), des ordres avec une date d'expedition
souhaitée, d'ajouter des produits avec leurs informations dans cet ordre et donner des informations supplémentaires.

4. L'onglet _Revenus_ donne accès à un récapitulatif sur 8 mois des revenus 
générés par chaque fournisseur et client.


##### **Remarques:**

De nombreuses autres fonctionnalités ont été développées dans le back (mise à jour de partenaires, modification d'un ordre
ou d'une expédition ainsi que toutes les méthodes de suppression) mais ne sont pas encore accessible dans le front. 
En effet, ce projet est destiné à une entreprise pour la fin de l'année et continuera d'être développé.
De même la partie login et gestion des sessions n'a pas encore été développée.

## Décomposition du projet
Nous avons utilisé un pattern **Modele Vue Controlleur** pour séparer l'accès aux données 
du traitement de l’information et de sa mise en forme.

Nous avons utilisé flask dans le back afin de créer notre propre API que nous appelons ensuite. 
Le front a été conçu avec un framework Angular.

Notre base de données est en SQLite car légère et correspondant à nos attentes quant à la facilité 
d'implémentation de l'application et contient **4 tables** contenant les ordres, partnenaires, expéditions et produits.
(voir Annexe à la fin).

### Les différents fichiers

``` text
> configs
> Controllers
> DataBase
> Models
> public où sont enregistré les exccels
> static
> templates
    .gitignore
    app.py
    generate_db.py
    itn.db
    README.md
    requirements.txt
    run.py
```

## Annexe
Description des tables de la base de donnée

|Orders|
|------|
|id_order|
|id_supplier|
|Id_client|
|expected_delivery_date|
|Payment_type|
|l_dips|
|appro_ship_sample|
|appro_s_off|
|ship_sample_2h|
|total_amount|
|creation_date|

|Partner|
|------|
|id_partner|
|partner_type|
|company|

|Products|
|--------|
|id_product|
|id_order|
|id_shipment|
|reference|
|color|
|meter|
|price|
|commission|

|Shipments|
|--------|
|id_shipment|
|expedition_date|
|Transportation|
|departure_location|
|arrival_location|
