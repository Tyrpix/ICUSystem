from InitialLR import InitialLR


class HRDayThree:
    def __init__(self, patient, current_feed):
        self.hour = 0
        self.patient = patient
        self.current_feed = current_feed

    # Get feed at 00:00 hours then every 4 hours
    def patient_round_decision(self, hourly_round):
        if self.hour % 4 == 0:
            self.current_feed = hourly_round.feed

        self.hour = self.hour + 1

        hourly_round.feed = self.current_feed

        # If GRV not empty patient goes to LR state
        if self.hour == 24 and hourly_round.day == 4:
            # Low Risk Instance
            state = InitialLR(self.patient)
            return state
        # Else repeat this state
        else:
            return self
