from constants.groups import groups_all_pt, groups_all_en, groups_all_es
from telegram.ext import  CallbackContext


def groups_command(update, context: CallbackContext):
  print("resultado update:",update.message.text)
  if update.message.text == "/grupos":
    update.message.reply_text(groups_all_pt)
  if update.message.text == "/groups":
    update.message.reply_text(groups_all_en)
  if update.message.text == "/losgrupos":
    update.message.reply_text(groups_all_es)