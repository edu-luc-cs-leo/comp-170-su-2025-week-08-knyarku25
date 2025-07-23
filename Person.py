from Birthday import Birthday


class Person:

    def __init__(self, first_name, last_name):
        """A person is defined by a first and last name, a birthday in the 
        form (month, day), and a city they live in. Additional fields may 
        be added here later. A new object requires only a first and last 
        name to instatiate. The remaining fields can be set later using 
        the corresponding mutator methods."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = None
        self.city = None

    def introduce(self):
        """Simple way for a person object to introduce itself."""
        print(
            f"Hello, my name is {self.first_name} and my birthday is on {self.say_birthday()}"
        )

    def set_birthday(self, month, day):
        """Mutator for birthday. Uses our very own Birthday class."""
        self._birthday = Birthday(month, day)

    def set_city(self, city):
        """Mutator for city."""
        self.city = city

    def get_first_name(self):
        """Accessor for first name"""
        return self.first_name

    def get_last_name(self):
        """Accessor for last name"""
        return self.last_name
    
    def say_birthday(self):
        result = "an unknown date"

        if self._birthday is not None:
            month_names = [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ]

            day = self._birthday.get_day()
            month = month_names[self._birthday.get_month() - 1]

            if day in [11, 12, 13]:
                suffix = "th"
            else:
                last_digit = day % 10
                if last_digit == 1:
                    suffix = "st"
                elif last_digit == 2:
                    suffix = "nd"
                elif last_digit == 3:
                    suffix = "rd"
                else:
                    suffix = "th"

            result = f"{day}{suffix} of {month}"

        return result

    def __lt__(self, other):
        return self.first_name < other.first_name

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.first_name} {self.last_name}]"
