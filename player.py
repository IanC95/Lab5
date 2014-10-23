from items import *
from map import rooms

inventory = [item_id] + [item_bass]

# Start game at the reception
current_room = rooms["Reception"]
health = 200