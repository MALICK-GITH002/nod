from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Fonction pour gérer la commande /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Bonjour ! Le bot est opérationnel. Utilisez les commandes disponibles."
    )

# Fonction principale pour démarrer le bot
def main():
    # Remplacez 'YOUR_TOKEN_HERE' par le token de votre bot Telegram
    application = Application.builder().token("8036490999:AAFlp8YuCAhjAd6wQumtUtdSs9HUMWKahFo").build()

    # Ajouter un gestionnaire pour la commande /start
    application.add_handler(CommandHandler("start", start))

    # Lancer le bot en mode polling
    application.run_polling()

if __name__ == "__main__":
    main()
