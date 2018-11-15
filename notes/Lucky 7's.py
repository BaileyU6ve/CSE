import random
money = 15
rounds = 0
while money > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        money = money - 1
        money = money + 5
        print()
        print("You rolled")
        print(dice1 + dice2)
        print("Current cash")
        print(money)
        print()
        rounds = rounds + 1
    elif dice1 + dice2 < 7:
        print()
        print("You rolled")
        print(dice1 + dice2)
        money = money - 1
        print("Current cash")
        print(money)
        print()
        rounds = rounds + 1
    elif dice1 + dice2 > 7:
        print()
        print("You rolled")
        print(dice1 + dice2)
        money = money - 1
        print("Current cash")
        print(money)
        print()
        rounds = rounds + 1
    elif money > 50:
        dice1 = random.randint(1, 3)
        dice2 = random.randint(1, 3)
        print()
        print("You rolled")
        print(dice1 + dice2)
        money = money - 1
        print("Current cash")
        print(money)
        print()
        rounds = rounds + 1
print()
print("You're Broke")
print("Rounds Played -")
print(rounds)


