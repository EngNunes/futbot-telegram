from constants.htext import help_pt, help_en, help_es
from telegram.ext import  CallbackContext


def help_command(update, context: CallbackContext):
  if update.message.text == "/ajuda":
    update.message.reply_text(help_pt)
  if update.message.text == "/help":
    update.message.reply_text(help_en)
  if update.message.text == "/ayuda":
    update.message.reply_text(help_es)