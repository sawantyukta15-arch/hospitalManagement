from patient import PatientManager
from employee import EmployeeTerminal

patient = PatientManager()
employee = EmployeeTerminal()

try:
    choice = int(input(
        "**Patient Management System**\n"
        "1) Patient\n"
        "2) Employee\n"
        "Enter choice: "
    ))

    match choice:
        case 1:
            patient.patient_saving_module()
        case 2:
            employee.info_patient_main()
        case _:
            print("Invalid option")

except ValueError:
    print("Please enter a valid number.")