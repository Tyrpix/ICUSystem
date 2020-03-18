from HRDayTwo import HRDayTwo


class HRDayOne:
    def __init__(self, patient):
        self.hour = 0
        self.patient = patient

    def patient_round_decision(self, hourly_round):

        hourly_round.feed = 1
        self.hour = self.hour + 1

        if self.hour == 24:
            state = HRDayTwo(self.patient, hourly_round.feed)
            return state
        else:
            return self

