#Simulates 20,000 infection encounters
#Half of the infections will be with an infected person
#The other half of the simulated encounters will be with a person who is not infected.

import Disease

def simulateInfected():
  infectedBySick = 0
  healthyBySick = 0

  infectedByHealthy = 0
  healthyByHealthy = 0 
  
  for i in range(10000):
    infected = Disease.contact(True)
    if infected:
      infectedBySick += 1
    else:
      healthyBySick += 1
    
  for i in range(10000):
    infected = Disease.contact(False)
    if infected:
      infectedByHealthy += 1
    else:
      healthyByHealthy += 1
      
  print "There were %d infected out of %d when they came into contact with someone already infected" %(infectedBySick, (infectedBySick + healthyBySick))
  print "There were %d infected out of %d when they came into contact with someone not infected" %(infectedByHealthy, (infectedByHealthy + healthyByHealthy))
  
simulateInfected()