from car_system import (
    DATA_FILE,
    load_data,
    save_data,
    add_car_menu,
    search_car_menu,
    edit_car_menu,
    remove_car_menu,
    print_car_list,)

def main():
    cars = load_data(DATA_FILE)
    print("Welcome to the Car Inventory system")

    while True:
        print("\nWhat would you like to do today?")
        print("- Add a car? enter 1")
        print("- Search for car? enter 2")
        print("- Edit car info? enter 3")
        print("- Remove a car? enter 4")
        print("- Print the car list? enter 5")
        print("- Save the data to a file? enter 6")

        choice = input("> ").strip()

        if choice == "1":
            add_car_menu(cars)
        elif choice == "2":
            search_car_menu(cars)
        elif choice == "3":
            edit_car_menu(cars)
        elif choice == "4":
            remove_car_menu(cars)
        elif choice == "5":
            print_car_list(cars)
        elif choice == "6":
            save_data(DATA_FILE, cars)
        else:
            print("Invalid selection. Please try again.")

        cont = input("\nContinue (y/yes) or exit (n/no)? ").strip().lower()
        if cont in ("n", "no"):
            break

if __name__ == "__main__":
    main()