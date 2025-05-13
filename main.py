from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bonjour ! Utilisez la commande /scan pour scanner un réseau.\n"
                              "Exemple : /scan 192.168.1 1 10 80")

def main():
    # Remplacez 'YOUR_TOKEN_HERE' par votre token Telegram
    application = Application.builder().token("8036490999:AAFlp8YuCAhjAd6wQumtUtdSs9HUMWKahFo").build()

    # Ajouter le gestionnaire pour /start
    application.add_handler(CommandHandler("start", start))

    # Démarrer le bot
    application.run_polling()

if __name__ == "__main__":
    main()
