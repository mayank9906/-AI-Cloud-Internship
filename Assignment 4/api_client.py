import requests

url = "http://127.0.0.1:5000/students"

response = requests.get(url)

if response.status_code == 200:
    students = response.json()

    print("===== Student Details =====\n")

    for student in students:
        print(f"ID        : {student['id']}")
        print(f"Name      : {student['name']}")
        print(f"Course    : {student['course']}")
        print(f"Semester  : {student['semester']}")
        print(f"City      : {student['city']}")
        print("-" * 30)
else:
    print("Failed to fetch data.")
    print("Status Code:", response.status_code)