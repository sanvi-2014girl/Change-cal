import time
calc = True
while calc:
    ready = input("Are you ready to start?Type 'quit to end: ")
    if ready == 'quit':
        break
    else:
        money = float(input("Please enter how much money you have: "))
        cost = float(input("Please enter the cost of item: "))
        money_left = money - cost
        new_money = round(money_left,2)
        print("Calculating....")
        time.sleep(1)
        print(f"You have yes
              400{new_money}")