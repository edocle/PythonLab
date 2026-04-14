from patient import patient
from datetime import datetime

patients = [
    patient("john", "doe", datetime(1990, 5, 18), 179.0, 65.0, False),
    patient("jim", "beam", datetime(1985, 3, 10), 180.0, 75.0, False),
    patient("jack", "daniels", datetime(1988, 11, 5), 175.0, 70.0, True),
    patient("jill", "valentine", datetime(1991, 6, 15), 168.0, 60.0, False),
    patient("jason", "bourne", datetime(1987, 9, 12), 182.0, 78.0, True)
]

def convert_patients_to_table_data():
    patients_data = []
    for patient in patients:
        strings = patient.convert_values_to_strings()
        patients_data.append(strings)
    return patients_data

def try_to_create_patient(values):
    try:
        first_name = values[0]
        last_name = values[1]
        date_of_birth = datetime.strptime(values[2], "%Y/%m/%d")
        height = float(values[3])
        weight = float(values[4])
        is_taking_medication = bool(values[5])

        if len(first_name) < 2 or len(last_name) < 2:
            return False
        if date_of_birth == "" or date_of_birth >= datetime.now():
            return False
        if height == "" or height <= 0 or weight == "" or weight <= 0:
            return False


        new_patient = patient(first_name, last_name, date_of_birth, height, weight, is_taking_medication)
        patients.append(new_patient)
        print("Patient created successfully: " + first_name + " " + last_name)
        return True
    except Exception as e:
        print("Error creating patient:", e)
        return False
    
