cost=input("Enter cost price of the product : ")
sell=input("Enter selling price of the same product : ")
profit=float(sell)-float(cost)#evaluating the profit
print("Profit from selling the product =",profit) #printing the profit
req_sell= float(cost) + 1.05*profit #calculating required selling price
print("The selling price for increasing the profit by 5% = ",req_sell) #revised selling price
