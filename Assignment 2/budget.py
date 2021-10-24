yourWallet = float(input('Your Current Money:\n> '))
priceOfApple = float(input('How much is the apple?\n> '))

#Computation
maximumNumberOfApples = int(yourWallet/priceOfApple)
remainingMoney = float(yourWallet%priceOfApple)

print(f"You can buy {maximumNumberOfApples} and your change is {remainingMoney}.") if priceOfApple <= yourWallet else print(f"Sorry, you don't have enough money.")