import datetime
x = datetime.datetime.now()

utcTime = x.strftime("%Z")
#utcTime = str(utcTime)
year = x.strftime("%Y")
sirianYear = x.year - 1193
gallicYear = sirianYear - 84
sirianYear = str(sirianYear)
gallicYear = str(gallicYear)
month = x.strftime("%m")
day = x.strftime("%d")
text = "Today is the the " + day + "." + month + "." + year + ", which is the " + day + "." + month + "." + sirianYear + " in Sirian time, and the " + day + "." + month + "." + gallicYear + " in Gallic time." + "\n" + "The current server time is" + utcTime
text = text.strip(" ")
print(text)
reeeeeeeeeee = input("")
