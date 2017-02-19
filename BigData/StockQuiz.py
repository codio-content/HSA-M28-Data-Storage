#Used to make requests
import urllib2
import csv

def getName(stock):
  x = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?f=snl1c1v&e=.csv&s=AAPL')
  textVersion = str(x.read())[2:]

  list1 = (textVersion.split(','))
  return list[1]

def getPrice(stock):
  x = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?f=snl1c1v&e=.csv&s=AAPL')
  textVersion = str(x.read())[2:]

  list1 = (textVersion.split(','))
  return list[2]