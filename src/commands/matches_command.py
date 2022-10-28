from telegram.ext import  CallbackContext
from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from constants.matches_pt import matches_pt
from constants.matches_en import matches_en
from constants.matches_es import matches_es

def matches_command(update: Update, context: CallbackContext) -> None:
  print("texto:",update.message.text)
  if update.message.text == "/agenda":
    keyboard = [
      [
        InlineKeyboardButton("20/11", callback_data="1"),
        InlineKeyboardButton("21/11", callback_data="2"),
        InlineKeyboardButton("22/11", callback_data="3"),
        InlineKeyboardButton("23/11 ", callback_data="4"),
        InlineKeyboardButton("24/11", callback_data="5"),
      ],
      [
        InlineKeyboardButton("25/11", callback_data="6"),
        InlineKeyboardButton("26/11", callback_data="7"),
        InlineKeyboardButton("27/11", callback_data="8"),
        InlineKeyboardButton("28/11", callback_data="9"),
        InlineKeyboardButton("29/11", callback_data="10"),
        
      ],
      [
        InlineKeyboardButton("30/11", callback_data="11"),
        InlineKeyboardButton("01/12", callback_data="12"),
        InlineKeyboardButton("02/12", callback_data="13"),
      ]
    ]
  if update.message.text == "/schedule":
    keyboard = [
      [
        InlineKeyboardButton("20/11", callback_data="14"),
        InlineKeyboardButton("21/11", callback_data="15"),
        InlineKeyboardButton("22/11", callback_data="16"),
        InlineKeyboardButton("23/11 ", callback_data="17"),
        InlineKeyboardButton("24/11", callback_data="18"),
      ],
      [
        InlineKeyboardButton("25/11", callback_data="19"),
        InlineKeyboardButton("26/11", callback_data="20"),
        InlineKeyboardButton("27/11", callback_data="21"),
        InlineKeyboardButton("28/11", callback_data="22"),
        InlineKeyboardButton("29/11", callback_data="23"),
        
      ],
      [
        InlineKeyboardButton("30/11", callback_data="24"),
        InlineKeyboardButton("01/12", callback_data="25"),
        InlineKeyboardButton("02/12", callback_data="26"),
      ]
    ]
  if update.message.text == "/calendario":
    keyboard = [
      [
        InlineKeyboardButton("20/11", callback_data="27"),
        InlineKeyboardButton("21/11", callback_data="28"),
        InlineKeyboardButton("22/11", callback_data="29"),
        InlineKeyboardButton("23/11 ", callback_data="30"),
        InlineKeyboardButton("24/11", callback_data="31"),
      ],
      [
        InlineKeyboardButton("25/11", callback_data="32"),
        InlineKeyboardButton("26/11", callback_data="33"),
        InlineKeyboardButton("27/11", callback_data="34"),
        InlineKeyboardButton("28/11", callback_data="35"),
        InlineKeyboardButton("29/11", callback_data="36"),
        
      ],
      [
        InlineKeyboardButton("30/11", callback_data="37"),
        InlineKeyboardButton("01/12", callback_data="38"),
        InlineKeyboardButton("02/12", callback_data="39"),
      ]
    ]
  
  reply_markup = InlineKeyboardMarkup(keyboard)
  update.message.reply_text("Select day:", reply_markup=reply_markup)
  
  
def buttonMatches(update: Update, context: CallbackContext) -> None:
  
  query = update.callback_query
  query.answer()
  if query.data == "1":
    query.edit_message_text(f"{matches_pt[0]}")
  if query.data == "2":
    query.edit_message_text(f"{matches_pt[1]}")
  if query.data == "3":
    query.edit_message_text(f" {matches_pt[2]}")
  if query.data == "4":
    query.edit_message_text(f" {matches_pt[3]}")
  if query.data == "5":
    query.edit_message_text(f" {matches_pt[4]}")
  if query.data == "6":
    query.edit_message_text(f" {matches_pt[5]}")
  if query.data == "7":
    query.edit_message_text(f" {matches_pt[6]}")
  if query.data == "8":
    query.edit_message_text(f" {matches_pt[7]}")
  if query.data == "9":
    query.edit_message_text(f" {matches_pt[8]}")
  if query.data == "10":
    query.edit_message_text(f" {matches_pt[9]}")
  if query.data == "11":
    query.edit_message_text(f" {matches_pt[10]}")
  if query.data == "12":
    query.edit_message_text(f" {matches_pt[11]}")
  if query.data == "13":
    query.edit_message_text(f" {matches_pt[12]}")
    
  #EN
  if query.data == "14":
    query.edit_message_text(f"{matches_en[0]}")
  if query.data == "15":
    query.edit_message_text(f"{matches_en[1]}")
  if query.data == "16":
    query.edit_message_text(f" {matches_en[2]}")
  if query.data == "17":
    query.edit_message_text(f" {matches_en[3]}")
  if query.data == "18":
    query.edit_message_text(f" {matches_en[4]}")
  if query.data == "19":
    query.edit_message_text(f" {matches_en[5]}")
  if query.data == "20":
    query.edit_message_text(f" {matches_en[6]}")
  if query.data == "21":
    query.edit_message_text(f" {matches_en[7]}")
  if query.data == "22":
    query.edit_message_text(f" {matches_en[8]}")
  if query.data == "23":
    query.edit_message_text(f" {matches_en[9]}")
  if query.data == "24":
    query.edit_message_text(f" {matches_en[10]}")
  if query.data == "25":
    query.edit_message_text(f" {matches_en[11]}")
  if query.data == "26":
    query.edit_message_text(f" {matches_en[12]}")
    
  #ES
  if query.data == "27":
    query.edit_message_text(f"{matches_es[0]}")
  if query.data == "28":
    query.edit_message_text(f"{matches_es[1]}")
  if query.data == "29":
    query.edit_message_text(f" {matches_es[2]}")
  if query.data == "30":
    query.edit_message_text(f" {matches_es[3]}")
  if query.data == "31":
    query.edit_message_text(f" {matches_es[4]}")
  if query.data == "32":
    query.edit_message_text(f" {matches_es[5]}")
  if query.data == "33":
    query.edit_message_text(f" {matches_es[6]}")
  if query.data == "34":
    query.edit_message_text(f" {matches_es[7]}")
  if query.data == "35":
    query.edit_message_text(f" {matches_es[8]}")
  if query.data == "36":
    query.edit_message_text(f" {matches_es[9]}")
  if query.data == "37":
    query.edit_message_text(f" {matches_es[10]}")
  if query.data == "38":
    query.edit_message_text(f" {matches_es[11]}")
  if query.data == "39":
    query.edit_message_text(f" {matches_es[12]}")
  
