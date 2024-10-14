# 2 eggs + 250 ml milk + 100g flour = 8 pancakes
# 1 egg + 125 ml milk + 50g flour = 4 pancakes

eggs = int(input("Amount of eggs: "))
milk = int(input("ml milk: "))
flour = int(input("grammes of flour: "))

eggsForPancakes = eggs*4
milkForPancakes = milk//30
flourForPancakes = flour//12.5

pancakeAmount = min(eggsForPancakes, milkForPancakes, flourForPancakes)

if pancakeAmount < 1:
    print("Not enough for pancakes!")
else: 
    print(f"You can make {pancakeAmount} pancake(s)")

