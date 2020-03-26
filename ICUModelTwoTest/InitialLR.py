from GRVCheck import GRVCheck


class InitialLR:
    def __init__(self, patient):
        self.hour = 0
        self.patient = patient
        self.grv = None

    def patient_round_decision(self, hourly_round):
        # Record the last known GRV as these do not seem
        # to occur when needed in flow chart
        if hourly_round.grv is not 0:
            self.grv = hourly_round.grv

        # Every 2 hours feed according to weight for a max of 4 hours
        # This is at 0 and 2 hours
        if self.hour == 0 or self.hour == 2:
            if self.patient.weight > 40:
                hourly_round.feed = 20.0
            else:
                hourly_round.feed = 5.0
        else:
            # Inbetween set to zero
            hourly_round.feed = 0

        hourly_round.issues = "NONE"

        # Feed at this rate for 4 hours
        if self.hour == 4:
            # Is the GRV > 5mls/kg
            ratio = self.grv / self.patient.weight
            if ratio > 5.0:
                # Create the new state (pause feed) and return the new state
                print("********** GO TO YES BRANCH")
            else:
                # Set the feed to 10ml or 30mls if > 40kg.
                # Create the new state to continue on this route, and return the new state
                print("********** GOT TO NO BRANCH")

        self.hour = self.hour + 1

        return self






