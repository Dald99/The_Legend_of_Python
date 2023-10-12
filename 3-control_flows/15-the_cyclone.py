# Write code below 💖

h = int(input("What's your height?: "))
c = int(input("How many credits you have?: "))

if h >= 137 and c >= 10:
    print("Enjoy the ride!")
elif h < 137 and c >= 10:
    print("You are not tall enough to ride.")
elif h >=137 and c < 10:
    print("You don't have enough credits.")
else:
    print("You have not met either requirement :(.")
