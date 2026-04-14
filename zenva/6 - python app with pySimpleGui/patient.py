from datetime import datetime


class patient:
    def __init__(self, first_name, last_name, date_of_birth, height, weight, is_taking_medication):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.height = height
        self.weight = weight
        self.is_taking_medication = is_taking_medication
        

    def convert_values_to_strings(self):
        first_name = self.first_name
        last_name = self.last_name
        date_of_birth = datetime.strftime(self.date_of_birth, "%Y/%m/%d")
        height_cm = str(self.height)
        weight_kg = str(self.weight)
        is_taking_meds = str(self.is_taking_medication)

        return [first_name, last_name, date_of_birth, height_cm, weight_kg, is_taking_meds]