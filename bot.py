import logging
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ✅ التوكن من متغيرات البيئة (آمن)
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ لم يتم تعيين BOT_TOKEN في متغيرات البيئة!")

# إعداد السجل
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# --- الأوامر ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"مرحباً {user.first_name}! 👋\n"
        "أنا بوت تيليغرام بسيط.\n\n"
        "الأوامر المتاحة:\n"
        "/start - بدء المحادثة\n"
        "/help  - المساعدة\n"
        "/about - معلومات عن البوت"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 الأوامر المتاحة:\n\n"
        "/start - بدء المحادثة\n"
        "/help  - عرض هذه الرسالة\n"
        "/about - معلومات عن البوت\n\n"
        "يمكنك أيضاً إرسال أي رسالة نصية وسأرد عليها!"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 هذا بوت تيليغرام تم إنشاؤه بـ Python\n"
        "المكتبة المستخدمة: python-telegram-bot\n"
        "الإصدار: 20+"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(
        f"📨 استلمت رسالتك:\n«{text}»\n\n"
        "سأعمل على معالجتها قريباً! 😊"
    )

# --- تشغيل البوت ---

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main