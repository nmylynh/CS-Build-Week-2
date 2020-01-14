from player import *

adventure = adv()
adventure.accumulate=True   # set pick up items to false
adventure.import_text_map=True
adventure.create_starting_map()
adventure.get_treasure()
