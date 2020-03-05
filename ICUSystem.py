class ICUSystem:
    def __init__(self):
        self.diagnosis_list = []

    def add_diagnosis(self, diagnosis):
        self.diagnosis_list.append(diagnosis)

    def __str__(self):
        return_str = ""
        for diagnosis in self.diagnosis_list:
            return_str += str(diagnosis) + "\n"

        return return_str
