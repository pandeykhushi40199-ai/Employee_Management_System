class Employee:

    def __init__(
        self,
        employee_id,
        name,
        email,
        phone,
        department,
        salary,
        joining_date,
        location
    ):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.phone = phone
        self.department = department
        self.salary = salary
        self.joining_date = joining_date
        self.location = location