class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library\n  City: {self.city}\n  Street: {self.street}\n  Zip Code: {self.zip_code}\n  Open Hours: {self.open_hours}\n  Phone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee\n  Name: {self.first_name} {self.last_name}\n  Hire Date: {self.hire_date}\n  Birth Date: {self.birth_date}\n  Address: {self.city}, {self.street}, {self.zip_code}\n  Phone: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book\n  Author: {self.author_name} {self.author_surname}\n  Publication Date: {self.publication_date}\n  Number of Pages: {self.number_of_pages}\n  Library: {self.library}"


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student\n  Name: {self.name}\n  Marks: {self.marks}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = '\n  '.join(str(book) for book in self.books)
        return f"Order\n  Employee: {self.employee}\n  Student: {self.student}\n  Order Date: {self.order_date}\n  Books:\n  {books_str}"


# Tworzenie obiektów
library1 = Library("Warsaw", "Main St", "00-001", "9-17", "123-456-789")
library2 = Library("Krakow", "Second St", "00-002", "10-18", "987-654-321")

employee1 = Employee("Jan", "Kowalski", "2020-01-01", "1980-01-01", "Warsaw", "Main St", "00-001", "123-456-789")
employee2 = Employee("Anna", "Nowak", "2021-02-02", "1990-02-02", "Krakow", "Second St", "00-002", "987-654-321")
employee3 = Employee("Piotr", "Wiśniewski", "2022-03-03", "2000-03-03", "Warsaw", "Main St", "00-001", "123-456-789")

student1 = Student("Marek", [5, 4, 3])
student2 = Student("Ewa", [5, 5, 5])
student3 = Student("Tomasz", [3, 2, 1])

book1 = Book(library1, "2000", "Adam", "Mickiewicz", 300)
book2 = Book(library2, "2001", "Henryk", "Sienkiewicz", 400)
book3 = Book(library1, "2002", "Juliusz", "Słowacki", 200)
book4 = Book(library2, "2003", "Maria", "Konopnicka", 350)
book5 = Book(library1, "2004", "Bolesław", "Prus", 250)

order1 = Order(employee1, student1, [book1, book2], "2023-11-01")
order2 = Order(employee2, student2, [book3, book4, book5], "2023-11-02")

# Wyświetlenie zamówień
print(order1)
print("\n")
print(order2)
