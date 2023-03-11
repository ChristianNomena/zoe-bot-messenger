import ampalibe
from ampalibe import Messenger

chat = Messenger()

# create a get started option to get permission of user.
# chat.get_started()

@ampalibe.command('/')
def main(sender_id, cmd, **ext):
    '''
    main function where messages received on
    the facebook page come in.

    @param sender_id String: 
        sender facebook id
    @param cmd String: 
        message content
    @param ext Dict: 
        contain list of others
            data sent by facebook (sending time, ...)
            data sent by your payload if not set in parameter
    '''
    
    if "hello" in cmd.lower():
        chat.send_text(sender_id, "Hello Christian")
    elif "who" in cmd.lower():
        chat.send_text(sender_id, "Sorry Christian")
    elif "sorry" in cmd.lower():
        chat.send_text(sender_id, "No problem")
    else:
        chat.send_text(sender_id, "I can't understand")
