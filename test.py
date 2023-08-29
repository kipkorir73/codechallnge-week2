from customer import Customer
from restaurant import Restaurant
from review import Review


customer1 = Customer("Collins", "Kipkorir")
customer2 = Customer("Brenda", "Rotich")


restaurant1 = Restaurant("Tasty Bites")
restaurant2 = Restaurant("Pizza Palace")

customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)
print(restaurant1.reviews())
print(restaurant2.reviews())
print(restaurant1.customers())
print(restaurant2.customers())
print(customer1.restaurants())
found_customer = Customer.find_by_name("Collins Kipkorir")
print(found_customer.full_name()) if found_customer else print("Customer not found")
all_johns = Customer.find_all_by_given_name("Collins")
for john in all_johns:
    print(john.full_name())

print(restaurant1.average_star_rating())
