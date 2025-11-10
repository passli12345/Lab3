def get_employees_by_age_range(employee_data, min_age, max_age):
    """
    Returns a list of employees within the specified age range.

    Args:
        employee_data: A list of dictionaries, where each dictionary
                       represents an employee with an 'age' key.
        min_age: The minimum age (inclusive).
        max_age: The maximum age (inclusive).

    Returns:
        A list of employees (dictionaries) within the age range.
    """
    employees_in_range = []
    for employee in employee_data:
        age = int(employee['age'])  
        if min_age <= age <= max_age:
            employees_in_range.append(employee)
    return employees_in_range


def calculate_average_salary(employee_data):
    """
    Calculates the average salary of all employees.

    Args:
        employee_data: A list of dictionaries, where each dictionary
                       represents an employee with 'salary' as a key.

    Returns:
        The average salary of all employees, or 0 if the employee_data is empty.
    """
    if not employee_data:
        return 0

    total_salary = 0
    for employee in employee_data:
        total_salary += int(employee['salary'])  

    return total_salary / len(employee_data)


def get_employees_by_dept(employee_data, department):
    """
    Returns a list of employees in a given department.

    Args:
        employee_data: A list of dictionaries, where each dictionary
                       represents an employee with a 'department' key.
        department: The department name to filter by.

    Returns:
        A list of employees (dictionaries) in the specified department.
    """
    employees_in_dept = []
    for employee in employee_data:
        if employee['department'] == department:
            employees_in_dept.append(employee)
    return employees_in_dept