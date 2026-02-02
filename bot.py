from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
user_numbers = {}
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.strip()
    # لو المستخدم بعت رقم أول مرة
    if text.lstrip("-").isdigit():
        user_numbers[user_id] = int(text)
        await update.message.reply_text(f"✅ تم حفظ الرقم: {text}")
        return
    # لو المستخدم بعت عملية + أو -
    if user_id in user_numbers and (text.startswith("+") or text.startswith("-")):
        try:
            op = text[0]
            num = int(text[1:].strip())
            if op == "+":
                user_numbers[user_id] += num
            else:
                user_numbers[user_id] -= num
            await update.message.reply_text(f"🧮 النتيجة: {user_numbers[user_id]}")
        except:
            await update.message.reply_text("❌ اكتب العملية صح: +5 أو -3")
    else:
        await update.message.reply_text("⚠️ ابعت رقم الأول")
def main():
    app = ApplicationBuilder().token("8165234650:AAGS2GlVJ-SzBFR31TLGwq02w_Xqj69t48M").build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
if __name__ == "__main__":
    main()
