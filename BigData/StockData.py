#http://download.finance.yahoo.com/d/quotes.csv?f=l1c1&e=.csv&s=STOCKLABEL

#Used to make requests
import urllib2
import csv

x = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?f=snl1c1v&e=.csv&s=AAPL')
textVersion = str(x.read())[2:]

list1 = (textVersion.split(','))
print(list1[1] + ": $" + list1[2])