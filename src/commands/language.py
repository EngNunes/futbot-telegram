from telegram.ext import  CallbackContext
from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from constants.htext import htext_en,htext_es,htext_pt 
from constants.language_const import PT, EN, ES


def language(update: Update, context: CallbackContext) -> None:
  print("language:",update.message.text)
  keyboard = [
    [
      InlineKeyboardButton("🇧🇷", callback_data=PT),
      InlineKeyboardButton("🇪🇸", callback_data=ES),
      InlineKeyboardButton("🇺🇸", callback_data=EN),
    ]
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  update.message.reply_text("Select your language:", reply_markup=reply_markup)
  
  return reply_markup
  
def buttonLanguage(update: Update, context: CallbackContext) -> None:
  
  query = update.callback_query
  query.answer()
  if query.data == "Português":
    query.edit_message_text(text=f"Selecionado: 🇧🇷 \n {htext_pt}")
  if query.data == "Español":
    query.edit_message_text(text=f"Seleccionado: 🇪🇸 \n {htext_es}")
  if query.data == "English":
    query.edit_message_text(text=f"Selected: 🇺🇸 \n {htext_en}")
  
