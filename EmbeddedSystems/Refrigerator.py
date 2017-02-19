#The code that would be embedded in the microcontroller of a refrigerator.
#For the purposes of this 

import SimulateTemp

setTemp = 40
global temp
coolCount = 0

def fridgeOS():
  global temp
  temp = SimulateTemp.getNewTemp(32, 60)
  cycle = 0
  while (cycle < 100): # we will simulate 100 cycles... in a real refrigerator it would always be going.
    
    temp = temp + .5 # temp goes up 1/2 degree per cycle due to outside air temp
    if (temp > setTemp):
      print "Cycle", cycle, "\t Temp:", temp
      print "Cooling"
      cool()
    
    cycle = cycle + 1
  
  print "The refrigerator ran for", coolCount, "cycles."
  
def cool():
  global temp
  global coolCount
  temp = temp - 2
  coolCount = coolCount + 1
    
fridgeOS()