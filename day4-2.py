# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:18:39 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

x,y,z=mc.player.getTilePos()
for i in range(20):
    r=random.randrange(1,5)
    if r==1:
        mc.setBlocks(x,y,z,x,y+5,z,7)
        y=y+5
    if r==2:
        mc.setBlocks(x,y,z,x,y-5,z,86)
        y=y-5
    if r==3:
        mc.setBlocks(x,y,z,x+5,y,z,20)
        x=x+5
    if r==4:
        mc.setBlocks(x,y,z,x-5,y,z,51)
        x=x-5
    if r==5:
        mc.setBlocks(x,y,z,x,y,z+5,137)
        z=z+4
    if r==6:
        mc.setBlocks(x,y,z,x,y,z-5,137)
        z=z+4