#!/usr/bin/python3
import requests
import sys
import csv

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

def export_to_csv(employee_data, todos_data):
    """Export the TODO list data to a CSV file."""
    user_id = employee_data.get('id')
    username = employee_data.get('username')
    filename = f"{user_id}.csv"
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([user_id, username, todo.get('completed'), todo.get('title')])
    
    print(f"Data has been exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data, todos_data = fetch_employee_data(emp_id)
    export_to_csv(employee_data, todos_data)
