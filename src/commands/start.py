from telegram.ext import CallbackContext
from telegram import Update
from constants.htext import htext_pt

def start_command(update: Update, context: CallbackContext):
  update.message.reply_text(htext_pt)
  