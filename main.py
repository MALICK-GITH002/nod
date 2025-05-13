import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Fonction générique pour appeler l'API HackerTarget
async def call_hackertarget_api(update: Update, context: CallbackContext, api_url: str, description: str) -> None:
    if len(context.args) != 1:
        await update.message.reply_text(f"❌ Fournissez une cible valide. Exemple : /{description} <cible>")
        return

    target = context.args[0]
    try:
        response = requests.get(api_url.format(target=target))
        if response.status_code == 200:
            await update.message.reply_text(f"🔍 Résultats {description.capitalize()} :\n\n{response.text}")
        else:
            await update.message.reply_text(f"❌ Erreur avec l'API. (Code : {response.status_code})")
    except Exception as e:
        await update.message.reply_text(f"❌ Une erreur s'est produite : {e}")

# Commandes spécifiques à chaque fonctionnalité
async def nmap_scan(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/nmap/?q={target}", "nmap")

async def dns_lookup(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/dnslookup/?q={target}", "dnslookup")

async def whois_lookup(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/whois/?q={target}", "whois")

async def geoip_lookup(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/geoip/?q={target}", "geoip")

async def port_scan(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/nmap/?q={target}", "portscan")

async def subdomains_lookup(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/hostsearch/?q={target}", "subdomains")

async def traceroute(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/mtr/?q={target}", "traceroute")

async def blacklist_check(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/blacklist/?q={target}", "blacklist")

async def asn_lookup(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/aslookup/?q={target}", "asn")

async def reversedns_lookup(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/reversedns/?q={target}", "reversedns")

async def shareddns_lookup(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/findshareddns/?q={target}", "shareddns")

async def ping_check(update: Update, context: CallbackContext) -> None:
    await call_hackertarget_api(update, context, "https://api.hackertarget.com/nping/?q={target}", "ping")

# Commande de démarrage
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "👋 Bienvenue dans le bot HackerTarget ! Voici les commandes disponibles :\n\n"
        "/nmap <cible> - Scan réseau avec Nmap\n"
        "/dnslookup <cible> - Recherche DNS\n"
        "/whois <cible> - Recherche Whois\n"
        "/geoip <cible> - Informations géographiques d'IP\n"
        "/portscan <cible> - Scan de ports\n"
        "/subdomains <cible> - Sous-domaines associés\n"
        "/traceroute <cible> - Trace de route\n"
        "/blacklist <cible> - Vérification de liste noire\n"
        "/asn <cible> - Recherche ASN\n"
        "/reversedns <cible> - Recherche DNS inversée\n"
        "/shareddns <cible> - Enregistrements DNS partagés\n"
        "/ping <cible> - Vérification Ping\n"
    )

# Configuration principale
def main():
    # Remplacez 'YOUR_TOKEN_HERE' par le token de votre bot Telegram
    application = Application.builder().token("8036490999:AAFlp8YuCAhjAd6wQumtUtdSs9HUMWKahFo").build()

    # Ajouter les gestionnaires de commandes
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("nmap", nmap_scan))
    application.add_handler(CommandHandler("dnslookup", dns_lookup))
    application.add_handler(CommandHandler("whois", whois_lookup))
    application.add_handler(CommandHandler("geoip", geoip_lookup))
    application.add_handler(CommandHandler("portscan", port_scan))
    application.add_handler(CommandHandler("subdomains", subdomains_lookup))
    application.add_handler(CommandHandler("traceroute", traceroute))
    application.add_handler(CommandHandler("blacklist", blacklist_check))
    application.add_handler(CommandHandler("asn", asn_lookup))
    application.add_handler(CommandHandler("reversedns", reversedns_lookup))
    application.add_handler(CommandHandler("shareddns", shareddns_lookup))
    application.add_handler(CommandHandler("ping", ping_check))

    # Lancer le bot
    application.run_polling()

if __name__ == "__main__":
    main()
