import csv
from django.shortcuts import render


class Employees:
    def __init__(self, file_with_path):
        self.list_of_rows = []
        self._read_csv(file_with_path)

    def _read_csv(self, file_with_path):
        with open(file_with_path) as csv_file:
            rows = csv.reader(csv_file)
            for row in rows:
                self.list_of_rows.append(row)


def table(request):
    employees_path = './data/table_of_employees.csv'
    employees = Employees(employees_path)
    my_dict = {'some_key': 'this is a value of the key named some_key'}
    context = {'hello': 'hello world', 'some_dict': my_dict, 'employees': employees}
    return render(request, 'table_app/tables-data.html', context)
