# Constructs object Diagnosis using patient object and hourly round list of objects
# Returns the objects as strings


class Diagnosis:
    def __init__(self, patient, hourly_rounds):
        self.patient = patient
        self.hourly_rounds = hourly_rounds

    def __str__(self):
        return_str = str(self.patient)

        for hourly_round in self.hourly_rounds:
            return_str += str(hourly_round)

        return return_str
