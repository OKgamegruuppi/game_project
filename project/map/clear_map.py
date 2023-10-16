from data.init_groups import *

def clear_map():
    print("CLEARING THE MAP")
    global collidables
    collidables = []
    global quest_items
    quest_items = []
    global found_cats
    found_cats = []


    camera_group[0].empty()
    playergroup.empty()
    friendlies.empty()
    questgroup.empty()
    enemies.empty()
    itemgroup.empty()
    decor.empty()
    effectsgroup.empty()
