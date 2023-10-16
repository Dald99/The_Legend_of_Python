import random


def play():
    while True:
        symbols = ['🍒', ' 🍇', '🍉', '7️⃣']
        results = random.choices(symbols, k=3)

        print("------------------")
        print(f"{results[0]}|{results[1]}|{results[2]}")

        if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
            print("Jackpot! 💰")
        else:
            print("Thanks for playing!")

        option = input("Play again? (y/n): ")
        if option.lower() != 'y':
            break


play()
