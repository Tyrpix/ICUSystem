from HRDayThree import HRDayThree

class HRDayTwo:
    def __init__(self, patient, current_feed):
        self.hour = 0
        self.patient = patient
        self.current_feed = current_feed

    def patient_round_decision(self, hourly_round):
        if self.hour == 0:
            self.current_feed = self.current_feed + 1
        elif self.hour == 11:
            self.current_feed = self.current_feed + 1

        self.hour = self.hour + 1

        hourly_round.feed = self.current_feed

        if self.hour == 24:
            state = HRDayThree(self.patient, hourly_round.feed)
            return state
        else:
            return self
