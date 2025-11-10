import pytest
from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept


employee_data = [
    {'name': 'Alice', 'age': '30', 'department': 'Sales', 'salary': '50000'},
    {'name': 'Bob', 'age': '25', 'department': 'Marketing', 'salary': '60000'},
    {'name': 'Charlie', 'age': '35', 'department': 'Sales', 'salary': '70000'},
    {'name': 'David', 'age': '40', 'department': 'Engineering', 'salary': '80000'},
    {'name': 'Eve', 'age': '28', 'department': 'Marketing', 'salary': '55000'},
]

def test_get_employees_by_age_range():
   
    result1 = get_employees_by_age_range(employee_data, 25, 35)
    assert len(result1) == 4
    assert 'Bob' in [emp['name'] for emp in result1]
    assert 'Alice' in [emp['name'] for emp in result1]
    assert 'Charlie' in [emp['name'] for emp in result1]
    assert 'Eve' in [emp['name'] for emp in result1]

   
    result2 = get_employees_by_age_range(employee_data, 36, 45)
    assert len(result2) == 1
    assert result2[0]['name'] == 'David'


    result3 = get_employees_by_age_range(employee_data, 50, 60)
    assert len(result3) == 0

def test_calculate_average_salary():
 
    average_salary = calculate_average_salary(employee_data)
    assert average_salary == 63000.0


    average_salary_empty = calculate_average_salary([])
    assert average_salary_empty == 0

def test_get_employees_by_dept():
  
    sales_employees = get_employees_by_dept(employee_data, 'Sales')
    assert len(sales_employees) == 2
    assert 'Alice' in [emp['name'] for emp in sales_employees]
    assert 'Charlie' in [emp['name'] for emp in sales_employees]


    engineering_employees = get_employees_by_dept(employee_data, 'Engineering')
    assert len(engineering_employees) == 1
    assert engineering_employees[0]['name'] == 'David'

    
    hr_employees = get_employees_by_dept(employee_data, 'HR')
    assert len(hr_employees) == 0