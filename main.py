import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Liste blanche des utilisateurs autorisés (remplacez par votre ID Telegram)
AUTHORIZED_USERS = [7569017578]  # Remplacez avec votre propre ID utilisateur Telegram

# Fonction pour exécuter des commandes système
async def shell(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id

    # Vérifiez si l'utilisateur est autorisé
    if user_id not in AUTHORIZED_USERS:
        await update.message.reply_text("⛔ Désolé, vous n'êtes pas autorisé à exécuter cette commande.")
        return

    # Récupérez la commande depuis la requête utilisateur
    command = " ".join(context.args)
    if not command:
        await update.message.reply_text("Veuillez fournir une commande à exécuter. Exemple : /shell ls")
        return

    try:
        # Exécutez la commande dans le shell
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, timeout=10)
        await update.message.reply_text(f"Résultat :\n{result}")
    except subprocess.CalledProcessError as e:
        await update.message.reply_text(f"Erreur lors de l'exécution :\n{e.output}")
    except Exception as e:
        await update.message.reply_text(f"Une erreur est survenue : {e}")

# Fonction pour démarrer le bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Bienvenue ! Utilisez /shell pour exécuter des commandes système.")

# Configuration principale
def main():
    # Remplacez 'YOUR_TOKEN_HERE' par votre token Telegram
    application = Application.builder().token("8036490999:AAFlp8YuCAhjAd6wQumtUtdSs9HUMWKahFo").build()

    # Commande pour /start
    application.add_handler(CommandHandler("start", start))

    # Commande pour /shell
    application.add_handler(CommandHandler("shell", shell))

    # Lancer le bot
    application.run_polling()

if __name__ == "__main__":
    main()
