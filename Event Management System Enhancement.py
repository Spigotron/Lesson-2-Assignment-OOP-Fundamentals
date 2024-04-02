class Event:
    def __init__(self, name, date, participants):
        self.name = name
        self.date = date
        self.participants = participants

    def add_participant(self):
        self.participants += 1

    def get_participant_count(self):
        print(f"This is the number of people attending {Gala.name}: {Gala.participants}.")
            
Gala = Event("Gala", "August 23, 2024", 0)
            
Gala.add_participant()
Gala.get_participant_count()