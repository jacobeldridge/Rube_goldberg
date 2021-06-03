from mine import *
import time
import pyfirmata
from playsound import playsound
board = pyfirmata.Arduino('/dev/cu.usbmodem14101')
pin9 = board.get_pin('d:9:s')
def move_servo(a):
    pin9.write(a)
# import pyfirmata

# board = pyfirmata.Arduino('/dev/cu.usbserial-1420')

def foward(x, y, z, num):
   for i in range(1, num):
      mc.setBlock(x+i,y,z, block.REDSTONE_BLOCK)
      time.sleep(.09)
      mc.setBlock(x+i,y,z, block.AIR)
   
def up(x,y,z,num):
   for i in range(1,num):
      mc.setBlock(x,y+i,z, block.REDSTONE_BLOCK)
      time.sleep(.09)
      mc.setBlock(x,y+i,z, block.AIR)
def down(x,y,z,num):
   for i in range(1,num):
      mc.setBlock(x,y-i,z, block.REDSTONE_BLOCK)
      time.sleep(.09)
      mc.setBlock(x,y-i,z, block.AIR)
def backward(x,y,z,num):
   for i in range(1, num):
      mc.setBlock(x-i,y,z, block.REDSTONE_BLOCK)
      time.sleep(.09)
      mc.setBlock(x-i,y,z, block.AIR)
def run():
   mc.setBlock(-66, 12, -210, block.REDSTONE_BLOCK)
   time.sleep(.09)
   mc.setBlock(-66, 12, -210, block.AIR)
   foward(-66, 12, -210, 4)
   down(-63, 12, -210, 2)
   foward(-63, 11, -210, 2)
   down(-62, 11, -210, 2)
   foward(-62, 10, -210, 5)
   down(-57, 10, -210, 2)
   down(-57,9,-210,2)
   foward(-57, 8, -210, 2)
   down(-56,8, -210, 2)
   backward(-56,7,-210, 4)
   down(-59,7,-210,2)
   backward(-59,5, -210, 5)
   backward(-63, 4, -210,2)
   backward(-64, 3, -210,2)
   down(-65, 3, -210, 2)
   foward(-65, 2, -210, 14)
   up(-52, 2, -210, 9)
   foward(-52, 9, -210, 5)
   foward(-48, 10, -210, 2)
   foward(-47, 10, -210, 2)
   foward(-46, 9, -210, 2)
   foward(-45, 10, -210, 2)
   foward(-44, 10, -210, 2)
   foward(-43, 9, -210, 2)
   foward(-42, 10, -210, 2)
   foward(-41, 10, -210, 2)
   foward(-40, 9, -210, 2)
   foward(-39, 9, -210, 4)
   foward(-36, 8, -210, 2)
   foward(-35, 7, -210, 7)
   foward(-29, 6, -210, 2)
   foward(-28, 5, -210, 2)
   down(-27, 5, -210, 3)
   mc.setBlock(-27, 2, -210, block.REDSTONE_BLOCK)
   iter8 = pyfirmata.util.Iterator(board)
   iter8.start()
   time.sleep(1.5)
   move_servo(90)
   playsound('/Users/jacobeldridge/Desktop/Bot/annoy.wav')
   move_servo(1)

   mc.postToChat("program done")

  

mc = Minecraft()



run()
mc.postToChat("Done")
