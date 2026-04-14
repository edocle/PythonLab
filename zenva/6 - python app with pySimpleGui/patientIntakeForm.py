import FreeSimpleGUI as sg


def create_layout():
    return [
    [sg.Text("First name"), sg.Input(key="FIRST_NAME")],
    [sg.Text("Last name"), sg.Input(key="LAST_NAME")],
    [sg.Text("Date of Birth"), sg.Input(key="DOB"), sg.CalendarButton("select date", target="DOB", format="%Y/%m/%d")],
    [sg.Text("Height (cm)"), sg.Input(key="HEIGHT")],
    [sg.Text("Weight (kg)"), sg.Input(key="WEIGHT")],
    [sg.Text("Takes medication ?"), sg.Checkbox("", key="TAKES_MEDICATION")],
    [sg.Cancel(), sg.Button("Save", key="SUBMIT")]
]

def display_intake_form(): 
    intake_window = sg.Window("New patient Intake Form", create_layout())
    
    while True:
        event, values = intake_window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            intake_window.close()
            break

        elif event == "SUBMIT":
            intake_window.close()
            return read_input_values(values)

def read_input_values(values):
    first_name = values["FIRST_NAME"]
    last_name = values["LAST_NAME"]
    dob = values["DOB"]
    height = values["HEIGHT"]
    weight = values["WEIGHT"]
    takes_medication = values["TAKES_MEDICATION"]

    return first_name, last_name, dob, height, weight, takes_medication
