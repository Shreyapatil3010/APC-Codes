
inventory = {
    "Pen": 50,
    "Notebook": 30,
    "Pencil": 40
}

print("Initial Inventory:")
print(inventory)

# Add a new product
inventory["Eraser"] = 20

# Update product quantity
inventory["Pen"] = 60

# Remove a product
del inventory["Pencil"]

print("\nUpdated Inventory:")
for product, quantity in inventory.items():
    print(product, ":", quantity)

