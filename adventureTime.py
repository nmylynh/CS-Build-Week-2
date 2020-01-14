from player import *

adventure = adv()
adventure.accumulate=True   # if you want to pick up items, set to True
adventure.import_text_map=True
adventure.want_to_mine=True # if you want to mine even though you had already mined, set to True
adventure.create_starting_map()
adventure.get_treasure()
