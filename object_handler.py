import time
from threading import Thread

from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc'
        self.static_sprite_path = 'resources/sprites/static_sprites'
        self.anim_sprite_path = 'resources/sprites/animated_sprites'
        self.npc_positions = {}

        self.add_initial_sprites()
        self.add_initial_npcs()
        self.start_npc_thread()

    def add_initial_sprites(self):
        self.add_sprite(SpriteObject(self.game))
        self.add_sprite(AnimatedSprite(self.game))
        self.add_sprite(AnimatedSprite(self.game, pos=(1.25, 1.25)))
        self.add_sprite(AnimatedSprite(self.game, pos=(1.25, 7.75)))
        # self.add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'red_light/0.png', pos=(1.25, 4.75)))

    def add_initial_npcs(self):
        self.add_npc(NPC(self.game))
        self.add_npc(NPC(self.game))
        self.add_npc(NPC(self.game, pos=(11.5, 4.5)))

    def start_npc_thread(self):
        self.npc_thread = Thread(target=self.add_npc_periodically)
        self.npc_thread.daemon = True
        self.npc_thread.start()

    def add_npc_periodically(self):
        while True:
            time.sleep(10)
            new_npc = NPC(self.game, pos=(11.5, 4.5))
            self.add_npc(new_npc)


    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
