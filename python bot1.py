from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8659849542:AAHLwsMRm6yBKwuzLeKlMINxmo7N5Lr8cVc"

# DATA STORE
user_data = {}

# MAIN MENU
main_menu = [
    ["📋 Task", "💰 Balance"],
    ["💸 Withdraw", "🔗 Reffer"],
    ["🏆 Rank", "ℹ️ Help"]
]

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in user_data:
        user_data[user_id] = {"balance": 0, "instagram": ""}

    await update.message.reply_text(
        "🔥 Welcome to Earn Bot",
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )

# HANDLER
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if user_id not in user_data:
        user_data[user_id] = {"balance": 0, "instagram": ""}

    # TASK MENU
    if text == "📋 Task":
        await update.message.reply_text(
            "📋 Choose Task:\n\n📸 Instagram Task\n❌ Cancel"
        )

    # INSTAGRAM TASK
    elif text == "📸 Instagram Task":
        await update.message.reply_text("✍️ তোমার Instagram username লিখো (@name)")

    # SAVE INSTAGRAM
    elif text.startswith("@"):
        user_data[user_id]["instagram"] = text
        await update.message.reply_text(
            f"✅ Instagram saved: {text}",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )

    # CANCEL
    elif text == "❌ Cancel":
        await update.message.reply_text(
            "❌ Cancelled",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )

    # BALANCE
    elif text == "💰 Balance":
        bal = user_data[user_id]["balance"]
        await update.message.reply_text(f"💰 Balance: {bal} TK")

    # WITHDRAW
    elif text == "💸 Withdraw":
        await update.message.reply_text("💳 bKash / Nagad number লিখো")

    # REFFER
    elif text == "🔗 Reffer":
        link = f"https://t.me/your_bot?start={user_id}"
        await update.message.reply_text(f"🔗 Your referral link:\n{link}")

    # RANK
    elif text == "🏆 Rank":
        bal = user_data[user_id]["balance"]

        if bal > 1000:
            rank = "🔥 Pro"
        elif bal > 500:
            rank = "⭐ Silver"
        else:
            rank = "🥉 Beginner"

        await update.message.reply_text(f"🏆 Rank: {rank}")

    # HELP
    elif text == "ℹ️ Help":
        await update.message.reply_text("📌 Support: @rosy3290")

# BOT SETUP
app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("Bot running...")
app.run_polling()
