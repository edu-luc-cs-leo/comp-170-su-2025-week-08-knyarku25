from Person import Person
from Birthday import Birthday

# Create a person and set birthday and city
p1 = Person("Kofi", "Nyarku")
p1.set_birthday(6, 29)
p1.set_city("Accra")

# Test say_birthday()
print("say_birthday:", p1.say_birthday())  # Expected: 29th of June

# Test introduce()
p1.introduce()  # Expected: Hello, my name is Kofi and my birthday is on 29th of June

# Create another person for comparison
p2 = Person("Ama", "Mensah")

# Test < operator
print("Ama < Kofi:", p2 < p1)  # Expected: True

# Test Birthday.days_until()
b = Birthday(12, 29)
print("days_until 12/29:", b.days_until())  # Varies based on today's date

# Test set_month and get_month
b.set_month(4)
print("get_month after set_month(4):", b.get_month())  # Expected: 4

# Test day_in_year
print("day_in_year(4, 29):", b.day_in_year(4, 29))  # Expected: 119
