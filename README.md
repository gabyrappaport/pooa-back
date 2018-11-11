# ITN

##### Projet réalisé pour le cours de POOA par Gabrielle Rappaport, Alix Mallard et Camille Nathan

## Applications
Cette application permet de gérer des ordres.
Un ordre est un ensemble d'informations correspondants à une commande de produits pour un client et commandée à un fournisseur. Chaque ordre est livré par une ou plusieures livraisons.

## Comment utiliser l'application
Vous arrivez sur la page de login, cliquez directement sur 'Connexion' pour accéder à l'application.

L'onglet Nouvel Ordre permet d'ajouter une nouvelle commande avec les produits qu'elle
contient et leur informations, le nom du client et celui du fournisseur
ainsi que les informations liées à la commande et caractéristiques à l'entreprise

L'onglet Ordres présente le récapitulatif des ordres. Vous pouvez télécharger un excel récapitulatif de l'ordre à envoyer à vos fournisseurs
en cliquant sur l'icône de téléchargement à gauche de l'ordre. En cliquant sur un ordre vous avez
toutes les informations de cet ordre et vous pouvez effectuer le suivi de commande 
(livraison et paiement) ainsi qu'ajouter des expéditions relatives aux produits de l'ordre. 

L'onglet Partenaires permet de créer des partenaires (clients ou fournisseurs), des ordres avec une date d'expedition
souhaitée, d'ajouter des produits avec leurs informations dans cet ordre et donner des informations supplémentaires.

L'onglet Revenus donne accès à un récapitulatif sur 8 mois des revenus 
générés par chaque fournisseur et client.


Remarque:
De nombreuses autres fonctionnalités ont été développées dans le back (mise à jour de partenaires, modification d'un ordre
ou d'une expédition ainsi que toutes les méthodes de suppression) mais ne sont pas encore accessible dans le front. 
En effet, ce projet est destiné à une entreprise pour la fin de l'année et continuera d'être développé.
De même la partie login et gestion des sessions n'a pas encore été développée.

## Blabla
Nous avons utilisé un pattern Modele Vue Controlleur pour séparer l'accès aux données 
du traitement de l’information et de sa mise en forme.

Nous avons utilisé flask dans le back afin de créer notre propre API que nous appelons ensuite. 
Le front a été conçu avec un framework Angular.

Notre base de données est en SQLite car légère et correspondant à nos attentes quant à la facilité 
d'implémentation de l'application et contient 4 tables contenant les ordres, partnenaires, expéditions et produits.
(voir Annexe à la fin)

## Installation
Si vous n'avez pas virtualenv, faire
```
pip3 install virtualenv
```
Créer un dossier d'environnement virtuel:
```
virtualenv -p python3 .venv
```
Activer l'environnement virtuel:

SUR LINUX : ```source .venv/bin/activate ```

SUR WINDOWS : ```.venv\Scripts\activate```

Installer les librairies python :

```
pip3 install -r requirements.txt
```
Générer la base de données et lancer l'application
```
python3 generate_db.py
python3 run.py
```
Aller sur l'application [ici](http://127.0.0.1:5000/)

Pour quitter l'environnement faites ```deactivate```.
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