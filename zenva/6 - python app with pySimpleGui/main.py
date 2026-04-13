import dataFunctions
import FreeSimpleGUI as sg


def main():
    patients_window = sg.Window('Patients list', patients_window_layout)
    
    while True:
        event, values = patients_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "ADD_NEW_PATIENT":
            press_add_new_patient()

    patients_window.close()

def press_add_new_patient():
    print("add new patient button clicked")

table_headings = ["First Name", "Last Name", "Date of Birth", "Height (cm)", "Weight (kg)", "takes medication"]
table_data = dataFunctions.convert_patients_to_table_data()
patients_window_layout = [
    [sg.Text("all patients data"), sg.Button("Add new patient", key="ADD_NEW_PATIENT")],
    [sg.Table(headings=table_headings,values=table_data)]
]


main()