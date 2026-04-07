

instructions = "List all patients, press 1\n run new diagnosis, press 2\n exit, press 3\n"

prompt_name = "Enter patient's name:\n"
prompt_appearance = "Enter patient's appearance:\n 1: normal appearance\n 2: irritable or lethargic\n"
prompt_skin = "Enter patient's skin condition:\n 1: skin pinch normal\n 2: skin pinch slow\n"
prompt_eye = "Enter patient's eye condition:\n 1: eyes normal or slightly sunken\n 2: very sunken eyes\n"

conclusion_no_dehydration = "Patient is not dehydrated."
conclusion_mild_dehydration = "Patient is mildly dehydrated."
conclusion_severe_dehydration = "Patient is severely dehydrated."
input_invalid = "Invalid input. Please try again."
error_message_empty_name = "Error: name cannot be empty, diagnosis aborted."
error_message_invalid_input = "Error: invalid input, diagnosis aborted."

patients = []

# structure of the program
def main():
    print("Welcome doctor.", "What would be the problem sir ?", sep="\n")
    while (True):
        choice = input(instructions)
        if choice == "1":
            list_patients() 
        elif choice == "2":
            start_new_diagnosis()
        elif choice == "3":
            print("Goodbye!")
            return
        
def list_patients():
    print("List of patients:")
    for patient in patients:
        if (patient):
            print(patient)

def start_new_diagnosis():
    name = get_name()
    diagnosis = get_diagnosis()
    compute_diagnosis(name, diagnosis)

# getters for user input
def get_name():
    name = input(prompt_name)
    return name

def get_appearance():
    appearance = input(prompt_appearance)
    return appearance

def get_skin_condition():
    skin_condition = input(prompt_skin)
    return skin_condition

def get_eye_condition():
    eye_condition = input(prompt_eye)
    return eye_condition

def get_diagnosis():
    diagnosis = diagnose_appearance()
    return diagnosis

# diagnosis logic
def diagnose_appearance():
    appearance = get_appearance()
    if (appearance == "1"):
        eye_condition = get_eye_condition()
        return diagnose_eye_condition(eye_condition)
    elif (appearance == "2"):
        skin_condition = get_skin_condition()
        return diagnose_skin_condition(skin_condition)
    else:
        return input_invalid

def diagnose_skin_condition(skin_condition):
    if skin_condition == "1":
        return conclusion_mild_dehydration
    elif skin_condition == "2":
        return conclusion_severe_dehydration
    else:
        return input_invalid

def diagnose_eye_condition(eye_condition):
    if eye_condition == "1":
        return conclusion_no_dehydration
    elif eye_condition == "2":
        return conclusion_severe_dehydration
    else:
        return input_invalid

# diagnosis computation
def compute_diagnosis(name, diagnosis):
    if (name == ""):
        print(error_message_empty_name)
        return
    
    if diagnosis == input_invalid:
        print(error_message_invalid_input)
        return
    
    print(f"Diagnosis for {name}: {diagnosis}")
    save_new_diagnosis(name, diagnosis)

def save_new_diagnosis(name, diagnosis):
    entry = f"{name}: {diagnosis}"
    patients.append(entry)
    print(f"Diagnosis recorded")


#main()


# unit tests
def unit_tests():
    test_diagnose_skin()
    test_diagnose_eye()
    test_compute_diagnosis()

def test_diagnose_skin():
    assert diagnose_skin_condition("1") == conclusion_mild_dehydration, "diagnose skin: invalid return value"
    assert diagnose_skin_condition("2") == conclusion_severe_dehydration, "diagnose skin: invalid return value"
    assert diagnose_skin_condition("3") == input_invalid, "diagnose skin: invalid return value"

def test_diagnose_eye():
    assert diagnose_eye_condition("1") == conclusion_no_dehydration, "diagnose eye: invalid return value"
    assert diagnose_eye_condition("2") == conclusion_severe_dehydration, "diagnose eye: invalid return value"
    assert diagnose_eye_condition("3") == input_invalid, "diagnose eye: invalid return value"

def test_compute_diagnosis():
    compute_diagnosis("", conclusion_no_dehydration)
    compute_diagnosis("Marine", conclusion_severe_dehydration)
    compute_diagnosis("John Doe", input_invalid)
    compute_diagnosis("John Doe", conclusion_no_dehydration)
    assert patients == ["Marine: Patient is severely dehydrated.", "John Doe: Patient is not dehydrated."], "compute diagnosis: invalid patient record"

unit_tests()