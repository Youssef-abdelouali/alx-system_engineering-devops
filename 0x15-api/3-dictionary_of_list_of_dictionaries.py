import json

# Sample data structure (replace this with your actual data source)
data = {
    1: [
        {"username": "Bret", "task": "delectus aut autem", "completed": False},
        {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": False},
        # Add more tasks here...
    ],
    2: [
        {"username": "Antonette", "task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": False},
        {"username": "Antonette", "task": "distinctio vitae autem nihil ut molestias quo", "completed": True},
        # Add more tasks here...
    ],
    # Add more users here...
}

# Create the formatted data structure
formatted_data = {}
for user_id, tasks in data.items():
    formatted_data[str(user_id)] = tasks

# Write to JSON file
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(formatted_data, json_file, indent=4)

print("Data successfully exported to todo_all_employees.json")
