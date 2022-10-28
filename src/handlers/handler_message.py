from handlers.handler_response import handle_response

def handle_message(update, context):
  message_type = update.message.chat.type
  text = str(update.message.text)
  print(f'User({update.message.chat.id}) says: "{text}" in: {message_type}')

  if message_type == 'group':
    if '@FutBotAdminbot' in text:
      new_text = text.replace('@FutBotAdminbot', '').strip()
      response = handle_response(new_text)
  else:
    response = handle_response(text)
  update.message.reply_text(response)
