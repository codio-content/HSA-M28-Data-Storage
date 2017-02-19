#Dice.py
#A single six-sided die
#Dice can be rolled or report thier value
import random

side = 0

# Randomly select a random side 
def roll():
  global side #gain access to modify the global variable side.
  side = random.randint(1, 6) #Randomly selects numbers between 1 and 6.
  
#Return the last rolled value
def getValue():
  return side

def testDie():
  roll()
  print "The die value is", getValue()
  
  