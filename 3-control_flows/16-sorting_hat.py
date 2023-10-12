# Write code below 💖

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("**********Sorting Hat**********")

print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

a = int(input("Enter the answer (1-2): "))

if a == 1:
    gryffindor += 1
    ravenclaw += 1
elif a == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")


print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

a = int(input("Enter the answer (1-4): "))

if a == 1:
    hufflepuff += 2
elif a == 2:
    slytherin += 2
elif a == 3:
    ravenclaw += 2
elif a == 4:
    gryffindor += 2
else:
    print("Wrong input.")


print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

a = int(input("Enter the answer (1-4): "))

if a == 1:
    slytherin += 4
elif a == 2:
    hufflepuff += 4
elif a == 3:
    ravenclaw += 4
elif a == 4:
    gryffindor += 4
else:
    print("Wrong input.")

points = max(gryffindor, hufflepuff, ravenclaw, slytherin)

if gryffindor == points:
    print("🦁 Gryffindor")
elif ravenclaw == points:
    print("🦅 Ravenclaw")
elif hufflepuff == points:
    print("🦡 Hufflepuff")
else:
    print("🐍 Slytherin")
