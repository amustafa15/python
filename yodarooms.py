#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:55:40 2017

@author: Ameen
"""

import sys

PROMPT = "> "

# rooms are just dictionaries, with a description and a list of named actions, which point at other rooms
# the 'exit' value indicates a room which ends the game
# the 'name' is used to give each room a unique in the map

entrance_room = {
        'name':'entrance',
        'desc':'Your ship loses control and crashes into the murky swamps of Dagobah. An old walking rat approaches your ship. You climb out and...',
        'actions':{'jump on land and bow before him':'swampbow','shout from your slowly sinking ship':'swampshout'}, ## these are your actions:new room
        'exit':False ## any room with exit:True is a room that ends the game
}
swamp_bow = {
        'name':'swampbow',
        'desc':'You bow before the rat. Oh talking rat, it is me, a humble human sent by the ghost of some guy I kinda knew to kill his father. I thought so the rat says. Come wtih me.',
        'actions':{'follow':'swampfollow'},
        'exit':False
}
swamp_shout = {
        'name':'swampshout',
        'desc':'I have been sent by the ghost of some old guy I kinda knew. He said a talking rat would teach me how to kill my father. I am that rat the rat says. Come with me.',
        'actions':{'follow':'swampfollow'},
        'exit':False
 }
swamp_follow = {
        'name':'swampfollow',
        'desc':'I am Yoda. first things first you need to get your ship out of the swamp. I can do it for you but Im too hungry to use the force. If you get me some possums I will have the strength to do it. They are one of those two holes. Go into...',
        'actions':{'hole one':'holeone','hole two':'holetwo'},
        'exit':False
 }
hole_one = {
        'name':'holeone',
        'desc':'you crawl into the dimly lit hole. you follow a dim light to a large chamber full of swamp squirrels. swamp squirrels are not rabbits. You could kill the swamp squirrels and try to confuse yoda or you can go to hole 2.',
        'actions':{'kill the squirrels':'squirrel','hole two':'holetwo'},
        'exit':False
}
hole_squirrel = {
        'name':'squirrel',
        'desc':'You crush the swamp squirrels skulls and rip off their tails to disguise them. You can bring them to yoda or go to hole 2',
        'actions':{'lie to yoda':'yodalie','hole two':'holetwo'},
        'exit':False
}
squirrel_yoda = {
        'name':'yodalie',
        'desc':'here are some delicate space possums. Yoda examines them. These are clearly common space squirrels with their tails ripped off. I will not help you. Goodbye.',
        'actions':{}, ## no actions because game over.
        'exit':True
}   
hole_two = {
        'name':'holetwo',
        'desc':'you crawl into the dimly lit hole. you follow a light to a chamber and you hear voices that lead you into a large chamber full of possums. You have no weapons. You can kill a possum with your hand but risk rabies. You can search for a weapon or use your hands.',
        'actions':{'search':'holesearch','attack':'holeattack'},
        'exit':False
}
hole_search = {
        'name':'holesearch',
        'desc':'you search the hole for some weapons but your rustling alerts the possums. stop the leader says. I know why you are here. I am not a possum. I am George Lucas! Do you listen to him or hurl the nearest rock at him?',
        'actions':{'listen':'holeattacktwo','hurl a rock':'holerock'},
        'exit':False
}
hole_attack = {
        'name':'holeattack',
        'desc':'You try to crush the possums skull but it is too quick. it bites your hand and you get space rabies, dying instantly.',
        'actions':{},
        'exit':True
}
hole_attack_two = {
        'name':'holeattacktwo',
        'desc':'this makes sense you think. possums cant talk. suddenly george lucas bites your hand and you get rabies, dying instantly.',
        'actions':{},
        'exit':True
}
hole_rock = {
        'name':'holerock',
        'desc':'you hurl the nearest rock can find and hit George Lucas in the skull. you drag his body to Yoda who is very pleased. He eats the possum and then announces he needs a nap. He tells you to go explore the swamp.',
        'actions':{'explore the swamp':'exploreswamp','explore the forest':'exploreforest'},
        'exit':False
}
explore_forest = {
        'name':'explore forest',
        'desc':'you walk around the forest. wow you say to yourself this sure is a forest. you are deep in the forest now when you here a voice.',
        'actions':{'follow the voice':'forestvoice','leave the forest':'exploreoptions'},
        'exit':False
}
forest_voice = {
        'name':'forestvoice',
        'desc':'it sounds like a mans voice. you follow it into the forest until you are surrounded by trees. you see a light in the distance',
        'actions':{'head towards the light':'forestlight','leave the forest':'exploreoptions'},
        'exit':False
}
forest_light = {
        'name':'forestlight',
        'desc':'you follow the light further and further into the forest. Now there is a voice, confident and smooth.',
        'actions':{'go to the voice':'forestfollow','leave the forest':'exploreoptions'},
        'exit':False
}
forest_follow = {
        'name':'forestfollow',
        'desc':'the light is birght and light blue now. the voice is clearer. if we look at the fourth quarter projections the voice says',
        'actions':{'go to the voice':'forestgo','leave the forest':'exploreoptions'},
        'exit':False
}
forest_go = {
        'name':'forestgo',
        'desc':'You observe from a clearing in the trees. There are a dozen men in suits crowded around a table and looking at a powerpoint. 4th quarter projections it is called.',
        'actions':{'get their attention':'forestattention','keep watching':'foresthide'},
        'exit':False
}
forest_attention = {
        'name':'forestattention',
        'desc':'Excuse me you say as you step into the clearing. what is this? the executives turn to you. hello  we are the studio executives we thought you were george lucas. have you seen him? short man? looks and talks like a possum.',
        'actions':{'lie':'forestlie', 'tell the truth':'foresttruth'}, 
        'exit':False
}
forest_lie = {
        'name':'forestlie',
        'desc':'I have seen no such person or possum you lie. I am actually Luke Skywalker. What are you doing here?',
        'actions':{'learning the force':'forestforce','i dont know':'forestwhat'},
        'exit':False
}
forest_force = {
        'name':'forestforce',
        'desc':'what? no you are supposed to be on the death star the studio executives say. we sunsetted the dagobah storyline a week ago.',
        'actions':{'wait what':'forestwait',},
        'exit':False
}
forest_what = {
        'name':'forestwhat',
        'desc':'we dont know either. you are supposed to be on the death star. we sunsetted the dagobah storyline a week ago.',
        'actions':{'wait what':'forestwait'},
        'exit':False
}
forest_wait = {
        'name':'forestwait',
        'desc':'but my ship is stuck in the swamp! fuck they say. that means we have to spend all day talking to the insurance company. someone get the special effects team. they will get the ship for you',
        'actions':{'go with the special effects guy':'foresteffect'},
        'exit':False
}
forest_effect = {
        'name':'foresteffect',
        'desc':'just then yoda, the magic talking swamp rat jumps out of the bushes. it is me yoda. i am glad you were able to find out the trick to using the force is to uhhh.... believe in yourself.',
        'actions':{'tell yoda thats some bullshit':'forestyoda'},
        'exit':False
}
forest_yoda = {
        'name':'forestyoda',
        'desc':'yoda that is some serious bullshit. yeah i know he says. you grab him and rub his face. his skin is normal colored underneath. i knew it you shout, you are no talking swamp rat, you are a midget!',
        'actions':{'fly away in your spaceship':'forestspaceship'},
        'exit':False
}
forest_spaceship = {
        'name':'forestspaceship',
        'desc':'you fly away and leave this garbage planet behind. you will never come back. not even in the sequel.',
        'actions':{},
        'exit':True
}
forest_truth = {
        'name':'foresttruth',
        'desc':'i killed a talking possum and my ship is stuck in the swamp. what why is it in the swamp? they ask. the special effects people will fix that for you',
        'actions':{'go with the special effects guy':'forseteffect'},
        'exit':False
}
forest_hide = {
        'name':'foresthide',
        'desc':'you try to hide but you see a talking space toad in the mud ahead. it screams the way talking space toads like to scream. who is there the  men say',
        'actions':{'introduce yourself':'forceattention'},
        'exit':False
}
## you haven't done any forest stuff yet.
explore_swamp = {
        'name':'exploreswamp',
        'desc':'you head to the banks of the swamp. You sit at the banks and deeply inhale the noxious green gas. You start to feel funny. Your mind is moving so fast. Do you want to stay or leave the swamp.',
        'actions':{'stay':'explorethoughts','leave':'exploreoptions'},
        'exit':False
}
explore_thoughts = {
        'name':'explorethoughts',
        'desc':'you sit at the banks of the swamp and really think. How can you fix the world? By making flashlights with scents like candles. do you want to continue exploring these deep thoughts or leave the swamp',
        'actions':{'keep thinking':'keepthinking','explore the rest of the area':'exploreoptions'},
        'exit':False
}
explore_options = {
        'name':'exploreoptions',
        'desc':'Wow theres so much to explore. What do you want to do?',
        'actions':{'go back to the swamp':'exploreswamp','explore the forest':'exploreforest'},
        'exit':False
}
keep_thinking = {
        'name':'keepthinking',
        'desc':'yes. these are genius thoughts. they will call you the flashlight genius when you are done.',
        'actions':{'keep thinking':'deepthoughts'},
        'exit':False
}
deep_thoughts = {
        'name':'deepthoughts',
        'desc':'yes. these thoughts are so deep. you are so deep. just like the pumpkin aroma on your seasonal flashlight',
        'actions':{'keep thinking':'thinkmore'},
        'exit':False
}
think_more = {
        'name':'thinkmore',
        'desc':'this is your destiny. you set about finding materials for the newest game changing scent. You set about looking for materials when you hear a womans voice. come into the swamp the voice says',
        'actions':{'follow':'swampwitch','leave':'exploreoptions'},
        'exit':False
}
swamp_goddess = {
        'name':'swampwitch',
        'desc':'I have the aromas you seek. I will give you fragrances no one else can even imagine.',
        'actions':{'go in the water':'swampdeath'},
        'exit':False
}
swamp_death = {
        'name':'swampdeath',
        'desc':'You follow the womans voice into the murky swamp water. You are waist deep in the water when the space swamp alligator attacks you. damn classic space swamp alligator luring tactics are your dying thoughts.',
        'actions':{},
        'exit':True
}

# this is shorthand way of making all of the above dictionaries into a dictionary keyed by the 'name' entries
# make sure there are no typos!
# always add the room name to the map!!!!
map = dict ( (item['name'],item) for item in (entrance_room, swamp_bow, swamp_shout, swamp_follow, hole_one, hole_search, hole_squirrel, squirrel_yoda, hole_two, hole_attack, hole_attack_two, hole_rock, explore_swamp, explore_thoughts, explore_options, keep_thinking, deep_thoughts, think_more, hole_one, swamp_goddess, swamp_death, explore_forest, forest_voice, forest_light, forest_follow, forest_go, forest_hide, forest_attention, forest_lie, forest_truth, forest_force, forest_what, forest_wait, forest_effect, forest_yoda, forest_spaceship, ))


def game_loop(room, map):
    # room is a dictionary describing an individual room or action
    # map is a dictionary of rooms, keyed by name

    sys.stdout.writelines(room['desc'])

    if room['exit']:
        sys.stdout.writelines('\nThanks for playing!')
        return

    next = None

    while not next:
        sys.stdout.writelines ("\nYou can...")
        for item in room['actions'].keys():
            sys.stdout.writelines("\n\t" + item)

        sys.stdout.writelines("\n>")
        user_input = sys.stdin.readline()
        user_input = user_input.strip().lower() # just take  lower case for simplicity
        if user_input in room['actions']:  
            next = room['actions'][user_input]
        else:
            sys.stdout.writelines("'%s' is not a supported option. Please try again\h" % user_input)
    game_loop(map[next], map)

game_loop (entrance_room, map)