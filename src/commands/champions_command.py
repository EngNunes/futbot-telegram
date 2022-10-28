from constants.champions import champions_all_pt, champions_all_en, champions_all_es
from telegram.ext import  CallbackContext


def champions_command(update, context: CallbackContext):
  if update.message.text == "/campeas":
    update.message.reply_text(champions_all_pt)
  if update.message.text == "/champion":
    update.message.reply_text(champions_all_en)
  if update.message.text == "/campeones":
    update.message.reply_text(champions_all_es)