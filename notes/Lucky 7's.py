import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
money = 15
rounds = 0
while money > 0:
    if dice1 + dice2 == 7:
        money = money + 5
        rounds = rounds + 1
        print(money)
    elif dice1 + dice2 < 7:
        money = money - 1
        print(money)
        rounds = rounds + 1
    elif dice1 + dice2 > 7:
        money = money - 1
        print(money)
        rounds = rounds + 1
print("You're Broke")
print("Rounds Played -")
print(rounds)


