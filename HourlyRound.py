class HourlyRound:
    def __init__(self, day, time, feed, grv, issues):
        self.day = day
        self.time = time
        self.feed = feed
        self.grv = grv
        self.issues = issues

    def __str__(self):
        return_str = "|Day: " + self.day
        # datetime object must be wrapped in str, removed unused seconds from string
        return_str += "|Time: " + str(self.time)[:-3]
        return_str += "|Feed: " + self.feed
        return_str += "|GRV: " + self.grv
        return_str += "|Issues: " + self.issues + "|\n"
        return return_str
