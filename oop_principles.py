#Task 1: Define Budget Category Class

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_category_name(self, category_name):
        self.__category_name = category_name

    def set_allocated_budget(self, allocated_budget):
        self.__allocated_budget = allocated_budget


#  Task 2: Implement Getters and Setters

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
        else:
            raise ValueError("Allocated budget must be a positive number")


#  Task 3: Add Budget Functionality

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
        else:
            raise ValueError("Allocated budget must be a positive number")

    # Method to add expenses and adjust the budget
    def add_expense(self, expense_amount):
        if expense_amount > 0:
            if expense_amount <= self.__allocated_budget:
                self.__allocated_budget -= expense_amount
            else:
                raise ValueError("Expense amount exceeds the allocated budget")
        else:
            raise ValueError("Expense amount must be a positive number")


# Task 4: Display Budget Details

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = 0

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
        else:
            raise ValueError("Allocated budget must be a positive number")

    # Method to add expenses and adjust the budget
    def add_expense(self, expense_amount):
        if expense_amount > 0:
            if expense_amount <= self.__allocated_budget:
                self.__allocated_budget -= expense_amount
                self.__expenses += expense_amount
            else:
                raise ValueError("Expense amount exceeds the allocated budget")
        else:
            raise ValueError("Expense amount must be a positive number")

    # Method to display budget category details
    def display_details(self):
        remaining_budget = self.__allocated_budget
        details = (
            f"Category Name: {self.__category_name}\n"
            f"Allocated Budget: ${self.__allocated_budget + self.__expenses}\n"
            f"Remaining Budget: ${remaining_budget}\n"
        )
        return details




#      2. E-commerce Product Catalog System
# Task 1 Create Base Product Class

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

# Task 2 Implement Subclass for Book

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")
# test Product  Catalog Functionality

# Example usage
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()
