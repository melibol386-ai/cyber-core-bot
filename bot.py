import os, logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8395316963:AAEfs7FOMEotIC-qnwLzB2tJhJvqp_fJBUI"
BOT_NAME = "CYBER-CORE SİBER TİM🇹🇷"

logging.basicConfig(level=logging.INFO)

async def anti_spam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower()
        spam_links = ["t.me/", "http://", "https://", "joinchat"]
        if any(link in text for link in spam_links):
            try:
                await update.message.delete()
                await context.bot.send_message(chat_id=update.effective_chat.id, text=f"🛡️ {BOT_NAME}\n⚠️ Spam engellendi!")
            except: pass

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), anti_spam))
    app.run_polling()
