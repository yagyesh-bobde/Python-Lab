# AIM: 


items = []
total = 0
discount = 0.1 # 10% off
tax = 0.07 # 7% tax

for i in range(3): 
    print(f"Item {i+1} info")
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total+= price * quantity
    items.append([name, quantity, price])
    print()

print("********BILL********")
print("\nItem\tQuantity\tPrice")
for i in range(3):
    print(f"{items[i][0]}\t{items[i][1]}\tRs.{items[i][2]}")
print("\n****************")
print("Total Amount: Rs. ", total)
print("\n****************")
print("Discount: ",discount * 100 , "%")
print("Tax: ", round(tax * 100, 2), "%")
print("\n****************")
print("Payable Amount: Rs. ", total - (total * discount) + (total * tax))