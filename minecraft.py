#Import the API
from mcpi_addons.minecraft import Minecraft
#Initialize the API (MCPI must be open and in a world at this time )
mc = Minecraft.create()
mc.postToChat("Hello World!")
X = int (input("X Coordinate: "))
Y = int (input("Y Coordinate: "))
Z = int (input("Z Coordinate: "))
X = int(X)
Y = int(Y)
Z = int(Z)
width = 10
height = 4
length = 7 
mc.setBlocks(X, Y, Z, X + width, Y + height, Z + length, 3)
mc.setBlocks(X + 1, Y, Z+1, X + width - 1, Y + height - 1, Z + length -1, 0)
