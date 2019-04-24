from config import Config

from fbchat import log, Client
from fbchat.models import *
from random import randint

# Subclass fbchat.Client and override required methods
class Bot(Client):
    def __init__(self, email, pw):
        Client.__init__(self, email, pw)
    
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        # self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))        

        # Dice bot
        if message_object.text == ".roll.":
            message_object.text = "DICE BOT: {}".format(randint(1,20))
            message_object.text = "DICE BOT: {}".format(1)
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

        # Meatstick bot
        if message_object.text == ".meatstick.":
            message_object.text = "*shocks brain*"
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

        # April foold bot
        if message_object.text in [".aprilfools.", ".aprilfooled.", ".aprilfool.", ".fooled", ".fool."]:
            message_object.text = "BIT BOT: http://www.latlmes.com/arts/return-of-the-golden-age-of-comics-1"
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

        # Bit bot
        if message_object.text in ["nice bit", "Nice bit", "nice bit!", "Nice bit!", "its a bit", "it's a bit", "Its a bit", "It's a bit", "it was a bit", "It was a bit", "it was a bit!", "It was a bit!"]:
            message_object.text = "Get on up outta here with those bits!"
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)

if __name__="__main__":
    client = Bot(Config.email, Config.pw)
    client.listen()    
    client.logout()
