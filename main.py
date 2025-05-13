import socket
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def scan_network(base_ip, start_range, end_range, port):
    """
    Fonction pour scanner une plage d'adresses IP.
    """
    results = []
    for i in range(start_range, end_range + 1):
        ip = f"{base_ip}.{i}"
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))
                if result == 0:
                    results.append(f"[+] Port {port} est ouvert sur {ip}")
        except Exception as e:
            results.append(f"[!] Erreur pour {ip}: {e}")
    return results

def start(update: Update, context: CallbackContext) -> None:
    """
    Commande /start pour démarrer le bot.
    """
    update.message.reply_text("Bonjour ! Utilisez la commande /scan pour scanner un réseau.\n"
                              "Exemple : /scan 192.168.1 1 10 80")

def scan(update: Update, context: CallbackContext) -> None:
    """
    Commande /scan pour lancer un scan réseau.
    Syntaxe : /scan <base_ip> <start_range> <end_range> <port>
    """
    try:
        # Extraire les arguments de la commande
        args = context.args
        if len(args) != 4:
            update.message.reply_text("Syntaxe invalide ! Utilisez : /scan <base_ip> <start_range> <end_range> <port>")
            return

        # Paramètres du scan
        base_ip = args[0]
        start_range = int(args[1])
        end_range = int(args[2])
        port = int(args[3])

        # Lancer le scan
        update.message.reply_text(f"Scan en cours pour {base_ip}.{start_range} à {base_ip}.{end_range} sur le port {port}...")
        results = scan_network(base_ip, start_range, end_range, port)

        # Envoyer les résultats du scan
        if results:
            update.message.reply_text("\n".join(results))
        else:
            update.message.reply_text("Aucun port ouvert trouvé dans la plage spécifiée.")

    except ValueError:
        update.message.reply_text("Erreur : veuillez entrer des plages et un port valides.")
    except Exception as e:
        update.message.reply_text(f"Erreur lors du scan : {e}")

def main():
    """
    Fonction principale pour démarrer le bot.
    """
    # Remplacez 'YOUR_TOKEN_HERE' par votre token Telegram obtenu via BotFather
    updater = Updater("8036490999:AAFlp8YuCAhjAd6wQumtUtdSs9HUMWKahFo")

    # Dispatcher pour gérer les commandes
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("scan", scan))

    # Démarrer le bot
    updater.start_polling()
    print("Bot en cours d'exécution...")
    updater.idle()

if __name__ == "__main__":
    main()
