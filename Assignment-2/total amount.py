appleQuantity = int(input("How many apples do you want to buy?\n> "))
orangeQuantity = int(input("How many oranges do you want to buy?\n> "))

totalApple = appleQuantity*20
totalOrange = orangeQuantity*25
grandTotal = totalApple + totalOrange

print(f"The total amount is {grandTotal}.")