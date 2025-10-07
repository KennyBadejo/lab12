#import the API
from mcpi_addons.minecraft import Minecraft
#Initialize the API
mc = Minecraft.create()
import time

pos = mc.player.getPos()
mc.setBlocks(pos.x, pos.y -1, pos.z, 12)
time.sleep(1)
mc.player.setTilePos(0,0,0)
  
