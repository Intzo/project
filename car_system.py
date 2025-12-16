DATA_FILE = "data.txt"

class Car:
    def __init__(self, car_id, name, make, body, year, value):
        self.car_id = int(car_id)
        self.name = name
        self.make = make
        self.body = body
        self.year = int(year)
        self.value = float(value)

    def __str__(self):
        return f"{self.car_id}\t{self.name}\t{self.make}\t{self.body}\t{self.year}\t{self.value:.2f}"

# Helper search functions

def find_car_by_id(cars, car_id):
    try:
        id_int = int(car_id)
    except ValueError:
        return None
    for car in cars:
        if car.car_id == id_int:
            return car
    return None

def find_car_by_name(cars, name):
    name = name.strip().lower()
    for car in cars:
        if car.name.lower() == name:
            return car
    return None

def car_exists_by_name(cars, name):
    return find_car_by_name(cars, name) is not None

# Persistence (load/save)

def load_data(filename):
    cars = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 6:
                    continue
                try:
                    car = Car(*parts)
                    cars.append(car)
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
    return cars

def save_data(filename, cars):
    with open(filename, "w", encoding="utf-8") as f:
        for car in cars:
            f.write(f"{car.car_id},{car.name},{car.make},{car.body},{car.year},{car.value}\n")
    print("Data saved to local file successfully!")
 
# Menu actions

def add_car_menu(cars):
    while True:
        print("\nEnter the car information.")
        car_id = input("Id:").strip()
        name = input("Name:").strip()
        make = input("Make:").strip()
        body = input("Body:").strip()
        year = input("Year:").strip()
        value = input("Value:").strip()

        if find_car_by_id(cars, car_id):
            print("Incorrect Id. Id already exists in the system.")
        else:
            if car_exists_by_name(cars, name):
                print("The car already exists in the inventory. No action is required.")
            else:
                try:
                    new_car = Car(car_id, name, make, body, year, value)
                    cars.append(new_car)
                    print("Car added to the inventory:")
                    print(new_car)
                except ValueError:
                    print("Invalid input. Make sure Id and Year are integers and Value is a number.")

        again = input("Do you want to add more cars? y(yes)/n(no) ").strip().lower()
        if again not in ("y", "yes"):
            break


def search_car_menu(cars):
    while True:
        print("\nTo search using the Id enter 1. To search using the Name enter 2. Enter -1 to return.")
        choice = input("> ").strip()

        if choice == "-1":
            break
        elif choice == "1":
            car = find_car_by_id(cars, input("Please Enter the id: ").strip())
            print("Car found: " + str(car) if car else "Car not found")
        elif choice == "2":
            name = input("Please Enter the car name: ").strip()
            car = find_car_by_name(cars, name)
            print("Car found: " + str(car) if car else "Car not found")
        else:
            print("Invalid selection. Please try again.")


def edit_car_menu(cars):
    while True:
        user_input = input("\nEnter the id (-1 to return): ").strip()
        if user_input == "-1":
            break

        car = find_car_by_id(cars, user_input)
        if car is None:
            print("Car not found")
        else:
            print("Enter new values (leave blank to keep current):")
            new_name = input(f"Name:").strip()
            new_make = input(f"Make:").strip()
            new_body = input(f"Body:").strip()
            new_year = input(f"Year:").strip()
            new_value = input(f"Value:").strip()

            try:
                if new_name:
                    car.name = new_name
                if new_make:
                    car.make = new_make
                if new_body:
                    car.body = new_body
                if new_year:
                    car.year = int(new_year)
                if new_value:
                    car.value = float(new_value)
                print("Car's new info is:")
                print(car)
            except ValueError:
                print("Invalid input. No changes were made.")


def remove_student_confirmation():
    pass

def remove_car_menu(cars):
    while True:
        car = find_car_by_id(cars, input("\nEnter id: ").strip())
        if car:
            cars.remove(car)
            print("Car removed")
        else:
            print("Car not found")

        if input("Remove more cars? y/n ").strip().lower() not in ("y", "yes"):
            break


def print_car_list(cars):
    if not cars:
        print("\nNo cars in inventory yet.")
        return
    
    print("\nId\tName\tMake\tBody\tYear\tValue")
    for car in sorted(cars, key=lambda c: c.car_id):
        print(car)