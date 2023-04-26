# how to check if a given year is leap year or not

def isLeapYear(year):
  if(year % 100 != 0 and year % 4 == 0):
    return True
  elif(year % 100 == 0 and year % 400 == 0):
    return True
  else:
    return False

### User validation loop
while True:
  try:
    currentYear = int(input("Please enter a year: "))
    if(isLeapYear(currentYear)):
      print(currentYear, " It is a leap year")
    else:
      print(currentYear, "It is not a leap year")
  except:
    print("Please try again.")