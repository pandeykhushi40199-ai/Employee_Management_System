from config.database import create_connection
from model.employee_model import Employee


# =========================================================
# CREATE - ADD EMPLOYEE
# =========================================================

def add_employee():

    print("\n========== ADD EMPLOYEE ==========")

    connection = None
    cursor = None

    try:
        employee_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
        location = input("Enter Location: ")

        employee = Employee(
            employee_id,
            name,
            email,
            phone,
            department,
            salary,
            joining_date,
            location
        )

        connection = create_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
        INSERT INTO employees
        (
            employee_id,
            name,
            email,
            phone,
            department,
            salary,
            joining_date,
            location
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            employee.employee_id,
            employee.name,
            employee.email,
            employee.phone,
            employee.department,
            employee.salary,
            employee.joining_date,
            employee.location
        )

        cursor.execute(query, values)
        connection.commit()

        print("\nEmployee added successfully!")

    except ValueError:
        print("\nInvalid input! Please enter correct values.")

    except Exception as error:
        print("\nError:", error)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


# =========================================================
# READ - VIEW ALL EMPLOYEES
# =========================================================

def view_employees():

    print("\n========== ALL EMPLOYEES ==========")

    connection = None
    cursor = None

    try:
        connection = create_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = "SELECT * FROM employees"

        cursor.execute(query)

        employees = cursor.fetchall()

        if not employees:
            print("\nNo employee records found.")
            return

        print("-" * 140)

        print(
            f"{'ID':<8}"
            f"{'Name':<20}"
            f"{'Email':<28}"
            f"{'Phone':<15}"
            f"{'Department':<15}"
            f"{'Salary':<12}"
            f"{'Joining Date':<15}"
            f"{'Location':<15}"
        )

        print("-" * 140)

        for employee in employees:

            print(
                f"{employee[0]:<8}"
                f"{employee[1]:<20}"
                f"{employee[2]:<28}"
                f"{employee[3]:<15}"
                f"{employee[4]:<15}"
                f"{employee[5]:<12}"
                f"{str(employee[6]):<15}"
                f"{employee[7]:<15}"
            )

        print("-" * 140)

    except Exception as error:
        print("\nError:", error)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


# =========================================================
# READ - SEARCH EMPLOYEE
# =========================================================

def search_employee():

    print("\n========== SEARCH EMPLOYEE ==========")

    connection = None
    cursor = None

    try:
        employee_id = int(input("Enter Employee ID: "))

        connection = create_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
        SELECT *
        FROM employees
        WHERE employee_id = %s
        """

        cursor.execute(query, (employee_id,))

        employee = cursor.fetchone()

        if employee:

            print("\nEmployee Found!")
            print("--------------------------------")
            print("Employee ID :", employee[0])
            print("Name        :", employee[1])
            print("Email       :", employee[2])
            print("Phone       :", employee[3])
            print("Department  :", employee[4])
            print("Salary      :", employee[5])
            print("Joining Date:", employee[6])
            print("Location    :", employee[7])
            print("--------------------------------")

        else:
            print("\nEmployee not found.")

    except ValueError:
        print("\nEmployee ID must be a number.")

    except Exception as error:
        print("\nError:", error)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


# =========================================================
# UPDATE EMPLOYEE
# =========================================================

def update_employee():

    print("\n========== UPDATE EMPLOYEE ==========")

    connection = None
    cursor = None

    try:
        employee_id = int(input("Enter Employee ID: "))

        connection = create_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        check_query = """
        SELECT *
        FROM employees
        WHERE employee_id = %s
        """

        cursor.execute(check_query, (employee_id,))

        employee = cursor.fetchone()

        if not employee:
            print("\nEmployee not found.")
            return

        print("\nWhat do you want to update?")

        print("1. Name")
        print("2. Email")
        print("3. Phone")
        print("4. Department")
        print("5. Salary")
        print("6. Joining Date")
        print("7. Location")

        choice = input("Enter your choice: ")

        if choice == "1":

            new_value = input("Enter new name: ")

            query = """
            UPDATE employees
            SET name = %s
            WHERE employee_id = %s
            """

        elif choice == "2":

            new_value = input("Enter new email: ")

            query = """
            UPDATE employees
            SET email = %s
            WHERE employee_id = %s
            """

        elif choice == "3":

            new_value = input("Enter new phone: ")

            query = """
            UPDATE employees
            SET phone = %s
            WHERE employee_id = %s
            """

        elif choice == "4":

            new_value = input("Enter new department: ")

            query = """
            UPDATE employees
            SET department = %s
            WHERE employee_id = %s
            """

        elif choice == "5":

            new_value = float(input("Enter new salary: "))

            query = """
            UPDATE employees
            SET salary = %s
            WHERE employee_id = %s
            """

        elif choice == "6":

            new_value = input(
                "Enter new joining date (YYYY-MM-DD): "
            )

            query = """
            UPDATE employees
            SET joining_date = %s
            WHERE employee_id = %s
            """

        elif choice == "7":

            new_value = input("Enter new location: ")

            query = """
            UPDATE employees
            SET location = %s
            WHERE employee_id = %s
            """

        else:
            print("\nInvalid choice.")
            return

        cursor.execute(query, (new_value, employee_id))

        connection.commit()

        print("\nEmployee updated successfully!")

    except ValueError:
        print("\nInvalid input.")

    except Exception as error:
        print("\nError:", error)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


# =========================================================
# DELETE EMPLOYEE
# =========================================================

def delete_employee():

    print("\n========== DELETE EMPLOYEE ==========")

    connection = None
    cursor = None

    try:
        employee_id = int(input("Enter Employee ID: "))

        connection = create_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        check_query = """
        SELECT name
        FROM employees
        WHERE employee_id = %s
        """

        cursor.execute(check_query, (employee_id,))

        employee = cursor.fetchone()

        if not employee:
            print("\nEmployee not found.")
            return

        print("\nEmployee Name:", employee[0])

        confirmation = input(
            "Are you sure you want to delete this employee? (y/n): "
        )

        if confirmation.lower() == "y":

            query = """
            DELETE FROM employees
            WHERE employee_id = %s
            """

            cursor.execute(query, (employee_id,))

            connection.commit()

            print("\nEmployee deleted successfully!")

        else:
            print("\nDelete operation cancelled.")

    except ValueError:
        print("\nEmployee ID must be a number.")

    except Exception as error:
        print("\nError:", error)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()