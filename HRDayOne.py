class HRDayOne:
    def __init__(self, patient, current_feed):
        self.hour = 0
        self.patient = patient
        self.current_feed = current_feed

    def patient_round_decision(self, hourly_round):
        hourly_round.feed = 1
        self.hour = self.hour + 1

        if self.hour == 24:
            state = HRDayTwo()
            return state
        else:
            return self

