from controller.employee_controller import (
    add_employee,
    view_employees,
    search_employee,
    update_employee,
    delete_employee
)


def main():

    while True:

        print("\n")
        print("=" * 50)
        print("       EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("\nThank you for using Employee Management System!")
            break

        else:
            print("\nInvalid choice! Please enter 1-6.")


if __name__ == "__main__":
    main()