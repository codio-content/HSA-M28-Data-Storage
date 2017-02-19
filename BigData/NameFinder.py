#Baby Name Finder
#Uses the SSN baby name dataset to find popularity of a given baby name in a given year.
#Displays the number of babies born in a given year and also displays the popularity of that name in the year.

import csv

def findName(name, year):
  fileName = "BigData/names/yob" + year + ".txt"
  workingFile = open(fileName)

  data = csv.reader(workingFile)
  dataList = list(data)

  nameSpot = 0
  for entry in dataList:
    if entry[0] == name:
      break
    else:
      nameSpot += 1

  #nameSpot = dataList.index(name)
  entry = dataList[nameSpot]
  print ("There were %s babies born in %s with the name %s") %(entry[2], year, name)
  print ("It was the %d most popular name that year.")%(nameSpot)

def askName():
  name = raw_input("Enter baby name: ")
  year = raw_input("Enter birth year: ")
  findName(name, year)

def defaultName():
  findName("Olivia", "1992")
  findName("Drake", "2001")
  
defaultName() #this runs automatically