import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ContextTypes, ConversationHandler
from dotenv import load_dotenv
from commands.language import language, buttonLanguage
from commands.matches_command import matches_command, buttonMatches
from commands.champions_command import champions_command
from commands.groups_command import groups_command
from commands.help_command import help_command

from handlers.handler_message import handle_message

from commands.error import error


load_dotenv()
my_secret = os.environ['TOKEN']
print('iniciando FutBot')

def main():
  updater = Updater(os.environ['TOKEN'])

  dispatcher = updater.dispatcher

  #commands
  dispatcher.add_handler(CommandHandler("start", language))
  dispatcher.add_handler(CommandHandler("lingua", language))
  dispatcher.add_handler(CommandHandler("language", language))
  dispatcher.add_handler(CommandHandler("lengua", language))
  
  
  dispatcher.add_handler(CommandHandler("grupos", groups_command))
  dispatcher.add_handler(CommandHandler("losgrupos", groups_command))
  dispatcher.add_handler(CommandHandler("groups", groups_command))
  
  dispatcher.add_handler(CommandHandler("campeas", champions_command))
  dispatcher.add_handler(CommandHandler("champions", champions_command))
  dispatcher.add_handler(CommandHandler("campeones", champions_command))
  
  
  dispatcher.add_handler(CommandHandler("agenda", matches_command))
  dispatcher.add_handler(CommandHandler("calendario", matches_command))
  dispatcher.add_handler(CommandHandler("schedule", matches_command))
  
  
  dispatcher.add_handler(CommandHandler("help", help_command))
  dispatcher.add_handler(CommandHandler("ayuda", help_command))
  dispatcher.add_handler(CommandHandler("ajuda", help_command))
  
  
  
  dispatcher.add_handler(CallbackQueryHandler(buttonLanguage, pattern=("^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]+$")))
  dispatcher.add_handler(CallbackQueryHandler(buttonMatches, pattern="^[0-9]*$"))

  #messages
  dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

  #errors
  dispatcher.add_error_handler(error)

  print('FutBot ativado')
  updater.start_polling()

  updater.idle()


if __name__ == '__main__':
  main()
