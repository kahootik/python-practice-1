
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter price per unit (KZT): "))
quantity = int(input("Enter quantity: "))


subtotal = price * quantity
discount = subtotal * 0.10 if subtotal > 5000 else 0
total = subtotal - discount


print("=" * 30)
print("SHOP RECEIPT")
print("=" * 30)
print(f"Customer : {customer_name}")
print(f"Product : {product_name}")
print(f"Price : {price} KZT")
print(f"Quantity : {quantity}")
print("-" * 30)
print(f"Subtotal : {subtotal} KZT")
print(f"Discount : {discount} KZT")
print(f"Total : {total} KZT")
print("=" * 30)


print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", total > 3000)