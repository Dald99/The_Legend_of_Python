# Write code below 💖
import random

q = input("Question: ")
num = random.randint(1, 9)

if num == 1:
    a = "Yes - definitely."
elif num == 2:
    a = "It is decidedly so."
if num == 3:
    a = "Without a doubt."
if num == 4:
    a = "Reply hazy, try again."
if num == 5:
    a = "Ask again later."
if num == 6:
    a = "Better not tell you now."
if num == 7:
    a = "My sources say no."
if num == 8:
    a = "Outlook not so good."
if num == 9:
    a = "Very doubtful."

print(f"Question: {q}")
print(f'Magic 8 Ball:  {a}')
