import json

class PharmacyPOS:
    def __init__(self):
        self.medicines = {}
        self.customer_cart = []

    def load_medicines(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.medicines = json.load(file)
        except FileNotFoundError:
            print("Medicine database file not found.")

    def save_medicines(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.medicines, file)

    def add_medicine(self, name, price):
        self.medicines[name] = price
        print(f"Medicine {name} added with price {price}.")

    def remove_medicine(self, name):
        if name in self.medicines:
            del self.medicines[name]
            print(f"Medicine {name} removed from the database.")
        else:
            print(f"Medicine {name} not found in the database.")

    def search_medicine(self, name):
        return self.medicines.get(name, None)

    def assign_medicine_to_customer(self, name):
        price = self.search_medicine(name)
        if price is not None:
            self.customer_cart.append((name, price))
            print(f"Medicine {name} added to customer cart.")
        else:
            print(f"Medicine {name} not found in the database.")

    def calculate_total_cost(self):
        total = sum(price for name, price in self.customer_cart)
        total_with_tax = total * 1.075
        return total_with_tax

    def checkout(self, amount_paid):
        total_cost = self.calculate_total_cost()
        difference = amount_paid - total_cost
        self.customer_cart.clear()
        return total_cost, difference

# Example usage
pharmacy = PharmacyPOS()
pharmacy.load_medicines('medicines.json')  # Load existing medicines from a file

# Adding medicines
pharmacy.add_medicine('Aspirin', 10.0)
pharmacy.add_medicine('Ibuprofen', 15.0)
pharmacy.add_medicine('Paracetamol', 7.5)

# Searching for a medicine
print(pharmacy.search_medicine('Ibuprofen'))  # Output: 15.0

# Assigning medicines to a customer
pharmacy.assign_medicine_to_customer('Aspirin')
pharmacy.assign_medicine_to_customer('Paracetamol')

# Calculating total cost with tax
total_cost = pharmacy.calculate_total_cost()
print(f"Total cost with tax: {total_cost}")

# Checkout process
amount_paid = 20.0
total_cost, change = pharmacy.checkout(amount_paid)
print(f"Total cost: {total_cost}, Change: {change}")

# Removing a medicine from the database
pharmacy.remove_medicine('Ibuprofen')

# Save updated medicines to a file
pharmacy.save_medicines('medicines.json')
