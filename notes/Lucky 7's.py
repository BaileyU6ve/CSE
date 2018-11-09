import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
money = 15
rounds = 0
while money > 0:
    if dice1 + dice2 == 7:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print()
        print("You rolled")
        print(dice1 + dice2)
        money = money + 5
        print("Current cash")
        print(money)
        print()
        rounds = rounds + 1
    elif dice1 + dice2 < 7:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print()
        print("You rolled")
        print(dice1 + dice2)
        money = money - 1
        print("Current cash")
        print(money)
        print()
        rounds = rounds + 1
    elif dice1 + dice2 > 7:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
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


