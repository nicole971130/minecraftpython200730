# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:23:52 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
number=1
x,y,z=mc.player.getPos()
for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
    number=number*2
    mc.postToChat(str(number))