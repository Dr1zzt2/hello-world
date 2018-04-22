import random
rolls_attacker=[]
rolls_defender=[]
lose=[0,0]
answer = 0
while answer < 1 or answer > 3:
    try:
        answer = int(input("Number of Attackers(Max3): "))
    except ValueError:
        continue
for x in range(answer):
    rolls_attacker.append(random.randint(1, 6))
answer = 0
while answer < 1 or answer > 2:
    try:
        answer = int(input("Number of Defenders(Max2): "))
    except ValueError:
        continue
for x in range(answer):
    rolls_defender.append(random.randint(1, 6))
answer = 0
print("Dice\n  Attacker: ", end="")
rolls_attacker.sort(reverse=True)
print(rolls_attacker)
print("  Defender: ", end="")
rolls_defender.sort(reverse=True)
print(rolls_defender)
print()
for x in range(0,len(rolls_defender)):
    if rolls_defender[x] >= rolls_attacker[x]:
        lose[0] = lose[0] + 1
    else: lose[1] = lose[1] + 1
print("Outcome\n  Attacker: ", end="")
print(f"Lost {lose[0]} units.")
print("  Defender: ", end="")
print(f"Lost {lose[1]} units.")