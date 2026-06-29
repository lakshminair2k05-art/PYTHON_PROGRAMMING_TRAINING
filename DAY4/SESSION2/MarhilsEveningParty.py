day=input("Enter the Day").strip()
# Remove Leading and Trailing Spaces
attendees=int(input("Enter the Attendees"))

# Function in Python
def classifySuccessOfParty(day,attendees):
    weekdays=["MON","TUE","WED","THU"]
    weekends=["FRI","SAT","SUN"]

    if day not in weekdays and day not in weekends:
        return "INVALID DAY"
    if attendees<0:
        return "INVALID ATTENDEES"

    if day in weekdays:
        if 700<=attendees<=1000:
            return "Successfull"
        else:
            return "Unsuccessfull"
        
    if day in weekends:
        if attendees>=1500:
            return "Successfull"
        else:
            return "Unsuccessfull"