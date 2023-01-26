import requests
from bs4 import BeautifulSoup

# URL de la page contenant les informations sur les programmes TNT
URL_PROGRAMME_TNT = "https://www.programme-tv.net/programme/programme-tnt/en-ce-moment.html"

# Envoi d'une requête HTTP GET à l'URL spécifiée
response = requests.get(URL_PROGRAMME_TNT)

# Traitement du contenu de la réponse en utilisant BeautifulSoup
data = BeautifulSoup(response.content, "html.parser")

# Récupération de tous les éléments div de la classe "gridRow-cards"
channels = data.find_all("div", class_="gridRow-cards")

# Boucle pour chaque élément trouvé
for channel in channels:
    # Récupération du numéro de la chaîne
    channel_number = channel.find('p', class_='gridRow-cardsChannelNumber').text
    # Récupération du nom de la chaîne
    channel_name = channel.find('a', class_='gridRow-cardsChannelItemLink').text.replace(channel_number, '').strip()
    # Récupération du nom du programme en cours
    programm_name = channel.find('h3', class_='mainBroadcastCard-title').find('a').text.strip()

    # Affichage des informations récupérées
    print(channel_name + ' : ' + programm_name)