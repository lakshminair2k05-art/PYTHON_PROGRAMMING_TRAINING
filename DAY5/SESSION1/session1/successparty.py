
day=input().strip()
#removing the leading and trailing space
attendees=int(input('enter the ATTENDEES:'))
#function in python
def classifySuccessOfParty(day,attendees):
    weekday=["MON","TUE","WED","THUR"]
    weekend=["FRI","SAT","SUN"]
    if day not in weekday and day not in weekend:
        return "INVALID DAY"
    if attendees<0:
        return "INVALID ATTENDEES"
    if day in weekday:
        if 700<=attendees<=1000:
            return "SUCCESSFUL"
        else:
            return "unsuccessful"
    if day in weekend:
        if attendees>=500:
            return "SUCCESSFUL"
        else:
            return "unsuccessful"

print(classifySuccessOfParty(day, attendees))

