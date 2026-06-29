
rain=int(input("Enter the amount of rainfall in mm: "))
if rain in range(0, 1):
    print("No rain")
elif rain in range(1, 5):
    print("Light rain")
elif rain in range(5, 10):
    print("Moderate rain")
else :
    print("Heavy rain")
    
