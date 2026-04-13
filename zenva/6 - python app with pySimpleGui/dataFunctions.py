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