#Predators vs. Prey
#During each simulation round, the following simulation occurs
#A predator will either catch prey or go hungry.
#The prey, if not eaten, will increase in popultation
#Each of these events will be based on probabilities and the roll of the dice.

#A predator eats if the dice is 4 or higher
#Prey increase their numbers if the roll is 5 or higher

import Dice

predators = 10
prey = 30
round = 1

def simulateRound():
  global predators
  global prey
  global round
  for i in range(predators):
    Dice.roll()
    if Dice.getValue() >= 4:
      prey = prey - 1 #one of the prey died.
    
  for i in range(prey):
    Dice.roll()
    if Dice.getValue() >= 5:
      prey = prey + 1
    
  #If there are fewer prey than predators, the prey start to die
  
  while (prey < predators):
    preditors = predators - 1
  
  print "After round", round
  print "Predators:", predators
  print "Prey:", prey
  round = round + 1

def simulateTenRounds():
  for i in range(10):
    simulateRound()

simulateTenRounds()