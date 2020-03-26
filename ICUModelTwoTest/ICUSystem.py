# Constructs the object ICU System with all patient objects and their respective data which is stored in a list
from HRDayOne import HRDayOne
from InitialLR import InitialLR


class ICUSystem:
    def __init__(self):
        # Holds diagnosis for each patient (patient + hourly round data)
        self.diagnosis_list = []
        self.day = 1
        # Date time object here starting at 00:00
        self.hour = 0

    def add_diagnosis(self, diagnosis):
        self.diagnosis_list.append(diagnosis)

    def __str__(self):
        return_str = ""
        for diagnosis in self.diagnosis_list:
            return_str += str(diagnosis) + "\n"
        return return_str

    # Retrieve the patient from the state.
    @staticmethod
    def get_patient(state):
        return state.patient

    # Retrieve the hourly rounds from the diagnosis list
    # for a particular patient
    def get_hourlyrounds_for_patient(self, patient_data):
        #  Find the diagnosis information for the particular patient
        for diagnosis in self.diagnosis_list:
            # Check patient in diagnosis is same as stored patient
            if diagnosis.patient == patient_data:
                return diagnosis.hourly_rounds

    @staticmethod
    def get_hourlyround_for_daytime(hourly_rounds, day, hour):
        for hourly_round in hourly_rounds:
            if hourly_round.time == hour and int(hourly_round.day) == day:
                return hourly_round

    def perform_rounds(self):
        # Holds the current state of the patient
        state_list = []

        # Iterate through all diagnosis' and assign starting state
        # Either High Risk or Low Risk
        # The diagnosis contains the patient and the hourly rounds
        for diagnosis in self.diagnosis_list:
            state = None
            if diagnosis.patient.risk == "HR":
                state = HRDayOne(diagnosis.patient)
            else:
                state = InitialLR(diagnosis.patient)
            state_list.append(state)

        # Iterate through each day and hour calling each patient state
        # to determine what to do next
        for day in range(1, 5):
            for hour in range(0, 24):
                #  Iterate through the state list, this contains the state and the patient as a context
                for i in range(len(state_list)):
                    # Get patient at index in state list
                    #  Retrieve the patient for the current state
                    patient_data = ICUSystem.get_patient(state_list[i])

                    # Retrieve the hourly rounds for the patient
                    hourly_rounds = self.get_hourlyrounds_for_patient(patient_data)

                    # Retrieve the hourly round for the particular day and hour
                    hourly_round = ICUSystem.get_hourlyround_for_daytime(hourly_rounds, day, hour)

                    # Call the state with the hourly round information to determine the action
                    # to perform given the context of the patient
                    current_state = state_list[i].patient_round_decision(hourly_round)
                    state_list[i] = current_state
