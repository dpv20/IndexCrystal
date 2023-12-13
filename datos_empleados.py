import csv
from login.models import Employee

def import_employee_data(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Employee.objects.create(
                full_name=row['nombre completo'],
                position=row['cargo'],
                department=row['departamento'],
                country=row['pais'],
                email=row['email'],
                company=row['compania'],
            )
