def welcome(name):
    print(f"Welcome {name} to the drive thru menu")
    print("Here are the menu items:")
    print("1. Cheeseburger")
    print("2. Fries")
    print("3. Soda")
    print("4. Ice Cream")
    print("5. Cookie")


def get_item(a):
    if a == 1:
        return "🍔 Cheeseburger"
    elif a == 2:
        return "🍟 Fries"
    elif a == 3:
        return "🥤 Soda"
    elif a == 4:
        return "🍦 Ice Cream"
    elif a == 5:
        return "🍪 Cookie"
    else:
        return "Invalid input"


welcome("Daniel")
option = int(input("Enter your option: "))
print(f"You have selected {get_item(option)}")
