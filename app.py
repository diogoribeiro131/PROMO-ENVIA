import requests
import bs4
import telebot
import logging

# Configurações do Telegram
bot = telebot.TeleBot("6338577772:AAEuZ-2gXuJVbmABSqXqcKYfcjSfO_xOt1g")

# Configurações de log
logging.basicConfig(filename='script_log.log', level=logging.INFO)

# Lista de sites a serem monitorados
sites = [
    "https://www.magazineluiza.com.br/",
    "https://www.amazon.com.br/",
    "https://www.americanas.com.br/",
    "https://www.americanas.com.br/",
    "https://www.mercadolivre.com.br/",
    "https://shopee.com.br/",
    "https://pt.aliexpress.com/",
    "https://www.netshoes.com.br/",
    "https://br.shein.com/"
]

# Função para extrair o link da promoção
def get_link_promocao(site):
    response = requests.get(site)
    if response.status_code != 200:
        logging.warning(f"Falha ao acessar {site}. Código de status: {response.status_code}")
        return None

    soup = bs4.BeautifulSoup(response.content, "html.parser")

    # Verifica se a classe "Promocao" está presente
    div_promocao = soup.find("div", class_="Promocao")
    if div_promocao:
        # Tenta encontrar o link da promoção dentro da div encontrada
        promocao = div_promocao.find("a")
        if promocao:
            return promocao["href"]

    # Trata o caso em que a classe "Promocao" ou o link não foram encontrados
    return None

# Função para enviar a mensagem via Telegram
def enviar_mensagem(link):
    bot.send_message("+WPIVJvfHkJQ0YTRh", f"Nova promoção: {link}")
    logging.info(f"Mensagem enviada: Nova promoção: {link}")

# Loop principal
for site in sites:
    link_promocao = get_link_promocao(site)
    if link_promocao:
        enviar_mensagem(link_promocao)
