actual_cost = float(input("please enter the actual price: "))
sale_amount = float(input("please enter the sales amount: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("total profit = {} in rupees".format(amount))
else:
    print("no profit!!!")