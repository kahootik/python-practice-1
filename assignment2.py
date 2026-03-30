

customer_name = input("Enter customer name: ")

subtotal = 0.0
item_count = 0

while True:
    product_name = input("Enter product name (or 'done' to finish): ")
    
    if product_name.lower() == "done":
        break
    
    price = float(input("Enter price: "))
    
    subtotal += price
    item_count += 1
    
print(f"Customer : {customer_name.upper()}")
print(f"Items : {item_count}")
print(f"Subtotal : {subtotal} KZT")



print("-" * 30)

if subtotal < 3000:
    discount_rate = 0
    discount_label = "No discount"
elif subtotal < 7000:
    discount_rate = 0.05
    discount_label = "5% discount"
else:
    discount_rate = 0.15
    discount_label = "15% discount"

discount = subtotal * discount_rate
total = subtotal - discount

print(f"Discount tier : {discount_label}")
print(f"Discount : {discount} KZT")
print(f"Total : {total} KZT")



print(f"Name uppercase : {customer_name.upper()}")
print(f"Name lowercase : {customer_name.lower()}")
print(f"Name length : {len(customer_name)}")

if len(customer_name) > 5:
    print("Long name")
else:
    print("Short name")