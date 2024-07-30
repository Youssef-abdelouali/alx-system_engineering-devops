#!/usr/bin/python3
import requests
import sys
import json

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

def export_to_json(employee_data, todos_data):
    """Export the TODO list data to a JSON file."""
    user_id = employee_data.get('id')
    username = employee_data.get('username')
    filename = f"{user_id}.json"
    
    tasks = [
        {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }
        for todo in todos_data
    ]
    
    data = {str(user_id): tasks}
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Data has been exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data, todos_data = fetch_employee_data(emp_id)
    export_to_json(employee_data, todos_data)
