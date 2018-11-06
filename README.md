# itn

##### Projet réalisé pour le cours de POOA par Gabrielle Rappaport, Alix Mallard et Camille Nathan

## Applications
Cette application permet de gérer des ordres.
Un ordre est un ensemble d'informations correspondants à une commande de produits pour un client et commandée à un fournisseur. Chaque ordre est livré par une ou plusieures livraisons.

## Base de donnée
4 tables en SQLite

##Installation
Créer un dossier d'environnement virtuel et l'activer:

```
virtualenv -p python3 .venv
source .venv/bin/activate
```
Installer les librairies python :

```
pip install -r requirements.txt
```
Générer la base de données et lancer l'application
```
python generate_db.py
python run.py
```
Aller sur l'application [ici](http://127.0.0.1:5000/)

