import json
from channels.generic.websocket import WebsocketConsumer

class DishConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def dish_updated(self, event):
        self.send(text_data=json.dumps(event))
