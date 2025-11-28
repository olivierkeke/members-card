# Générateur de cartes d'adhérents

Outil de génération de cartes d'adhérents à partir du tableau (format CSV) des adhérents.

Emplacement prévus pour :

* le logo de l'association
* un titre (ex: "saison 2025-2026")
* un QRcode (par exemple pour encoder l'url du site web de l'association)
* le nom de l'adhérent
* une pied de page en deux lignes (par exemple pour indiquer l'adresse de l'association)

## Installation

Prérequis :

* Python 3 (testé uniquement en Python 3.12) et pip.

Clôner le dépôt puis installer l'outil avec la commande

```shell
pip install .
```

## Utilisation

### En ligne de commande

```shell
usage: members-card [-h] --name-columns NAME_COLUMNS [NAME_COLUMNS ...] [--name-color NAME_COLOR] [--background-color-1 RED GREEN BLUE] [--background-color-2 RED GREEN BLUE] [--paper-format PAPER_FORMAT]
                    [--qrcode-url QRCODE_URL] [--logo LOGO] [--title TITLE] [--title-color TITLE_COLOR] [--footer-1 FOOTER_1] [--footer-2 FOOTER_2] [--footer-color FOOTER_COLOR]
                    members_csv output_file

positional arguments:
  members_csv           CSV file with members list
  output_file           Output pdf file path

options:
  -h, --help            show this help message and exit
  --name-columns NAME_COLUMNS [NAME_COLUMNS ...], -n NAME_COLUMNS [NAME_COLUMNS ...]
                        Columns of the CSV file to use as name
  --name-color NAME_COLOR, -nc NAME_COLOR
                        color of the name text
  --background-color-1 RED GREEN BLUE, -c1 RED GREEN BLUE
                        Background color of the bottom left angle
  --background-color-2 RED GREEN BLUE, -c2 RED GREEN BLUE
                        Background color of the top right angle
  --paper-format PAPER_FORMAT, -p PAPER_FORMAT
                        Paper format
  --qrcode-url QRCODE_URL, -q QRCODE_URL
                        Sting to encode in the qrcode
  --logo LOGO, -l LOGO  Logo
  --title TITLE, -t TITLE
                        Card title
  --title-color TITLE_COLOR, -tc TITLE_COLOR
                        Title color
  --footer-1 FOOTER_1, -f1 FOOTER_1
                        Footer first line
  --footer-2 FOOTER_2, -f2 FOOTER_2
                        Footer seconde line
  --footer-color FOOTER_COLOR, -fc FOOTER_COLOR
                        Footer color
```

Par exemple, la commande
```shell
members-card tests/resources/adherents.csv cartes-adherents.pdf -n Nom Prénom -c1 255 255 255 -c2 0 166 82 -p a4 -q "https://github.com/Cyclo-Club-de-Grand-Lieu/members-card" -l tests/resources/logo.svg -t "SAISON 2025 - 2026" -f1 "Mon adresse partie 1" -f2 "Mon adresse partie 2"
```
génère le document suivant :

[![](doc/cartes-adherents.svg)](doc/cartes-adherents.pdf)
