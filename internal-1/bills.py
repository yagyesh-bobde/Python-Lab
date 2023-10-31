# develop a python program to generate bills for a grocery store. How would you take care of the 
# following:
# item names, quantities, costs, discounts, taxes, total payable amount for each item and  total bill amount

# start code
print("Creating a bill for a grocery store")
print("Enter the number of items to be billed")
n = int(input())
items = {}
items["total"] = 0
for i in range(n):
    product = {}
    print("-------------------")
    print("Enter the item name")
    item = input()
    print("Enter the quantity")
    quantity = int(input())
    print("Enter the cost per item")
    cost = float(input())
    discount = 0.1
    tax=0.0
    if (cost > 1000) : 
        discount=0.2
        tax = 0.05
    elif(cost < 500) :
        discount=0.05
        tax = 0.01
    elif(cost > 5000) : 
        discount=0.25
        tax = 0.08
    items[item]= {
        "quantity" : quantity,
        "cost" : cost,
        "discount" : discount,
        "tax" : tax,
        "total" : quantity*cost,
        "total_discount" : quantity*cost*discount,
        "total_tax" : quantity*cost*tax,
        "total_payable" : quantity*cost*(1-discount)*(1+tax)
    }
    items["total"]+=items[item]["total_payable"]


print("*******Generating bill...********")
print("Item Name\tQuantity\tCost\tDiscount\tTax\tTotal Payable")
for (item, value) in items.items():
    if item != "total":
        print(item, "\t\t", value["quantity"], "\t\t", value["cost"], "\t\t",
              value["discount"], "\t\t", value["tax"], "\t\t", value["total_payable"])
print("*******************************")
print("Total Payable Amount: ", items["total"])
