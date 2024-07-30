#!/usr/bin/python3
import requests
import sys

def fetch_employee_data(employee_id):
    """Fetch the employee data from the API and return it as a dictionary."""
    try:
        # URLs for user and todo information
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        
        # Fetch user data
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        
        # Fetch todos data
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        return user_data, todos_data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

def print_employee_progress(employee_data, todos_data):
    """Print the employee TODO list progress."""
    employee_name = employee_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo.get('completed'))
    
    # Print the summary line
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    
    # Print the completed tasks
    for todo in todos_data:
        if todo.get('completed'):
            print(f"\t {todo.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data, todos_data = fetch_employee_data(emp_id)
    print_employee_progress(employee_data, todos_data)
